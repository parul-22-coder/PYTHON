# string is collection of character inside double or single qoute
name ="pArul"
# string indexing
print(name[1])
print(name[-1])
# string slicing
print(name[0:3:1])
print(name[-1:0:-1])                       #[start arg : stop arg:step arg]
print(name[0:-2])
print(name[0:])                            #if their is no arg it will end with last character
# user input
age = input("enter your age :")            # input fun9ction always takes input in strings 
age = int(input("enter your class"))       #we can change input from dtring to number by usint int method
print(age)
user_name, age = input("enter your name and age :").split(",")
print(user_name)
print(age)
# len function
print(len(name))
print(name.lower())                          # it convert whole string in lower case letters
print(name.upper())                          # it converts whole string in upper case letters
print(name.title())                          # it converts first letter in upper case and rest in lower case
print(name.find("r"))
print(name.find("r",3))
r_pos = name.find("r")
r_pos_2 = name.find("r",r_pos + 1)           #we9 can find the positio of 2nd r by using variables
print(name.center(11,"*"))
# string are immutable
                                                 #  we can not change string.
print(name.replace("l","L","1"))                                                 