class programmer:
    company = "microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"the name of {self.company} programmer is {self.name} and the product is {self.product}")
deepankar = programmer("deepankar","google")
alka= programmer("alka","github") 
deepankar.getinfo()
alka.getinfo()
