#Make a calculator for 2 variables
# "*" is multiply and "/" is divide so 2*2 = 4, 10/5 = 2.
#also this is a comment btw, it won't affect your code.
userInput = input("What would you like to do? \n Choose one option: + - / * :")
num1 = 1
num2 = 2

#addition condition block
if(userInput == "+"):
    print(num1 + num2)

#subtraction condition block
elif(userInput =="-"): #remember elif stands for else if
    print(num1-num2)

#division condition block
elif(userInput =="/"):
    print(num1/num2)

#multiplication
elif(userInput=="*"):
    print(num1*num2)