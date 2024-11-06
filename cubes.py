m=int(input("enter the first no:"))
n=int(input("enter the second no:"))
if(m>n):
    print("invalid")
else:
    sum=0
    for i in range(m,n+1):
        sum=sum+i**3
    print(sum)
