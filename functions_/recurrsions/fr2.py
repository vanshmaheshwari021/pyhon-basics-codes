'''sum of no using recirssion'''
a=int(input('enter no'))
def sum(a):
    if (a==0 or a==1):
        return a
    return(a+sum(a-1))
print(sum(a))