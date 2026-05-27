" condition inside a condition"
id=input('admin id ')
ps=input('password')
ad='admon'
p='pswrd'
if(id==ad and ps==p):
    print("sucessfully log in")
else:
    if(id!=ad and ps==p):
        print("name is wrong")
    elif(id==ad and ps!=p):
        print("password is wrong")
    else:
        print("both invalid")