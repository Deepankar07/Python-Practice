n=int(input())
for _ in range(0,n+1):
    min1,max=input().strip().split()
    #min2,maxx=input().strip().split()
    for i in range(int(min1),int(max)+1):
        b=str(i)
        r=b[::-1]
        if b==r:
            print(f"Case 1: {len(b)}")    

#for i in range(int(min2),int(maxx)+1):
#    b1=str(i)
#    r1=b1[::-1]
#    if b1==r1:
#        print(f"Case 2: {b1.count(str(i))}")    
        
    
    

