'''Check  tuple  elements same or not'''
#tuples are immutable so u have to create another list that stores the values and than convert it into tuple
tp1=(5,5,5,4)
hp=0
for i in tp1:
    if tp1[0]!=i:
        hp=-1
        break
        
if (hp==-1):
    print("false")
    
else:
    print("true")