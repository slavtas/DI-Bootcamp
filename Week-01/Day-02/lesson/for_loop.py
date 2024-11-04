students = ['Alex','Noah','Sara','Dima']

for each_student in students:
    if each_student == 'Dima':
        print(f'Dobroe Utro, {each_student}')
        
    else:
        print(f'Good Morning, {each_student}')

for i in range(1,10):
    print(f'Hi, there {i}')

for i in range(len(students)):
    print(f'Hello there {i}')

for i, each_student in enumerate(students):
    print(i, each_student)
