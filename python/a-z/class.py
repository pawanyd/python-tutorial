class Point:

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def show(self):
        return "This is show funciton"
        #print("This is show function")

    def view(self):
        return "This is viw funciton"
    

# create instansce 
point1 = Point(x=10,y=20)
point2 = Point(10,30)

#overide the x value
point1.x = 50

print(point1.x)

print(point2.view())


# below the example of the inheritance
class Mammal:

    def walk(self):
        print("walk")

class Dog(Mammal):
    pass
    # python not like empty class so we put pass

class Cat(Mammal):
    pass


dog1 = Dog()

dog1.walk()



