#Write a program that takes a string input from the user and writes it to a text file
text=input("please enter the message ")
samplefile=open("C:/Users/sanika khanduja/OneDrive/Documents/demo.txt",'w')
print(text,file=samplefile)