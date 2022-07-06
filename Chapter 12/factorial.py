n=int(input())
fact=1
#def factorial(n):
#    if n==0 or n==1:
#        return 1
#    return n*factorial(n-1)  
#factorial=factorial(n)      
for i in range(1,n+1):
    fact=fact*i

print(f"Factorial of {n} is {fact*i}",end="")
print(fact)