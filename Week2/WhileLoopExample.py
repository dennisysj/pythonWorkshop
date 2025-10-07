#this while loop is useful if you need a condition to be satisfied
response = ""

while response != "yes":
    response = input("Type 'yes' to continue: ")
    if(response != "yes"):
        print("that was not a yes")
    
print("Thank you!")

