from operator import truediv


def greater_than_five(num):
    if num>5:
        return True
    else:
        return False
l=[1,6,7,3,8,9,2,3]       
print(list(filter(greater_than_five,l)))  

g=lambda num:num<5
print(list(filter(g,l)))   