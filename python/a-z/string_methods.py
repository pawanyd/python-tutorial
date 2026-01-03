description = "my name is pawan kumar and i am beginner"

# len() is function that return the string length 

print(len(description))

# we have differenct methods that we can perform on the sting 

# upper() method will convert the value into the upper case 
# but it not changes into the original string 

print(description.upper())

print(description.lower())

# we can find the character into the sting 

# it return the index of that perticualar character
# count strart with 0
# if we find the sting that not exits then it return -1

print(description.find("p"))


# if we put the word insted of the char then it return the strating index 
print(description.find("pawan"))



# replace() method it will get two param find and replace 
# it is case sencitive

print(description.replace('beginner', 'advanced'))


# check perticualar word or sting is existing in the sting 

# it return True or False value

print('pawans' in description)


# title() method
# it make the sting as title you can say that it make first character of sting make upper 
print(description.title())


# split() it convert into the array behalf of the seperator

print(description.split(" "))
