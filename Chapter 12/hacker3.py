n=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))
d=set()
e=set()
for i in s1:
    if i==s2:
        d.add(i)
    else:
        e.add(i)    
for i in s2:
    if i==s1:
        d.add(i)
    else:
        e.add(i)

print(len(d)+len(e))            