class Restaurant:
  def __init__(self, foodid, name, quantity, discount, price, stock):
    self.foodid = foodid
    self.name = name
    self.quantity = quantity
    self.discount = discount
    self.price = price
    self.stock = stock
  
  def set_foodid(self, foodid):
    self.foodid = foodid
  
  def get_foodid(self):
    return self.foodid
   
  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    return self.name
  
  def set_quantity(self, quantity):
    self.quantity = quantity
  
  def get_quantity(self):
    return self.quantity

  def set_discount(self,discount):
    self.discount = discount
  
  def get_discount(self):
    return self.discount
  
  
  def set_price(self, price):
    self.price = price
  
  def get_price(self):
    return self.price
  
  def set_stock(self, stock):
    self.stock = stock
  
  def get_stock(self):
    return self.stock
  
  def _str_(self):
    return(f'foodid: {self.foodid}\nquantity: {self.quantity}\nname: {self.name}\nprice: {self.price}\ndiscount: {self.discount}\nstock: {self.stock}\n')