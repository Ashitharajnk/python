lst=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    x=int(input("enter the elements:"))
    lst.append(x)
for i in range(0,n):
    if lst[i]>100:
        lst[i]="over"
print(lst)