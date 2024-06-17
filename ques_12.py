#Write a python program that calculates the sum of the digits of a given number.
n=int(input("please enter the number.."))
sum=0
while(n!=0):
    digit=int(n%10)
    sum+=digit
    n=n/10
print("sum of digits of the number is ",sum)
