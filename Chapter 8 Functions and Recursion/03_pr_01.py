def maximum (num1 , num2 , num3):
    if (num1 > num2):
        if(num1>num3):
            return num1
        else:
            return num3
    if (num2>num1):
        if(num2>num3):
            return num2
        else:
            return num3
a = maximum(555,66,88)
print("maximum of above three is "+ str(a))                            