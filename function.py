'''def printinfo(name,age):
    print("Name:",name)
    print("Age:",age)
    return;
printinfo(name=str(input("Enter a name:")))
printinfo=input("Enter a age:")

printinfo(name="Ramakant Sharma",age=45):
print("Name:",name)
print("Age:",age)

printinfo(age=int(input("Entera Age:",)),name=input("Enter a name:"))
printinfo()'''


def printinfo(arg1,*vartuple):
    print("output is:",end="")
    for var in vartuple:
        print(var,end="/b")
        print()
        return
printinfo()
#printinfo(50,60,70,80)
