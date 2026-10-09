s=int(input("enter a number"))
for i in range(1,s+1):
    if i%2!=0:
        print("*"*i)
    else:
        print("#"*i)
    