# print("let start we are learing python")

#hello i am devil 
# """"hello this is multile
# prince sachin rahul sourav"""

#sher="prince"
#a="sachin"

# youtubeSchool="students" # camel case
# YoutubeSchool="students" # pascal case
# youtube_school="students" # snake case

# st='ooo 9u87535'
# print(type(st))

#b =True
#s= False
#print(type(b))


#a= "hello brother"

#print(a[6])

# a= "sher coder"
# print(a[5::1])

# a =12
# a=str(a)
# print(a)
# print(type(a))
#b= "89"
#b= int(b)
#print(type(b))

#print(12/4)

# name="prince"
# age="18" 

# print("hello my name is",name,"and my age is")
# #print(f"my name is {name} and my age is {age}")

# age = int(input("hello what is your age"))
# print("hello my name is",name,"and my age is",age)
# print(age)

# rrrr = str(input("hello what is your name"))
# print(rrrr)

# print( 5!= 5)

# a = 2
# b= 40

# print(a+b)
# print(a-b)
# print(a*b)
# print(b//a)
# print(b/a)
# print(5**99)

#print(35+8/4) "it Also follow BODMAS RULE"

#ASSIGMENT operators
#a= 23

#compund assigment operators
 
# a= 20
# a +=50
# a -=30
#a *=10
# a/= 5

# print(a)


# a =5
# a = a+5
# a+=5

# print(a)

# conditional statement

# a=12

# if a > 20:
#     print("i am ready")

# else:
#     print("i am not ready")


# money= int(input("please provide me money :-"))

# if money == 10:
#     print("i will buy pen")

# elif money == 20:
#     print(" i will buy a car")

# else:
#     print("i will buy a toy")

# FOR LOOP

# a= range(1,33,2)

# for chacha in a:
#     print(chacha)

# for chachi in range(20,51):
#     print(chachi)

# for chachi in range(-15,-2):
#     print(chachi)

# for chachi in range(16,0,-1):
#     print(chachi)

# LETS PRINT TABLE OF 5

# for table in range(5,301,5):
#     print(table)

# n=int(input(" which table you want:- "))

# for i in range(n,(n*10)+1,n):
#     print(i)

# a= "WORLD IS SO BEAUTIFUL"
# print(len(a))


# for i in range(len(a)):
#     print(a[i])

# for i in range(1,21):
#     if i == 20:
#         print("berak statement is excuted")
#         break
#     print(i)

# else:
#     print("break statement is not executed")
        

"FUNCTION"

# def hello():
#     print("this is a hello function so i am doing hello")

# hello()

# def sum(a,b):
#     print(f"the sum of your numbers is {a+b}")

# sum (15,16)
# sum (17,24)

# def pallindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev+st[i]

#     if rev== st:
#         print(f"{st} is a pallindrome")

#     else:
#         print(f"{st} is not a pallindrome")

        
# pallindrome("naman")
# pallindrome('prince')

# def hello():
#     return("hello how are you")

# print(hello())

"DATA STRUCTURE"

# a =[12,13,14,15,16,23.4,True,print()]

# # print(a[0:5:1])

# # 1st way using index

# for i in range(len(a)):
#     print(a[i])

# # 2nd way directily on values

# for i in a:
#     print(i)

# print(dir(list))

# help(list)

# l=[1,2,4,5,4,4]

# l.append(7)
# l.append(8)

# l.insert(1,3)

# l.remove(4)
# l.extend([78,90,89])
# index =l.index(4)
# count =l.count(4)
# pop =l.pop(2)

# # l.sort()
# # l.reverse()
# # l.clear()
# print(f"index of 4 is{index},pop of 2 is {pop} and count of 4 is {count} ")

'TUPLE'

# a=(1,3,45,66,55)

# # print(type(a))

# # print(a[2])

# # for i in range(len (a)):
# #     print(a[i])

# index= a.index(45)
# print(index)

# count=a.count(3)
# print(count)

# a,b,c,d=(1,3,5,7)
# # tuple un packing
# print(c)

'sets'

# s={2,4,5,5,6,7}
# print(s)

# b=hash("hello")
# print(b)

# a={1,8,9,3,5,"hello",2,6}

# for i in a:
#     print(i)

"dictionary"

# d={10:"hello",20:56,30:90,"lol":"♥️♥️"}

# # print(type(d))

# print(d[20])

# print(d["lol"])

# d[10]="achha" #upadating
# d[40]= 500 #cerating
# del d[30] #deleting

# print(d[10])

# for i in d:
#     print(i)
#     print(d[i])

# help(dict)

# a=[2,4,5,6]
# b=a.copy() #shallow copy

# b[0]=100

# print(a)

"EXCEPTION HANDLING"

# a= int(input("tell your number ="))

# try:
#     print(10/a)

# except ZeroDivisionError: #zerodevisionerror= Exception as err
#     print("sorry you can't divided by zero")

# print("ok, i have done this division ")

# method 2

# a= int(input("tell your number ="))

# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry there is an error as {err}")

# print("ok, i have done this division ")

# raise function 

# age = int (input(" tell your age = "))

# if age<10 or age> 18 :
#     raise ValueError("your age must be between 10 and 18")
# else :
#     print("welcome to the club")


# print("club will start soon")


"FILE HANDLING"

# p= open('loop.py')

# print(p.read())

# r= open ("good.txt",'a')

# r.write("hello this is prince and i a creating and writing inside file ")
# r.write("and now i am appending some content inside the file")

# r.close()


# print("press 1 for creating a file")
# print("press 2 for reading a file")
# print("press 1 for updating a file")
# print("press 1 for deleting a file")

# check= int (input("p"))

"OOPS"

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

"LAMBDA FUNCTION"

# addition = lambda a,b : a+b

# print(addition(12,13))

# addition = lambda a: "even" if a %2 ==0 else "odd"

# print(addition(13))

"MAP FILTER AND ZIPS"

# a =[1,2,3,4,5]

# result = map(lambda x :x*2 ,a)

# print(list(result))

# a =[1,2,3,4,5]

# def square(x):
#     return x**2


# result = map(square,a)

# print(list(result))

# def even(x):
#     if x%2 ==0:
#         return True
#     else:
#         return False
    
# a =[1,2,3,4,5,6,7,8]    

# result = filter(even , a)

# print(list(result))

# result =filter( lambda a:True if  a%2== 0 else False ,a)

# print(list(result))

'modules and packages'



