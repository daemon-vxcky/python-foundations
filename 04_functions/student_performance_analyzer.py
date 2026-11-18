def valid_marks(marks: int) -> bool:
    """Checks if the marks are valid and returns True if it's between 0 and 100."""
    if marks<0 or marks>100:
        return False
    return True

def print_student_grade(total: int) -> None:
    """Prints the student grade from the total marks scored by the student."""
    if total>=250:
        print(f'Student has done a terrific job, he deserves an S or O!!!')
    elif total>=200:
        print(f'Student has done a good job, definitely an A or at the very least an A-')
    elif total>=150:
        print(f'Student can do better, B')
    else:
        print(f'Student has got some work to do, a generous D')

def process_student() -> None:
    """Requests students details from the user and computes students total marks and grade."""
    student_name = input('Enter Student name: ')
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
    
    total = chemistry_marks + physics_marks + math_marks

    print_student_grade(total)

n = int(input('Enter no of students whose marks you would like to enter:'))

while n<=0:
    print("Enter Only Positive values for n!!!!!!")
    n = int(input('Enter no of students whose marks you would like to enter:'))

for i in range(n):
    process_student()
