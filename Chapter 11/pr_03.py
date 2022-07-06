class employee:
    salary=1000
    increment=1.5
    @property 
    def salaryafterincrement(self):
        return self.salary*self.increment

    @salaryafterincrement.setter
    def salaryafterincrement(self,salaryafterincrement):
         self.increment=salaryafterincrement/self.salary    

e=employee()
print(e.salary)
print(e.salaryafterincrement)
e.salaryafterincrement=2000
print(e.increment)         