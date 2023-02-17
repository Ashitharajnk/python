n1=int(input("enter the 1st num:"))
n2=int(input("enter the 2nd num:"))
i=1
while(i<=n1 and i<=n2):
    if(n1%i==0 and n2%i==0):
        gcd=i
    i=i+1
print("GCD:",gcd)