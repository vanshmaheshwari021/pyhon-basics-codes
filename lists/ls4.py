'''find a number in a list'''
ls=[20,5,30,6,33,13,95,87,65,48,72,36,1]
find=int(input("enter no"))
for i in ls:
    if i==find:
        print((ls.index(i)+1))
if find in ls:
    print("found")
else:
    print("nahi hai")