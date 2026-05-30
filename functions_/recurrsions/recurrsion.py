'''factorial of n'''
n=int(input("enter no"))
def fec(n):
    if (n==0 or n==1):
        return n
    return n*fec(n-1)
    
print(fec())
''' here i discover a very popular topic taht is reccurssion a 
function calling itself again and again'''
