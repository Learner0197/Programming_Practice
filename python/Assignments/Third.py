from abc import ABC,abstractmethod

class CartIsEmptyException(Exception):
    def __init__(self):
        super().__init__("Cart is empty")

class AmountInvalidException(Exception):
    def __init__(self):
        super().__init__("Amount is invalid")

class DessertItem(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def calculateamount(self):
        pass

    def getname(self):
        return self.name



class Candy(DessertItem):
    def __init__(self, name,quantity):
        super().__init__(name)
        self.quantity=quantity
        self.priceperkg = 50

    def calculateamount(self):
        totalprice=self.quantity * self.priceperkg //1000
        return totalprice
    def __class__(self):
        return "Candy"


class Cookie(DessertItem):
    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity
        self.priceperdozen = 80

    def calculateamount(self):
        totalprice = self.quantity * self.priceperdozen // 12
        return totalprice

    def __class__(self):
        return "Cookie"


class IceCream(DessertItem):
    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity
        self.priceperpiece = 65

    def calculateamount(self):

        totalprice = self.quantity * self.priceperpiece
        return totalprice
    def __class__(self):
        return "Ice Cream"


class Sundae(IceCream):
    def __init__(self, name, quantity):
        super().__init__(name,quantity)
        # self.quantity = quantity
        self.toppings=20

    def calculateamount(self):
        totalprice=super().calculateamount()+self.toppings
        return totalprice
    def __class__(self):
        return "Sundae"

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
            raise CartIsEmptyException()

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