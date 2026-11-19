from collections.abc import Iterable, Iterator
from math import isfinite
from typing import Any


import logging
raw_events = [
    {
        "event_id": "evt_001",
        "timestamp": "2026-11-17T10:20:00Z",
        "service": {"name": "checkout-svc", "version": "1.4.2", "region": "ap-south-1"},
        "metrics": {"cpu_pct": 68.4, "memory_mb": 512, "latency_ms": 120},
        "tags": ["prod", "critical"],
    },
    {
        "event_id": "evt_002",
        "timestamp": "2026-11-17T10:20:05Z",
        "service": {"name": "auth-svc"},  # missing version and region
        "metrics": None,  # null payload instead of dict
        "tags": [],
    },
    {
        "event_id": "evt_003",
        "timestamp": "2026-11-17T10:20:10Z",
        # completely missing "service" and "tags" keys
        "metrics": {"cpu_pct": 12.1, "latency_ms": "invalid_str"},
    },
    {
        "event_id": "evt_004",
        "service": "malformed_string_instead_of_dict",  # type drift trap
        "metrics": {"cpu_pct": 91.0, "memory_mb": 1024, "latency_ms": 450},
        "tags": None,
    },
]

def _parse_float(val: Any) -> float | None:
    """Helper function which parses stringified floating point numbers to decimals.

    Args:
        val (Any): Input to the helper function

    Returns:
        float | None: returns a decimal value if the input is a valid stringified floating point number else None
    """
    if val is None or isinstance(val, bool):
        return None
    try:
        parsed = float(val)
    except(TypeError, ValueError):
        return None
    return parsed if isfinite(parsed) else None

def _parse_int(val: Any) -> int | None:
    """Helper function which parses stringified numbers to integer.
    Floating point numbers are type-casted to integer.

    Args:
        val (Any): Input to the helper function

    Returns:
        int | None: returns a integer value if the input is a valid stringified number else None
    """
    parsed = _parse_float(val=val)
    if parsed is not None and not parsed.is_integer():
        logging.warning("%s would be truncated to integer", parsed)
    return int(parsed) if parsed is not None else None

def _clean_str(val: Any) -> str | None:
    """Helper function which checks if it's a valid string by cleaning and stripping it.

    Args:
        val (Any): Input to the helper function

    Returns:
        str | None: Returns the stripped string else None.
    """
    if val is None:
        return None
    if isinstance(val, str):
        s = val.strip()
        return s if s else None
    return None

def _initialize_result() -> dict[str, Any]:
    """Helper function to initialize the boilerplate of the result.

    Returns:
        dict[str, Any]: The result's default template.
    """
    return {
            "event_id": None,
            "timestamp": None,
            "service_name": "unknown",
            "service_version": "0.0.0",
            "region": "unknown",
            "cpu_pct": None,
            "memory_mb": None,
            "primary_tag": None,
        }


def flatten_telemetry_events(events: Iterable[dict[str, Any]]) -> Iterator[dict[str, Any]]:
    """This is a method to flatten nested JSON/Dictionary items.

    Args:
        events (Iterable[dict[str, Any]]): The list of nested JSON/Dictionary object.

    Yields:
        Iterator[dict[str, Any]]: The flattened iterable result produced by flattening the nested object.
    """

    for event in events:
        if not isinstance(event, dict):
            logging.warning('Skipping non-dictionary telemetry record of type %s', type(event).__name__)
            continue
        result = _initialize_result()
        result['event_id'] = _clean_str(event.get('event_id'))
        result['timestamp'] = _clean_str(event.get('timestamp'))

        service = event.get('service')
        if isinstance(service, dict):
            result['service_name'] = _clean_str(service.get('name')) or 'unknown'
            result['service_version'] = _clean_str(service.get('version')) or '0.0.0'
            result['region'] = _clean_str(service.get('region')) or 'unknown'

        metrics = event.get('metrics')
        if isinstance(metrics, dict):
            result['cpu_pct'] = _parse_float(metrics.get('cpu_pct'))
            result['memory_mb'] = _parse_int(metrics.get('memory_mb')) 

        tags = event.get('tags')
        if isinstance(tags, list) and tags:
            primary_tag = tags[0]
            result['primary_tag'] = _clean_str(primary_tag)
        yield result

if __name__=="__main__":

    results = flatten_telemetry_events(events=raw_events)
    for result in results:
        print(result)