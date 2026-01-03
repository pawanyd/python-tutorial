#2d list in the python

# 1 2 3
# 4 5 6
# 7 8 9

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# we can access this like 

print(matrix[0])

print(matrix[0][1])

for item in matrix:
    for num in item:
        print(num)


# list methonds 

numbers = [1,2,3,4,5]

# append 
numbers.append(10)
print(numbers)

# it append the number in the last

# insert funciton 
# two param first is index and value
numbers.insert(0, 20)

print(numbers)


# remove method the element
numbers.remove(20)

print(numbers)

# clear() method remove all elements
# numbers.clear()
# print(numbers)

#pop() menthod remove last element
numbers.pop()
print(numbers)


# index method => return the index 
# if we check that element not exist then it threow the error
print(numbers.index(4))


# return true or false 
print(50 in numbers)


# count the number that is presend in the list
# if not exits then it return 0
print(numbers.count(40))


# sort method 
numbers.sort()
print(numbers)

# sort in reverse
numbers.reverse()
print(numbers)


# copy method just copy the main
numbers2 = numbers.copy()

print(numbers)
print(numbers2)


# excercise remvoe duplicate from the list

mydata = [1,2,3,2,4,5,5,6]

for item in mydata:
    if(mydata.count(item) > 1):
        mydata.remove(item)

print(mydata)



# by condition 
numberslist = [1,2,3,3,4,4,5,6,6]
unique = []

for number in numberslist:
    if number not in unique:
        unique.append(number)

print(unique)

