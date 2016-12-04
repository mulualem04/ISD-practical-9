class Person(): # create Person class
    # The __init__ method initializes attributes  
    # To construct object
    def __init__(self,name="unknown"):
        self._name = name
    # accessing instance variable
    def printName(self):
        print(self._name)

person1=Person("unknown") # object creation
person1.printName() # Call class method
