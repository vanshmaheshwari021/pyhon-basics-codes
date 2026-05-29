"this is an alternative cace of if else"
no=int(input("enter no"))
"after match whaever you write that will go in the cases"
match no:
    case 1:
        print("1")
    case 2:
        print("2") 
    case 3:
        print("3")
    case _ if no>3:
        print("greater then 3")  