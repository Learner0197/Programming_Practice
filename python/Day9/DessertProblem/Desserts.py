from abc import ABC,abstractmethod

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

