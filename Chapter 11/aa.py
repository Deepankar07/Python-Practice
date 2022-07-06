#n =int(input(""))
#i=1
#while i<=n:
#    print(i)
#    i=i+1

#print(input()==0 or hash(tuple(map(int,input().strip().split()))))

n,m=input().split()    # To take input in one line separated by space use this
l=[int(item) for item in input().split()]
#for items in range(int(n)):
#    e=list(map(int,input().split()))
#    l.append(e)
#l.append(int(m))
print(l)
hapiness=0
a=set()
a=[int(item) for item in input().split()]
print(a)  
b=set()
b=[int(item) for item in input().split()]
print(b)      
for item in l:
    if item in a:
        hapiness=hapiness+1
    elif item not in a:
        hapiness=hapiness-1

print(hapiness)