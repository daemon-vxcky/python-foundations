import logging
from pathlib import Path
from collections import Counter


def parse_status_counts(filepath: str | Path) -> dict[int, int]:
    """This is a method to extract the counts of status codes present in a sample log file

    Args:
        filepath (str | Path): The path to the log file.

    Returns:
        dict[int, int]: The dictionary output which has the status_code and the number of times that code appeared in the file.
    """
    try:
        with open(file=filepath, encoding='utf-8') as sample_log_file:
            status_code_dict = Counter()
            malformed_lines = 0
            for line_num, line in enumerate(sample_log_file, start=1):
                line_copy = line.strip()
                if not line_copy:
                    continue
                line_split = line_copy.split(' | ')
                for data_element in line_split:
                    if data_element.startswith('status='):
                        try:
                            _,status_code = data_element.split('=', maxsplit=1)
                            status_code = int(status_code)
                            status_code_dict[status_code]+=1
                            break
                        except ValueError as e:
                            logging.warning(f'Error Occured: {e} at line number {line_num}')
                else:
                    malformed_lines+=1

            logging.info(f'Number of malformed lines in the file: {malformed_lines}')
            return dict(status_code_dict)
    except (OSError) as e:
        logging.error(f'Error occured in parse_status_counts method, error: {e}')
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    file_path = '08_file_io_collections/sample.log'
    status_code_dict = parse_status_counts(filepath=file_path)
    for status_code, appearances in status_code_dict.items():
        print(f'{status_code} appeared {appearances} times in the file')