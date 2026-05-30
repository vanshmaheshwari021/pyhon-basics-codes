''' fn  print a to b'''
a=int(input("enter no"))
b=int(input("enter till"))
def fun(a,b):
    if (a==b):
        return a
    for v in range(a,b+1,1):
        print(v)
print(fun(a,b))
    
    