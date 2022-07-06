from logging import exception


while(True):
    print("Press q to quit")
    a=input("Enter the number: ")
    if a=='q':
        break
    try:
        a=int(a)
        if a>6:
            print("Entered number is greater than 6")
    except Exception as e:
        print(e)

print("Thanks for playing !")