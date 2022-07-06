words=["donkey","mote","hyna"]
with open("table.txt") as f:
    content=f.read()
for word in words:    
    content=content.replace(word,"#@$!%")    
with open("table.txt",'w') as f:
    f.write(content)