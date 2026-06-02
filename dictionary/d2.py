student = {
    "vansh": 85,
    "rahul": 90,
    "aman": 78,
    "priya": 92
}
search=input("enter entity")
if search in student:
    for i in student:
        if i==search:
            print(student[i])
else:
    print("no user found")
    