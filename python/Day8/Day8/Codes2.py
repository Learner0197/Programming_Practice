from wsgiref.util import request_uri


class Calculator:
    def add(self,a=0,b=0):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a//b

class advcalc(Calculator):
    def div(self,a,b):
        return a%b

    def mul(self,a,b):
        return a**b



c=Calculator()
a=advcalc()
print(c.div(25,2))
print(a.div(25,2))

print(c.mul(2543,2534))
print(a.mul(2545,45))

print(c.add(53,44.7))
print(c.add())
print(c.add(53))
