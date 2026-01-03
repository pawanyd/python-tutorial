try:
    age = int(input("enter your age > "))
    print(age)
except ValueError:
    print(f"Please enter a valid input you enter age")
#we can handle multipal exceptions 