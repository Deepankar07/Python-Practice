with open("table.txt") as f:
    content=f.read()
content=content.replace("donkey","#@$!%")    
with open("table.txt",'w') as f:
    f.write(content)