#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
str=input("please enter the string you want to check...")
suffix=input("please enter the suffix...")
prefix=input("please enter the prefix...")
if(prefix in str):
    print("prefix is present in the string")
elif(suffix in str):
    print("suffix is present in the string")
else:
    print("neither suffix or prefix present")