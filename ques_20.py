#Write a python program that takes a list of numbers and returns their sum
n=int(input("please enter the number of elements.."))
l=[]
for i in range(n):
    ele=int(input("enter the value of element.."))
    l.append(ele)
print("the sum of the elements are..",sum(l))
