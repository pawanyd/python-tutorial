customer = {
    "name" : "Pawan",
    "age" : 30,
    "mobile": 784343433
}

print(customer["name"])

# we can also access by the methods
print(customer.get("name"))

# get and return default if key not exist then it return yadav
print(customer.get("name","yadav"))

customer["hello"] = "value of hello"

# we can overide the key and add the new value