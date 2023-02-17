n = input("enter the limit:")
lst = []
c = 0
for i in range(n):
    x = input("enter the names:")
    lst.append(x)
for i in lst:
    for j in i:
        if 'a' in j:
            c = c + 1
print("the occurence of a is:", c)
