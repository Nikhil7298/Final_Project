from Restaurant import Admin
class Functions:
    fooditems=[]
    def ADDFOOD(self):
        foodid=int(input('enter the foodid : '))
        name=input('enter the food name : ')
        quantity = input('enter the quantity :')
        discount=input('enter the discount : ')
        price=int(input('enter the price : '))
        stock=input('enter the stock : ')
        obj=Admin(foodid,name,quantity,discount,price,stock)
        self.fooditems.append(obj)
        print('food item added !!!!!')
        
    def view(self):
        for item in self.fooditems:
            print(f"foodid: {item.foodid}\nName: {item.name}\nQuantity: {item.quantity}\nDisocunt: {item.discount}\nPrice: {item.price}\nStock: {item.stock}\n")
            
    def Update(self):
        foodid=int(input('enter the foodid :'))
        for Restaurant in self.fooditems:
            
            if foodid==Restaurant.get_foodid():
            
                name=input('enter the food name : ')
                quantity = input('enter the quantity :')
                discount=input('enter the discount : ')
                price=int(input('enter the price : '))
                stock=input('enter the stock : ')
                
                Restaurant.set_name(name)
                Restaurant.set_quantity(quantity)
                Restaurant.set_discount(discount)
                Restaurant.set_price(price)
                Restaurant.set_stock(stock)
            
            print('succussfully updated !!!!')
            
        
        
    