#Write a program that copies the contents of one text file to another
file1=open("C:/Users/sanika khanduja/OneDrive/Documents/demo.txt",'r')
content=file1.read()
file2=open("C:/Users/sanika khanduja/OneDrive/Documents/demo2.txt",'w')
file2.write(content)
print("copied successfully")