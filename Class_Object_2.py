# QS :1
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(s1.name,s1.age)
s1=Person("Amit",22)
s1.show()

#QS :2
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
       
        print("Area:",self.radius*(22/7)**2)
    def perimeter(self):
        
        print("Perimeter:",self.radius*(22/7)*2)
c1=Circle(14)
c1.area()
c1.perimeter()
    

#QS :3

class Rectangle:
    def __init__(self):
        self.length=0
        self.breath=0

    def setDimension(self,length,breath):
        self.length=length
        self.breath=breath

    def showDimension(self,length,breath):
        print("length :",self.length)
        print("breath :",self.breath)

    def getArea(self):
        print("Area :",self.length*self.breath)

r1=Rectangle()
r1.setDimension(23,45)
r1.showDimension(23,45)
r1.getArea()

# QS 4

class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price

    def show(self):
        print("Bookid :",self.bookid)
        print("Title :",self.title)
        print("Price :",self.price)

b1=Book(1.1,'Introduction',230)
b1.show()'''

#QS 5

class Team:
    def __init__(self,member=[]):
        self.member=member

    def add_member(self,name):
        self.member.append(name)

    def display_member(self) :
        for member in self.member:
            print(member)
t1=Team()
t1.add_member("Ms Dhoni")
t1.add_member("Rohit")
t1.add_member("Kolhi")

t1.display_member()
        