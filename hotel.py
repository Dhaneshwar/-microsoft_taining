a="pizza = 200"
b="burgger = 180"
c="briyani = 250"
d="dosa = 80"
e="idly=50"
print(a , b , c , d , e )
n=int(input("how many items u need to order?"))
sum=0
for i in range(n):
    item=input("enter the item u need to order : ")
    if(item=="a"):
        print("pizza")
        qty1=int(input("enter the quantity you want:"))
        sum+=200*qty1
    elif(item=="b"):
        print("burgger")
        qty2=int(input("enter the quantity you want:"))
        sum+=180*qty2
    elif(item=="c"):
        print("briyani")
        qty3=int(input("enter the quantity you want:"))
        sum+=250*qty3
    elif(item=="d"):
        print("dosa")
        qty4=int(input("enter the quantity you want:"))
        sum+=80*qty4
    else:
        print("idly")
        qty5=int(input("enter the quantity you want:"))
        sum+=50*qty5
print("total ",sum)
if(sum>1000):
    print("discount")
    sum1=sum*0.10
    tot=sum-sum1
    print("final bill :",tot)
else:
    print("final bill ",sum)
