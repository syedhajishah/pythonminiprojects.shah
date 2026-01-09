# Q1 write a program to input first name and print its length ?
full_name = input("Enter Full Name : ")
print(len(full_name))

# Q2 write a program to input a string and print its first and last character ?
str = input("Enter a string : ")   
print(str[0], str[-1])

# Q3 write a program to input a string and print its reverse ?
str1 = input("Enter a string : ") 
print(str[::-1])

# Q4 write a program to input a string and check if '$' is present in the string or not. if present print its index ?
str2 = "syed haji shah $ 123"
print(str2.find("$")) # index of first occurrence of "$"

# Q5 write a program to input a string and replace all occurrences of 'a' with '@' ?
str3 = "syed haji shah $ 123"
print(str3.replace("a","@"))

#  Q6 write a program to input a string and print it in uppercase ?
str4 = input("Enter a string : ")
print(str4.upper())

# Q7 write a program to input a string and check if it is alphanumeric or not ?
str5 = input("Enter a string : ")
print(str5.isalnum())

# Q8 write a program to input a string and print it in title case ?
str6 = input("Enter a string : ")
print(str6.title())
# Q9 write a program to input a string and count number of times 'e' is present in the string ?
str7 = input("Enter a string : ")
print(str7.count("e"))  
# Q10 write a program to input a string and check if it starts with 'Hello' or not ?
str8 = input("Enter a string : ")
print(str8.startswith("Hello"))
# Q11 write a program to input a string and check if it ends with 'Python' or not ?
str9 = input("Enter a string : ")
print(str9.endswith("Python"))
# Q12 write a program to input a string and split it into a list of words ?
str10 = input("Enter a string : ")
print(str10.split())