c=int(input("enter the current year"))
f=int(input("enter the final year"))
print("the future leap years are:")
for i in range(c,f+1):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)
        