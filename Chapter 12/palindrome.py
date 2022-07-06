from audioop import reverse


#n=int(input())
#b=str(n)
#r=b[::-1]
#if b==r:
#    print("This is a palindrome")
#else:
#    print("Not")    
#
min=int(input())
max=int(input())
for i in range(min,max+1):
    b=str(i)
    r=b[::-1]
    if b==r:
        print(b,end="   ")

    