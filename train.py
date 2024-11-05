n=int(input("enter the no of tickets:"))
sum=0
for i in range (n):
    age=int(input ("enter the age:"))
    if(age>60):
        sum+=30
    elif(age<12):
        sum+=20
    else:
        sum+=50
print("total :",sum)
