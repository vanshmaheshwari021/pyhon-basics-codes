'''Letʼs create a Simple Calculator that performs arithmetic operations. Create 
a function calculator(a, b, operation) that performs addition, subtraction, 
multiplication, or division based on the operation parameter. 
[ 
operation 
parameter can have values , , & .'''
c=float(input("enter no"))
b=float(input("enter 2nd no" ))
a=input("enter oprator")
def cal(a,b,c):
    if a=="+":
        return c+b
    if a=="-":
        return c-b
    elif a=="*":
        return c*b
    elif a=="/":
        return c/b
    else:
        return "wrong operator"
print(cal(a,b,c))
    
