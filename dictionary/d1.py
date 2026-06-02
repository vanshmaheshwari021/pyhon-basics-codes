'''Highest Marks Subject'''
a={
    "hindi":48,
    "english":51,
    "math":99
}
highest=0
for i in a:
    if a[i]>highest:
        highest=a[i]
print(highest)