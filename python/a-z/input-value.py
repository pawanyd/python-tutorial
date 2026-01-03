# input() - we can get value form the terminal by the help of input function.
# int() - type casting from string to int
# string() - string type casting 
# type() - this funciton will tell which type of the variable - int , string , float 
# float() - type casting of flote data type 
# Note:- when we get any value from the input we always get the string value so need to cast that 


name = input("what is your name? ")

print(type(name))

color = input("what is your favorite color? ")

weightInPound = input("how much your body weight in pound? ")

weightInKg = (int(weightInPound) * 0.45)

print('Hi my name is', name, "And my favorite color is", color, "and my weight in kg ", weightInKg)