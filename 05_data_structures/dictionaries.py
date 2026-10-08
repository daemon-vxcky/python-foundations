def valid_marks(marks: int) -> bool:
    """Checks if the marks are valid and returns True if it's between 0 and 100."""
    if marks<0 or marks>100:
        return False
    return True

def print_student_grade(total: int) -> str:
    """Prints the student grade from the total marks scored by the student."""
    if total>=250:
        print(f'Student has done a terrific job, he deserves an S or O!!!')
        return 'O'
    elif total>=200:
        print(f'Student has done a good job, definitely an A or at the very least an A-')
        return 'A'
    elif total>=150:
        print(f'Student can do better, B')
        return 'B'
    else:
        print(f'Student has got some work to do, a generous D')
        return 'D'

def process_student() -> int:
    """Requests students details from the user and computes students total marks and grade."""
    student_name = input('Enter Student name: ')
    student_names.append(student_name)
    chemistry_marks = int(input('Enter marks scored by student in chemistry: '))
    physics_marks = int(input('Enter marks scored by student in physics: '))
    math_marks = int(input('Enter marks scored by student in math: '))

    while not valid_marks(chemistry_marks):
        print('Invalid, Try again')
        chemistry_marks = int(input('Enter Chemistry Marks between 0-100: '))
    
    while not valid_marks(physics_marks):
        print('Invalid, Try again')
        physics_marks = int(input('Enter Physics Marks between 0-100: '))
    
    while not valid_marks(math_marks):
        print('Invalid, Try again')
        math_marks = int(input('Enter Math Marks between 0-100: '))
    
    return chemistry_marks + physics_marks + math_marks

n = int(input('Enter no of students whose marks you would like to enter:'))

while n<=0:
    print("Enter Only Positive values for n!!!!!!")
    n = int(input('Enter no of students whose marks you would like to enter:'))

student_total_marks = []
student_names = []

for i in range(n):
    student_total_marks.append(process_student())
student_data = dict()
student_datas = []
for i in range(n):
    student_grade = print_student_grade(student_total_marks[i])
    student_data['name'] = student_names[i]
    student_data['marks'] = student_total_marks[i]
    student_data['grade'] = student_grade
    student_datas.append(student_data)
    student_data = dict()

for stud_data in student_datas:
    print(stud_data)