sub1=int(input("Enter the first subject mark\n"))
sub2=int(input("Enter the second subject mark\n"))
sub3=int(input("Enter the third subject mark\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
elif((sub1+sub2+sub3)/3<40):
    print("You are fail") 
else:
    print("You are passed")       