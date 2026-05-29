i = 1

while i <= 5:

    if i == 3:
        i += 1
        continue

    print("yoii", i)
    i += 1
    '''here i encounter an infinite loop because when the value 
    is ==3 and we didnt add any itrato in if block then it stucks 
    on 3
    and loop runs infinitly
    '''
    '''you can also run i=1 before so that the updation heppens first and 
    then break happens
    '''