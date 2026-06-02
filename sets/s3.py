'''Given a list, print all elements that appear more than once in the list'''
list=[1,2,3,4,5,6,6]
s1=set()
s2=set()
for i in list:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
print(s2)
'''trick one it le me think too muchh
'''