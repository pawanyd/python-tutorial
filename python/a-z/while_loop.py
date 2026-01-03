i = 1

while i <= 5:
    print("*" * i)
    i += 1

print("Done")


# another while loop with else

secrate_number = 3
secrate_count = 0
limit = 3


while secrate_count < limit:
    guss = int(input("Please enter guss number? "))
    secrate_count += 1
    if guss == secrate_number:
        print("you won!")
        break
else:
    print("you loose")