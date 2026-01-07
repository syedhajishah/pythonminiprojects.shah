# there are three types to store string 
print("i\tstring printing types\n")
frist = 'hello "syed haji shah " wellcome' #  in sentence using dubble code. cover string with ' " ' apostrofe 
name = " it's syed haji shah" # most using " ' " 
subjects = ''' it's "syed haji shah" and 
i am pursing in 2nd year degree''' #trible code mens asitise next line print, mulity line print  
print(frist)
print(name)
print(subjects)

# escape sequence charecter
print("\nii\texamples of escape sequence charecter")
print("\nhello \n dear \t syed haji shah") # \n new line \t tab space

# string length functions
print("\niii\tchecking string length")
print(len(subjects))
length = len(subjects) # len() function use to find length of string
print(length)

# basic operation
#1 concatenation on string  ( + operator)
print("\niv\tstring oprations")
x , y = "haji " , "shah"
print(x+y) # concatenation of string
z  = "haji" + "shah"
print(z)
a = input("Enter first name : ")
b = input("Enter middle name : ")
c = input("Enter last name : ")
print("Full name is : " , a + " " + b + " " + c)
# or
full_name = a + " " + b + " " + c
print(full_name)

#2 repetition of string ( * operator)
str1 = "syed "
str2 =  str1 * 3
print(str2)
# or
str3 = "haji " * 5
print(str3)     

#3 membership operator (in and not in)
str4 = "The quick brown fox"
checkIn = "fox" in str4
print("in" , str(checkIn))

check_notIn = "dog" not in str4

print("not in" , check_notIn)

#4 Comparison Operators (==, !=, <, >, <=, >=)
str5 = "apple" # lowercase 'a' value 97
str6 = "Apple" # uppercase 'A' value 65
print(str5 == str6)  # False
print(str5 != str6)  # True
print(str5 < str6)   # False
print(str5 > str6)   # True
print(str5 <= str6)  # False
print(str5 >= str6)  # True

#5 Formatting (Implicit Operators/Syntax)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
formatted_str = f"My name is {name} and I am {age} years old." #f-string formatting
print(formatted_str)    

# Indexing
print("\nv\tindexing ")
index = "syed haji shah"
print(index[3], index[8], index[13])  # d, i, h
ch = index[0] + index[5] + index[10]  # s, h, s
print(ch)