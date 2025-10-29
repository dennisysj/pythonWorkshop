import random
student = {}

#press control c to end the program
while 1==1:
    randNum = random.randint(0,100)
    name = input("Add Student: ")
    student[name] = randNum
    print(student)
