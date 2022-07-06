def remove_and_strip(string, word):
    newstr=string.replace(word, "")
    return newstr.strip()
this="   Deep is a good boy  " 
n=remove_and_strip(this, "Deep")
print(n)    