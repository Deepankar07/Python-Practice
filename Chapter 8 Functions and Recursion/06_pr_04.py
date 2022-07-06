from tkinter import N


def sum(n):
    if n == 0 or n==1:
        return 1

    return (n + sum(n-1))

s =sum(10)
print(s)    

            
 


