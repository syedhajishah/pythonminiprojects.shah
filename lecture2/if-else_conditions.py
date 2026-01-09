# Traffic light condition check

# light = input("Enter traffic light color\t:\t")

# if(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("ready to stop")
# elif(light == "red"):
#     print("stop")
# else:
#     print("signel is broken. Not working")

# Grate condition check

# grate = float(input("Enter your grate\t:\t"))

# if(0 <= grate and 100 >= grate):
#     if(grate > 90 and grate <= 100):
#         print("'A' grate")
#     elif(grate >= 70 and grate <= 90):
#         print("'B' grate")
#     elif(grate >= 40 and grate < 70):
#         print("'C' grate")
#     elif(grate >= 28 and grate <= 40):
#         print("'D' grate")
#     else:
#         print("Fail")
# else:
#     print("Invalid grate")
 
#or

# Best and Most Reliable Version
grade = float(input("Enter your grade: "))

if 0 <= grade <= 100:
    if grade > 90:
        print("'A' grade")
    elif grade >= 70:
        print("'B' grade")
    elif grade >= 40:
        print("'C' grade")
    elif grade >= 28:
        print("'D' grade")
    else:
        print("Fail")
else:
    print("Invalid Input! Please enter a value between 0 and 100.")