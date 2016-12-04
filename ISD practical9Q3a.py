class CashRegister : # new class in the upper case
   # The __init__ method initializes the attributes 
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
   # The following methods are mutators for the class.
   def addItem(self, price) :
      #adds each item to the item count
      self._itemCount = self._itemCount + 1
      #adds the price to the total price
      self._totalPrice = self._totalPrice + price 
      
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
