lst=[]
n=int(input("enter the size of list:"))
for i in range(0,n):
    x=int(input("enter the elements:"))
    lst.append(x)
    print("square of numbers are:")
    for i in lst:
        sqrt=pow(i,2)
        print(sqrt)