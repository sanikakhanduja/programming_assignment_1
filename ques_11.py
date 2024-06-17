#Write a python program that generates the first n numbers in the Fibonacci sequence
first=1
second=1
n=int(input("please enter the range.."))
print("the first n numbers of fibonacci sequence is as follows")
print(first)
print(second)
for i in range(2,n):
    sum=first+second
    print(sum)
    first=second
    second=sum

