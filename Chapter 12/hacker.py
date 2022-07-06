n=int(input())
l=[]
for items in range(n):
    e=input()
    l.append(e)
print(l)    
s={items for items in l}
print(s)
print(len(s))