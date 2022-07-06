num=input("Enter the number: ")
def increment(num):
    try:
        return int(num)+2
    except:
        raise ValueError ("Wrong Input")


b=increment(num)
print(b)