num=int(input())
table=[num*i for i in range(1,11)]
print(str(table))

with open("2Tables.txt",'a') as f:
    f.write(str(table))
    f.write("\n")