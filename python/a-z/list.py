names = ['A','B','C','D','E']

print(names)
print(names[1:])


# find the largest number in the list
max = 0
numbers = [1,2,3,4,5,6,7]
for num in numbers:
    if(num > max):
        max = num
print(max)


coordinates = [21,32,45]
#we can assign it's index to the variable
# internally it is happing 
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z = coordinates

print(f"value of {x} , {y} , {z}")