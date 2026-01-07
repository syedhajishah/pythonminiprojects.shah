# Different Data Types in Python

name = "Syed haji shah " # ✔ str → string data type


marks = 7.2 #float -> decimal number


age = 83 #int -> integer whole number

print("age typr is ", type(age)) # printing data type using type() function

print(int(age)) # converting age to integer using int() function 

learnPy = True #✔ boolean data type return true or false


emty = None #✔ NoneType → empty value complex data type

#Sequence Types
my_list = [1,2,3] #✔ list
my_tuple = (1,2,3) #✔ tuple
my_range = range(5) #✔ range

#Mapping Type 
my_dict = {"name":"Syed", "age":20} #✔ Key-value format ✔ Only 1 type → dict

#Set Types
my_set = {1,2,3} #✔ Unique values store karta hai ✔ unordered hota hai ✔ 2 types → set, frozenset


a = 20 # ✔ int → integer
b = 20.20 # ✔ float → decimal
z = 2+3j # ✔ complex → complex numbers
sum = (a+b*b/a) # calculation operators - + / *
print(sum) # printing

shah = input("Enter Your Name : ")
print(shah)