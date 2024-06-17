#Write a python program that checks if two strings are anagrams of each other
str1=input("please enter the string1..")
str2=input("please enter the string2..")
if(sorted(str1)==sorted(str2)):
    print("the strings are anagrams")
else:
    print("the strings are not anagrams ")