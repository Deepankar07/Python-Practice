def game():
    return 98
g=game()
f=open('highscore.txt','r')
data=f.read() 
print(data)

if str(g) > data or data == " " :
    f=open('highscore.txt','w')
    f.write(str(g))
    f.close()