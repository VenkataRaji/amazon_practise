"""Magic methods are the methods which start and end with __ and mostly they are called inplicitly.

dir() is the in built function to know the magic methods of the given class or obejct type can perform

There is no need to call these methods by the user,it is a choice"""

"""for eg

for int object, __add__ is the magic method to add the numbers
wherever the intrepreter find the + symbol,it automatically calls the __add__ magic method
"""

a=20

# here I explicitly called the __add__ magic method,which is now adding 10 to value 20 
# op is 30
print(a.__add__(10))

# op is 50
# because __add__ magic method is called twice---coz there is a + symbol along with explicit invoking. 
print(a+a.__add__(10))
