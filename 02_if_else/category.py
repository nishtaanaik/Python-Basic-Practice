# to print if their an child,teenager,adult or senior citizen
age = int(input("enter your age:"))

if(age <13):
    print("child")
elif(age <= 19):
    print("Teenager") 
elif(age <= 59):
    print("Adult")
else:
    print("Senior Citizen")


