#Write a python program that returns the minimum and maximum values in a list of numbers
n=int(input("please enter the number of elements.."))
l=[]
for i in range(n):
    ele=int(input("enter the value of element.."))
    l.append(ele)
print("the maximum element is ",max(l))
print("the minimum element is ",min(l))
