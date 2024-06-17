#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
choice=input("please enter C for celcius and F for fahrenheit")
if(choice.upper()=='C'):
    tempc=int(input("Please enter the temperature in celcius"))
    tempf=(tempc*(9/5))+32
    print("the temp in farenheit is ",tempf)
else:
    tempf=int(input("Please enter the temperature in farenheit"))
    tempc=(tempf*(5/9))-32
    print("the temp in celcius is ",tempc)
