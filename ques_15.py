#Write a program that reads data from a CSV file and prints it to the console
import csv
with open('newfilecsv.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["id ","name","marks"])
    writer.writerow([101,"reema",89])
    writer.writerow([102,"seema",78])
    writer.writerow([103,"meena",66])
    writer.writerow([104,"tina",56])
    print("records added succesfully !!")

with open('newfilecsv.csv','r',newline='') as file2:
    reader=csv.reader(file2)
    for i in reader:
        print(i)
    