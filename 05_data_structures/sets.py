student_a = set(list(map(input("Enter the courses completed by student A separated by spaces: ").split())))
student_b = set(list(map(input("Enter the courses completed by student B separated by spaces: ").split())))

a_union_b = student_a.union(student_b)
a_intersection_b = student_a.intersection(student_b)
set_difference_between_a_and_b = student_a.difference(student_b)
set_difference_between_b_and_a = student_b.difference(student_a)
symmetric_difference = student_a.symmetric_difference(student_b)

print(f'The courses completed by both A and B are: {a_intersection_b}')
print(f'The courses which student A only completed is: {set_difference_between_a_and_b}')
print(f'The courses which student B only completed is: {set_difference_between_b_and_a}')
print(f'All unique courses completed: {a_union_b}')