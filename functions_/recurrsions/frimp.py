a=int(input("no"))
def feb(a):
    if (a==1 or a==0):
        return a
    a=(feb(a-2)+feb(a-1))
    return a
print(feb(a))
