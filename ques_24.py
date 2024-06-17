#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
a =int(input("Please enter the first number "))
b=int(input("Please enter the second number "))
choice=input("please enter the operators + - * / ")
if(choice=='+'):
    print("the sum is :",a+b)
elif(choice=='-'):
    print("the difference is :",a-b)
elif(choice=='*'):
    print("the product is :",a*b)
else:
    print("the remainder is :",a/b)
