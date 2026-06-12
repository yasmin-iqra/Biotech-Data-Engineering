# 1.classes
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")



point1=Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2=Point()
point2.x=2
print(point2.x)

#2.Constructors
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point=Point(10,20)
print(point.x)
#Exercise
class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f"Hi,I am {self.name}")


iqra=Person("Yasmin Iqra")
iqra.talk()

bob=Person("Bob Smith")
bob.talk()

#3.Inheritance
#----------------------------------------------------------------------
#----------------------------------------------------------------------
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")00.000

dog1=Dog()
dog1.walk()

#4.Modules
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
from utils import find_max

numbers=[10,3,6,2]
max=find_max(numbers)
print(max)

#5.Packages
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
