#sum = 1 + 2 + ..... + n
n= int(input("enter the value of n: "))
i=1
sum = 0
while i in range (1,n+1):
    sum= sum + i
    i=i+1
print(f"the sum of first {n} natural number is {sum}")
