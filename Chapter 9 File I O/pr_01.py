f=open('another.txt','r')
data=f.read()
print(data)
if "twinkle" in data:
    print("twinkle is present")
else:
    print("twinkle is not present")    
f.close()    