str = "i am a coder, i love coding, i love python, i love programming, i love learning, i love challenges, i love solving problems, i love making a difference."

# Demonstrating various string functions in Python
#this string functions oprate using print. it's not change in actule string is a temperary

# this is basic string functions
print(str.endswith("love")) # False
print(str.startswith("i am")) # True
print(str.capitalize()) # the first letter capitalized
print(str.replace("love", "like")) # replace all occurrences of "love" with "like"
print(str.find("love")) # index of first occurrence of "a"
print(str.count("love")) # count occurrences of "love"
print(str.upper()) # convert to uppercase all
print(str.lower()) # convert to lowercase all
print(str.split(",")) # split by comma
print(str.title()) # convert to title case all words first letter capitalized

# this is more string functions

print(str.index("coder")) # index of first occurrence of "coder"
print(str.swapcase()) # swap case of all letters
print(str.strip()) # remove leading and trailing whitespace
print(str.isalpha()) # check if all characters are alphabetic
print(str.isdigit()) # check if all characters are digits
print(str.isalnum()) # check if all characters are alphanumeric
print(str.isspace()) # check if all characters are whitespace
print(str.center(100)) # center the string within a width of 100 characters
print(str.ljust(100)) # left-justify the string within a width of 100 characters
print(str.rjust(100)) # right-justify the string within a width of 100 characters
print(str.zfill(120)) # pad the string with zeros on the left to a total width of 120 characters
print(str.partition("coding")) # partition the string at the first occurrence of "coding"
print(str.rpartition("love")) # partition the string at the last occurrence of "love"
print(str.splitlines()) # split the string at line breaks
print(str.encode()) # encode the string to bytes using default encoding (utf-8)
print(str.expandtabs(tabsize=4)) # expand tabs to spaces with a tab size of 4
print(str.format()) # format the string (no placeholders in this case)
print(str.format_map({})) # format the string using a mapping (no placeholders in this case)
print(str.islower()) # check if all characters are lowercase
print(str.isupper()) # check if all characters are uppercase
print(str.removeprefix("i am a ")) # remove the prefix "i am a " if it exists
print(str.removesuffix(".")) # remove the suffix "." if it exists
print(str.translate(str.maketrans("love", "like"))) # translate characters using a translation table
print(str.casefold()) # casefold the string for caseless matching
print(str.isidentifier()) # check if the string is a valid identifier




#modifying the original string
# this string is change acctule string
str = str.replace("love", "like")
print(str)
print(str.title())