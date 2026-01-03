# import the entire module
import converters
import ecommerce.shipping as myname
# import only perticular funciton
from converters import kg_to_lbs

# module is basically use to orgnaize the file and function in a better manner


# there are alrady different predefind modules 
# find then on google
# type python 3 module index

print(kg_to_lbs(30))

print(converters.kg_to_lbs(10)) 

print(myname.ship())
