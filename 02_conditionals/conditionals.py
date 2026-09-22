chemistry_marks = int(input('Enter marks scored by student in chemistry: '))
physics_marks = int(input('Enter marks scored by student in physics: '))
math_marks = int(input('Enter marks scored by student in math: '))

chemistry_retries = 0
physics_retries = 0
math_retries = 0

if chemistry_marks<0 or chemistry_marks>100:
    chemistry_marks = int(input('Enter Chemistry Marks between 0-100: '))
    chemistry_retries+=1

if physics_marks<0 or physics_marks>100:
    physics_marks = int(input('Enter Physics Marks between 0-100: '))
    physics_retries+=1

if math_marks<0 or math_marks>100:
    math_marks = int(input('Enter Math Marks between 0-100: '))
    math_retries+=1

if (chemistry_marks<0 or chemistry_marks>100) and chemistry_retries<2:
    chemistry_marks = int(input('Enter Chemistry Marks between 0-100: '))
    chemistry_retries+=1

if (physics_marks<0 or physics_marks>100) and physics_retries<2:
    physics_marks = int(input('Enter Physics Marks between 0-100: '))
    physics_retries+=1

if (math_marks<0 or math_marks>100) and math_retries<2:
    math_marks = int(input('Enter Math Marks between 0-100: '))
    math_retries+=1

if (chemistry_marks>=0 and chemistry_marks<=100) and (physics_marks>=0 and physics_marks<=100) and (math_marks>=0 and math_marks<=100):
    total = chemistry_marks + physics_marks + math_marks

    if total>=250:
        print('Student has done a terrific job, he deserves an S or O!!!')
    elif total>=200:
        print('Student has done a good job, definitely an A or at the very least an A-')
    elif total>=150:
        print('Student can do better, B')
    else:
        print('Student has got some work to do, a generous D')

else:
    print('Enter marks only in the range of 0-100 after rerunning the program!')