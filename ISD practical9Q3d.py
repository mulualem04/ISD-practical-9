class CashRegister : # new class in the upper case
   # The __init__ method initializes the attributes 
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._change = 0
   # The following methods are mutators for the class.
   def addItem(self, price) :
      #adds each item to the item count
      self._itemCount = self._itemCount + 1
      #adds the price to the total price
      self._totalPrice = self._totalPrice + price

   def giveChange(self, price) :
       self._itemCount = self._itemCount + 1
       # adds the price to the total price without pence
       self._totalPrice = self._totalPrice + price
       self._change = self._payment - self._totalPrice
       return self._change
   # The following method are accessors for the class.
   def getTotal(self) :
      return self._totalPrice
      
   # The following method are accessors for the class.
   def getCount(self) :
      return self._itemCount

   # Clears out both the itemcount and total price in the cash register class 
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

register1 = CashRegister() # This would create first object(register1) 
register1.giveChange(0.90)
register1.giveChange(0.95)
register2 = CashRegister() # This would create second object(register2) 
register2.giveChange(1.90) 

print(register1._itemCount) # returns itemCount
print(register1._totalPrice) # returns totalPrice
print(register2._itemCount)
print(register2._totalPrice)
