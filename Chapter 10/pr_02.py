class Calculator:
    def __init__(self,number) :
        self.number = number

    def square(self):
         print(f"square of {self.number} is {self.number**2}")

    def squareroot(self):
         print(f"squareroot of {self.number} is {self.number**0.5}")

    def cube(self):
         print(f"cube of {self.number} is {self.number**3}")

a = Calculator(9)        
a.square()
a.squareroot()
a.cube()
