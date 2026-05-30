a=(int(input("enmter no")))
def count(a):
    if a<10:
        return 1
    
    return 1+count(a//10)
print(count(a))