# class Factory:
#     a = 12  #atribute
    
#     def hello(self): #methods
#         print("how are you")
        
#     print("hello how are you i am getting")
    
# print(Factory().a)

# Factory().hello()

# obj = Factory()

# print(obj.a)

# obj.hello()

# class factory :
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets =pockets
    
#     def show(self):
#         print(f"your object details are {self.material},{self.pockets},{self.zips}")
        
        
        
# reebok= factory("leather",3,2)

# campus =factory("nylon",4,3)

# # print(reebok.pockets)

# reebok.show()

# class animal:
#     name = "lion" #class attributs
    
#     def __init__(self,age):
#         self.age = age #instance attribute
        
#     def show(self): #instance method
#         print(f"how are you and your age is {self.age}")
        
#     @classmethod 
#     def hello(cls):
#         print("how are you  brother")
        
#     @staticmethod
#     def static():
#         print("how are you")
        
# obj = animal(12)

# obj .show()

# "four pillers"

# 'inheritance'

# class factory:   #parent class / super class
#     a="i am an attribuites mentioned in a factory "
#     def hello(self):
#         print("hello i am method mentioned inside factory")
        
        
# # class factorypune(factory):  #chid class /sub class
# #     pass

# obj = factory()
# # obj2= factorypune()

# print( obj.hello())

# class animal:
#     def __init__(self,name):
#         self.name= name
        
#     def show(self):
#         print(f"hello your name is {self.name}")       
        
        
# class human(animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
        
#     def show(self):
#         print(f"hello your name is {self.name},{self.age}")

# animal1= animal("lion")
# person1=human("prince",18)

# person1.show()

# class animal:
#     def __init__(self,name):
#         pass
    
# class humans:
#     def __init__(self,name, age):
#         pass
    
# class robots(humans, animal):
#     name3 = "gangu bai"
    
# obj = robots("prince",18)

# class factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips
        

# class biharfactory(factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color
        
# class delhifactory(biharfactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets
        
# obj = delhifactory()

# obj.

# "polymorphism"

# def show():
#     print("how are you")
    
# def show():
#     print("i am fine")
# show()



# class animal:
#     def show(self):
#         print("hello jii , i am prince")
        
# class human(animal):
#     def show(self):
#         print("how are you")
        
# obj =human()
# obj. show()
    

# class animal:
#     def show(self):
#         print("i am showing")
        
# class human:
#     def show(self):
#         print("hello i am showing")
        
# obj = animal()
# obj2 = human()

# obj.show()
# obj2.show()

'encapsulation '

# class factory:
#     _a= "pune"
    
#     def show(self):
#         print(" hello i am pune factory")
        
# class bhopal(factory):
#     def show2(self):
#         print(super().a)

# obj= bhopal()
# obj.show2()

# class factory:
#     __a = "pipra"
    
#     def __show():
#         print("hello i am a factory")
        
# obj = factory()
# # print(obj.__a)
# obj.show()

"abstraction"
# from abc import ABC ,abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     def area(self):
#         pass

# class square(abstract):
#     def __init__(self,side):
#         self.side = side
        
#     def perimeter(self):
#         print("i have created this")
        
#     def area(self):
#         print("i am good")
        
# class circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def perimeter(self):
#         print("i have created this")
        
#     def area(self):
#         print("i am good")
        
# obj = circle(5)
# obj2= square(5)

"DUNDER METHOD"

# class animal :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
        
#     def __str__(self):
#         return(f"hello how are you and your name is {self.name}")
    
#     def __add__(self, other):
#         return(f"your sum of ages are {self.age+other.age}")
        
# obj = animal("lion",12)
# obj2 =animal("dolphin",11)


# print(obj+obj2)



# class animal :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
        
#     def __str__(self):
#         return(f"hello how are you and your name is {self.name}")
    
#     def __add__(self, other):
#         sum=0
#         for i in other:
#             sum =sum + i.age
#         return(f"your sum of ages are {self.age+sum}")
        
# obj = animal("lion",12)
# obj2 =animal("dolphin",11)
# obj3 = animal("tiger",34)

# print(obj + (obj2, obj3))

"DECROTERS"

# class animal:
#     @property
#     def show(self):
#         print ("hello how are you ")
        
# obj = animal()

# obj.show

# def decorate(func):
#     def wrapper():
#         print("i print my self before the function hello")
#         func()
#         print("i will print after the function")
#     return wrapper

# @decorate
# def hello():
#     print("hello i am prince")
    
# hello()


# def decorate(func):
#     def wrapper(a,b):
#         print("the addition to your number is")
#         func(a,b)
#         print("i hope you liked it")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"your total is {a+b}")
    
# addition(12,34)


# def addition (*args):
#     sum =0
#     for i in args:
#         sum =sum + i
    
#     print(sum)
    
# addition(12,23,45,56,78)


# def information(**kwargs):
#     print("your information is\n\n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    
    
    
# information(name = "prince",age= 18, desination ="AI/ML")


"COMPHREHENSION"

# for i in range(1,21):
#     if i %2 ==0:
#         print(f"{i} =even")

# l={i : i**3 for i in range(1,10)}

# print(l)