# Object Oriented Programming - everything in python is an object

mylist = [1,2,3]
mylist.append(4)
print(mylist)

print(type([]))
print(type(()))
print(type(20))
print(type(20.0))
print(type(False))

# classes

class Sample():
    pass

x = Sample()
print(type(x))

class Dog():

    # class object attribute
    species = 'mammal'

    def  __init__(self, breed, name): # method refers to itself
        self.breed = breed
        self.name = name

mydog = Dog(breed = 'pit bull', name = 'spike')
print(mydog.breed)
print(mydog.name)
print(mydog.species)
print(type(mydog))

odog = Dog('huskie', 'enoch')
print(odog)
print(odog.breed)
print(odog.name)

class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(999)
print(myc.area())
myc.radius = 100
print(myc.radius)
print(myc.area())

# Inheritance
class Animal():

    def __init__(self):
        print('animal')

    def whoAmI(self):
        print('lion')

    def eat(self):
        print('Bible')

mya = Animal()
mya.eat()
mya.whoAmI()

class Dogg(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('dogg')

    def bark(self):
        print('woof')

    def eat(self):
        print('treat')

mydogg = Dogg()
mydogg.whoAmI()
mydogg.eat()

# Special Methods
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title: {}, Author: {}, Pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('a book is destroyed')

b = Book('Romans', 'Paul', 16)
print(b)
print(len(b))
del b

alist = [1,2,3]
print(alist)

