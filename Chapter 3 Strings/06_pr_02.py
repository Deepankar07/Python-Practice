Letter = ''' Dear <|NAME|>
I am glad to inform you about your selection in our company.
You are selected !
Thanks & Regards, 
Depix
Date: <|DATE|>
'''
Name = input("Enter your Name\n")
Date = input("Enter Date\n")
Letter = Letter.replace("<|NAME|>", Name)
Letter = Letter.replace("<|DATE|>", Date)
print(Letter)