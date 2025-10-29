import random
student = {}

#press control c to end the program
while 1==1:
    sNum = random.randint(1000,9000)
    ageNum = random.randint(18,100)
    name = input("Add Student: ")
    student[name] = {
        "studentID" : sNum,
        "age": ageNum
    }
    print(student)
    print(student[name]["age"])
    print(student[name]["studentID"])
