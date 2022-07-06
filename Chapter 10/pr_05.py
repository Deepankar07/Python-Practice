seatnumber = [1, 2]
class train:
    def __init__(self, name, fare, seats,seatnumber):
        self.name =name
        self.fare =fare
        self.seats =seats
        self.seatnumber =seatnumber

    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available are {self.seats}")

    def getfaredetail(self):
        print(f"The fare of the booked seat under the train {self.name} is {self.fare}")

    def bookticket(self):
        if (self.seats>0):
             print(f"Your ticket has been booked and your seat number is {self.seats}")
             self.seats = self.seats - 1
        else:
            print("Sorry the train is full")    

    def cancelticket(self):
        self.seatnumber=input("Enter your seat number you want to cancel :")
        print(f"Your ticket booked under seat number{self.seatnumber} has been cancelled")
        self.seats=self.seats + 1



intercity=train("Intercity Express 14056", 100, 2, seatnumber) 
intercity.getstatus() 

intercity.bookticket()      
intercity.getfaredetail() 

intercity.bookticket()  
intercity.getfaredetail()  

intercity.bookticket()  
intercity.cancelticket()
intercity.bookticket()  



