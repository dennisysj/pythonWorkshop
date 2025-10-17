#take the user input
num = int(input("Enter a number: "))

#define the function to print out the userInput
def printNum():
    print(num)

def check_number():
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function and show the result
result = check_number()
print(printNum()," is", result)
