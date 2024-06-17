#Write a program that asks the user for their birth year and calculates their age.
byear=int(input("please enter your birth year "))
if(byear<=2000):
    age=abs(2000-byear)+24
else:
    age=2024-byear
print("Your age is ",age)