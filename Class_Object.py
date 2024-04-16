'''
QS:1
class Student:
    name="Pappu Kumar"
S1=Student()
print(S1.name)

#Qs:2
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Karan",98)
print(s1.name,s1.marks)
s2=Student("Aman",89)
print(s2.name,s2.marks)

#QS:3
class Student:
    def __init__(self,name,marks):   #constructor
        self.name=name
        self.marks=marks
    def welcome(self):    # method
        print("Welcome New Student")
    def get_marks(self):
        return self.marks
        
s1=Student("Karan",98)     #object
print(s1.name,s1.marks)
s2=Student("Aman",89)
print(s2.name,s2.marks)
s1.welcome()
print(s1.get_marks())

#QS:4
class Student:
    def __init__(self,name,marks):   #constructor
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("average : ",sum/3)

        
s1=Student("Karan", [98,97,99])     #object
s1.get_avg()

#QS:5 Create Account class with 2 attribute balance and account-no. create method for debit,credit,print the balance.

class Account:
    def __init__(self,bal,account):
        self.balance=bal
        self.account_no=account

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount, "Was debit")
        print("Total balance:",self.get_balance())   

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount, "Was credited")
        print("Total balance:",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(1000)

#QS:6
class Car:
    
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("car stop")
class Toyota_Car(Car):
    def __init__(self,name,color):
        self.name=name
        
Car1=Toyota_Car("Fortuner")
Car2=Toyota_Car("prius")
print(Car2.start())
print(Car1.stop())


#QS:7

class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to class B"
class C(A,B):
    varC="Welcome to class c"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

class Person:
    name="anonymous"
    # def changeName(self,name):
    #     self.name="Rahul"
    @classmethod
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("pappu Kumar")
print(p1.name)
print(Person.name)


#QS:8

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    # def CalcPercentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
   
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"



stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy=87
# print(stu1.phy)
# stu1.CalcPercentage()
print(stu1.percentage)

#QS:9

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22/7)*self.radius **2
    def perimeter(self):
        return (22/7)*2*self.radius


c1=Circle(14)
print(c1.area())
print(c1.perimeter())

# QS:10
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("role:",self.role)
        print("dept:",self.dept)
        print("salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","It",75000)

eng1=Engineer("Rahul",34)
eng1.showDetails()
print(eng1.name,eng1.age)

print()
e1=Employee("Accountant","Finance",60000)
e1.showDetails()'''

#QS:11
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return ord1.price>ord2.price
    
ord1=Order("chips",20)
ord2=Order("biscut",30)
print(ord1>ord2)

