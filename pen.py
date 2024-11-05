num=int(input("no of values: "))
a=[]
for i in range (num):
    b=int(input("enter the number"))
    a.append(b)
    

n=0
for i in range(len(a)):
    if (a[i]%2==0):
        n=n
    else:
         n=n+1
print("total no of swaps ",n)
