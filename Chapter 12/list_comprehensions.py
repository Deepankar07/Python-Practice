l=[4,5,6,8,77,23,55]
#a=[] 
#for item in l:
#    if item%2==0:
#        a.append(item)
#print(a)

#Short cut for above
a=[item for item in l if item%2==0]  #-----list comprehension
print(a)