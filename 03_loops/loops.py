n = int(input('Enter no of students whose marks you would like to enter:'))

for i in range(n):
    chemistry_marks = int(input('Enter marks scored by student in chemistry: '))
    physics_marks = int(input('Enter marks scored by student in physics: '))
    math_marks = int(input('Enter marks scored by student in math: '))

    while chemistry_marks<0 or chemistry_marks>100:
        print('Invalid, Try again')
        chemistry_marks = int(input('Enter Chemistry Marks between 0-100: '))

    while physics_marks<0 or physics_marks>100:
        print('Invalid, Try again')
        physics_marks = int(input('Enter Physics Marks between 0-100: '))

    while math_marks<0 or math_marks>100:
        print('Invalid, Try again')
        math_marks = int(input('Enter Math Marks between 0-100: '))

    total = chemistry_marks + physics_marks + math_marks
    if total>=250:
        print(f'Student {i+1} has done a terrific job, he deserves an S or O!!!')
    elif total>=200:
        print(f'Student {i+1} has done a good job, definitely an A or at the very least an A-')
    elif total>=150:
        print(f'Student {i+1} can do better, B')
    else:
        print(f'Student {i+1} has got some work to do, a generous D')
