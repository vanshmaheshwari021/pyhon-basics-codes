#condition of age that what is the
# person according tu age like child adult teenager old baby 
age=int(input("enter no"))
#variable decared age that takes intiger and using input function 
#we are getting the value 
if (age<0):
    print("invalid age ")
elif(age>=0 and age<=3):
    print("baby")
elif(age>3 and age<=12):
    print("child")
elif(age>12 and age<=18):
    print("teenager")
elif(age>18 and age<=60):
    print("adult")
else:
    print("snr citizon")