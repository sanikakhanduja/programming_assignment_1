#Write a python program that calculates the factorial of a given number
a=int(input("please enter the number..."))
fact=1
for i in range(1,a+1):
    fact*=i;
print("the factorial is ",fact)
