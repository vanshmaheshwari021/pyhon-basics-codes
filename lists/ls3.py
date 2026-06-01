''' average of list'''
ls=[4,8,0,4,16,6,4,8,0,4]
sum=0
for i in ls:
    sum=sum+i
    avg=sum/len(ls)
print(avg)