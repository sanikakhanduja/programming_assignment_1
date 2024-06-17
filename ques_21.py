#Write a python program that counts the occurrences of a specific element in a list
n=int(input("please enter the number of elements.."))
l=[]
for i in range(n):
    ele=int(input("enter the value of element.."))
    l.append(ele)
ele=int(input("please enter the element for which we will count  the occurence..."))
print("the frequency of  the element is ",l.count(ele))
