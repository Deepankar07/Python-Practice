import random
def game(comp,you):
    if comp == you:
        return None
    elif comp == "s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="s":
            return True
        elif you=="g":
            return False
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True
print("comp turn: snake(s) water(w) or gun(g)")
random_no = random.randint(1,3) 
if random_no == 1:
    comp="s"
elif random_no == 2:
    comp ="w"
elif random_no == 3:
    comp ="g"

you=input("your turn: snake(s) water(w) or gun(g)")
a=game(comp,you)
print(f"comp chose {comp}") 
print(f"you chose {you}")           
if a== None:
    print("game is a tie")
elif a==True:
    print("you win")
else:
    print("you lost")           

