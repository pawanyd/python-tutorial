# to define tuples we use paranthisis
# we can not modify this not add and not remove any element
# if we try to modify this then it throw the error
numbers = (1,2,3)

print(len(numbers))

print(numbers[0])


# tuples unpacking 

coordinates = (21,32,45)
#we can assign it's index to the variable
# internally it is happing 
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z = coordinates

print(f"value of {x} , {y} , {z}")