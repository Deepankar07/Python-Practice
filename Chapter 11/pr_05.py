class vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str=""
        index=0
        for i in self.vec:
            str+=f" {i}a{index} +"  
            index +=1
        return str[:-1]

    def __add__(self,v):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + v.vec[i])    
        return vector(newlist)
            
    def __mul__(self,v):
        sum=0
        for i in range(len(self.vec)):
            sum +=self.vec[i]*v.vec[i]
        return sum  

    
v1=vector([1, 2, 3])    
v2=vector([2, 4, 6])    
print(v1+v2)
print(v1*v2)
