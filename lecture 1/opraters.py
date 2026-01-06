a = 20
b = 10 

print("arithmetic oprater")

print("+" ,(a + b)) # pluse, addition operater 
print("-" ,(a - b)) # minus, supraction operater
print("*" ,(a * b)) # star, multiplecation  operater 
print("/" ,(a / b)) # oblic/slash, divition operater 
print("%" ,(a % b)) # modulo/persentage, this operater given remain value

print("relational / comparition oprater")

print(a != b) #not equal to 
print(a == b) # equal to 
print(a < b) # less than 
print(a > b) # greter than 
print(a <= b) # less than equal to
print(a >= b) # greter than equal to

print("assinment oprater")

num = 5
num += 10  # num = num + 10
num -= 10  # num = num - 10
num *= 10  # num = num * 10
num /= 10  # num = num / 10
num %= 10  # num = num % 10
num ** 10  # num = num ** 10 power 
print( num )

print("logical oprater")

# not oprater
print(not(a > b)) #false because given opposite value 
print (not(a < b)) #true same as frist one 

# and oprater

print(a > b and a < b) #one value is true another value is false given is false 
print(a > b and b < a) #two value is true given is true
print(a < b and a == b) #two value is false given is false 

# or oprater

print(a > b or b < a) #two value is true given is true
print(a > b or a < b) #one value is true another value is false given is true
print(a < b or a == b) #two value is false given is false 