'''vowels count'''
count=0
sting=input("enter string")
for i in sting:
    if i in "aeiou":
        count=count+1
print(count)