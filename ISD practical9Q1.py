class Person():
    def __init__(self, firstName):
        self._name = firstName

    def printName(self):
        print(self._name)

person1=Person("Harry")
person1.printName()
