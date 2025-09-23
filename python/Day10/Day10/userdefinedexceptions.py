class MyException(Exception):
    def __init__(self):
        super().__init__("This exception is because Aman was sleeping")

class TravelException(Exception):
    def __init__(self):
        super().__init__("No input from user...Travelled Kilometres cannot be zero")

class MedicalAllowanceException(Exception):
    def __init__(self):
        super().__init__("Medical Allowance less than minimal amount of Rs. 2000")
