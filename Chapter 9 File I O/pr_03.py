for i in range (2,21):
    with open(f"table.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")
            if j!=10:                     # To remove extra bullet no. of rows after 10
                f.write("\n")
        