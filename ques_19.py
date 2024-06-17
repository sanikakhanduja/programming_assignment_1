#Write a python program that removes all punctuation from a given string

strinp = input("Please enter the string with punctuation: ")
result_str = ''
for char in strinp:
    if char not in [',', '.', ';', "'", '-']:
        result_str += char
print("The string without punctuation is:", result_str)


