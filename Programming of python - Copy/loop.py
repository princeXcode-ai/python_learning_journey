# QUESTION NO 1
# n=int(input("how many hello world do you want:-"))


# for i in range(n):
#     print("hello world")

# QUESTION NO 2

# n=int(input("nutural number:-"))

# for i in range(1,n+1):
#     print(i)

# QUESTION NO 3

# n= int(input("reverse counting from :- "))

# for i in range(n,0,-1):
#     print(i)

# QUESTION NO 4

# n=int(input("TABLE OF :- "))

# for i in range(n,n*10+1,n):
#     print(i)

"method 2"

# n= int(input("which table you want :- "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# "QUESTION NO 5"

# sum = 0
# # n = int(input("sum up to :-"))

# # for i in range(1,n+1,1):
# #     sum += i

# # print(sum)

# n = int(input("Enter n: "))

# total = 0
# for i in range(1, n + 1):
#     total += i

# print("Sum =", total)


# def sum_n(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# print(sum_n(5))  # Output: 15

"question no 6"

# n=int(input("factorial of a number:-"))
# total=1
# for i in range(1,n+1,1):
#     total *= i

# print("factroial=",total)

"QUESTION NO 7"

# n=int(input("sum no. upto:- "))

# oddTotal = 0
# eventotal = 0
# for i in range(1,n+1,1):
#     if(i % 2 == 0):
#         eventotal += i

#     else:
#        oddTotal += i
  
# print("sum of even no",eventotal)
# print("sum of odd total" , oddTotal)

"QUESTION NO 8"

'print all factors of a given number'

# n=int(input("factors of no:-"))


# for i in range(1,n,1):
#     if n%i==0:
#         print("factor =",i)

    # else:
    #     print("not a factor of given no.",i)

'QUESTION NO 9'
"PERFECT NUMBER OR NOT"

# n=int(input("factors of no:-"))
# total =0

# for i in range(1,n,1):
#     if n%i==0 :
#         total+=i

# print("is this perfect number = ", n == total)   

# if(n == total):
#     print("given number is perfect number")
# else :
#     print("not a perfect number")

"question no 9"

# n=int(input("give any number:- "))
# total=0

# for i in range(1,n+1,1):
#     if n%i==0:
#         total = total + 1


# if total ==2:
#     print("given no is a prime number")

# else:
#     print("given no is a not prime number")

"QUESTION NO 10"

# a= "important"


# for i in range (len(a)-1,-1,-1):
#     print(a[i])

# print(a[::-1])      


"QUESTION NO 11"       

# a= "naman"
# b=""

# for i in range (len(a)-1,-1,-1):
#     b= b+a[i]

# if b==a :
#     print('your word is pallindrome')
    
# else:
#     print("word is not a pallindrome")

"question no  12"

# a = "spark1724923313!@#$$%^&**("

# char=0
# dig=0
# spchar=0

# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchar+=1

# print(f"your digit are {dig}\nyour alphabets are {char}\nyour special characters are {spchar}")


print(dir(str))