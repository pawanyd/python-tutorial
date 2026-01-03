# define string in single cots 

about = 'this is pawan "house"'

print(about)

# define in double cots 

about_pawan = "this is pawan 'House'"

print(about_pawan)

# to maintain multiline string we use three single cots

sendMail = '''

Hi Pawan,

I hope you are fine.

Thanks 
Team
'''

print(sendMail)

# if we want to get the first character then we can get it via useing index

name = "pawan";

print(name[0])

# output will be - p

# if we want to get last element of the string then we use the index in negitive

print(name[-1])

# output will be n

# if we want to get the perticular portion of sting then we can get like this 
# when we pass two point string and end point to get the sting then it excluse the last element 
# it string counting form zero. 0

print(name[0:2])

# output will be pa

# we can also pass only first and only last element number to get the string 

print(name[0:])

# it will give the full sting because we string from the zero 
print(name[1:])

# output will be awan because it remove first character from the string 


#we can pass only end key for get the sting in last
# by default it consider 0 to the starting 

print(name[:2])

# output will be pa



# copy or full sting
name_copy = name[:]

print(name_copy)


# we can pass the negitive value 

print(name[1:-1])

# output will be awa it remvoe first and last element 


print(name[-1:1])


