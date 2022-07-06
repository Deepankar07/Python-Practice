import os

with open("newsample.txt") as f:
    content=f.read()
with open("rename_by_python.txt","w") as f:
    f.write(content)

os.remove("newsample.txt")
