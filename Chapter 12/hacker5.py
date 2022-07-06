
s = input()
print(s.isalnum())   
def hasalpha(s):
    return any(char.isalpha() for char in s)    
print(hasalpha(s))
def hasnumber(s):
    return any(char.isdigit() for char in s)
print(hasnumber(s))
def haslower(s):
    return any(char.islower() for char in s)
print(haslower(s))
def hasupper(s):
    return any(char.isupper() for char in s)
print(hasupper(s))

