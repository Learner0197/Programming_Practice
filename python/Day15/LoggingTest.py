import logging
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="calci.log", level=logging.DEBUG, format = FORMAT)

class Calculator:
    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        if(b>a):
            logging.info("Difference should not be negative")
        else:
            return a-b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if(b==0):
            logging.warning("Division by zero")
        else:
            return a / b

print(Calculator().div(24,0))
print(Calculator().sub(21,854))
print(Calculator().sum(16,7))
print(Calculator().div(46,23))