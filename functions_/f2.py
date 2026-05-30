'''there is something default value exsists in '''
a=int(input("enter no"))
b=int(input("enter no"))
def sum(a=0,b=0):
    return(a+b)
print(sum(a))
    
'''here in arguments we just passed down a so b will 
    automatically count as 0 '''