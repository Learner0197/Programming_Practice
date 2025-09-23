from DessertProblem.Desserts import IceCream, Candy, Cookie, Sundae


class Checkout:
    def __init__(self):
        self.totalitems=0
        self.totalbill=0
        self.cart=[]


    def addtocart(self,dessert):
        if dessert not in self.cart:
            self.cart.append(dessert)
            self.totalitems+=1
            self.totalbill=self.totalbill+dessert.calculateamount()

    def clearcashregister(self):
        self.cart.clear()
        self.totalbill=0
        self.totalitems=0

    def gettotalcost(self):
        return self.totalbill

    def gettotalitems(self):
        return self.totalitems


    def __str__(self):
        if not self.cart:
            return "Cart is empty"

        result = str()

        for item in self.cart:
            result += f"{item.getname()} {item.__class__()}\n"
        result += f"\nTotal items: {self.totalitems}"
        result += f"\nTotal bill: Rs. {self.totalbill}"
        return result


a=IceCream("Chocolate",2)
b=Candy("Chocolate",250)
c=Cookie("Butter",6)
d=Sundae("Vanilla",3)

checkout=Checkout()
checkout.addtocart(a)
checkout.addtocart(b)
checkout.clearcashregister()
checkout.addtocart(c)
checkout.addtocart(d)



print("\n" + str(checkout))