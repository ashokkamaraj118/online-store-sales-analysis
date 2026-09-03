# print ("ashok")
# a =float(int(input("enter the num1 ;")))
#


# date of birth
# a =int(input("enter the birth year ;"))
# b =2024
# c =b-a
# print(c)

# celsious value
# a=float("enter the celsius value ;")
# b=(the fehrenheit value is ;,b)
# c=float(input("enter the fehrenheit value ;"))ash
# d=(c-32)*5/9
# print("the celsius value is ;",d)


# age calculater
 a=(input("ashok kumar"))
 b=(input("2003"))
 a=input("enter your name;")
 b=int(input("enter your birth year ;"))
 print("hai,",a,"your age is",b)
 print(f"hai{a}your name is {b}")



# add num or even
# a=11
# if a%2==0:
#     print("even")
# else:
# #     print("odd")



# mini calculater
# a=int(input("enter the num 1"))
# b=int(input("enter the num 2"))
# c=input("choose the operation:add/sub/mul/div")
# if c=='add':
#     print(f"the addition is {a+b}")
# elif c=='sub':
#     print(f"the subration value is {a-b}")
# elif c=='mul':
#     print(f"the multiplication value is {a*b}")
# elif c=='div':
#     print(f"the division value is {a/b}")
# else:
#     print("givien num incorrect")


# find last num
# n=int(input("enter the num:"))
# print("last num:",n%10)


# grade system
# mark=int(input("enter the mark:"))
# if mark >=90:
#     grade='A'
# elif mark >=70 and mark > 90:
#     grade='B'
# elif mark >=50 and mark > 70:
#     grade='c'
# elif mark >=35 and mark > 50:
#     grade='D'
# else:
#     grade="FAIL"
# print(f"the grade of the mark{mark}is{grade}")


# loan eligibility
# age=int(input("enter your age:"))
# loan_amount=int(input("enter the loan amount:"))
# if(loan_amount > 50000 or age >= 18):
#     name=input("enter your name:")
#     if(age <=25):
#         print(f"{name}sorry...your loan amount limit is 20000 as bcoz your age is {age>18}")
#     else:
#         print(f"yes,{name}you can available the loan")
# else:
#     print("sorry you are not eligible")


# cource eligibility
# coc=input("enter the code oc conduct-good/bad---->")
# mark=int(input("enter the 10th mark:"))
# if coc=="good":
#     name=input("please enter your name:")
#     if mark >=450:
#         cource="bio maths"
#     elif mark >=400:
#         cource="computer science"
#     elif mark >=300:
#         cource="ARTS"
#     else:
#         print(f"sorry..{name}you are not eligible to these cource")
#     print(f"congrat{name}your mark is{mark}and you are eligible to take the{cource}cource")
# else:
#     print(f"sorry you are not eligible to apply the cource")


# division
# a=int(input("enter the number:"))
# b=a%100
# if b%3==0 and b%4==0:
#     print("it is divisible by 3 and 4")
# elif b%6==0:
#     print("it is divisible by 6")
# elif b%8==0:
#     print("it is divisible by 8")
# else:
#     print("it is not divisible")


    # electricity bill
# unit=int(input("enter the num of units"))
# amount=0
# if(unit<=100):
#     print(amount)
# elif(unit>100 and unit<=200):
#     amount=(unit-100)*5
#     print(amount)
# elif(unit>100):
#     amount=(unit-100)*10
#     print(amount)


# tax amount

# price=int(input("enter the amount"))
# tax_amount=0
# if(tax_amount>100000):
#     tax_amount=(15/100)*price
#     print(tax_amount)
# elif(tax_amount>50000):
#     tax_amount=(10/100)*price
#     print(tax_amount)
# elif(tax_amount<50000):
#     tax_amount=(5/100)*price
#     print(tax_amount)


# city = (input("enter the city : delhi / chenni --->"))
# if city .lower() =="delhi":
#     print(f"{city} has taj mahal")
# elif city.upper() =="CHENNAI":
#     print(f"{city} has marina beach")
# else :
#     print("no city")


# #  for loop
# a = int (input())
# b = int (input())
# for i in range (a,b):
#     print( i )

#  add / even
# a = int (input("enter the starting value"))
# b = int (input ("enter the ending value"))
# for A in range (a,b):
#     print( A , "even")

# a = 1
# b = 1000
# for A in range (a,b):
#     print( A , "even")


# table
# a = int ( input("enter the starting num"))
# b = int (input("enter the ending num"))
# for i in range ( a , b):
#     print(f"{i} * 5 = { i * 5}")


# #1st format
# a=int(input("enter the number :"))
# for  i in range (1,11):
# #     if a==1:
#         print(f"{i} x 1 = {i*1}")
#     if a==2:
#         print(f"{i} x 2 = {i*2}")
#     if a==3:
#         print(f"{i} x 3 = {i*3}")
#     if a==4:
#         print(f"{i} x 4 = {i*4}")
#     if a==5:
#         print(f"{i} x 5 = {i*5}")
#     if a==6:
#         print(f"{i} x 6 = {i*6}")
#     if a==7:
#         print(f"{i} x 7 = {i*7}")
#     if a==8:
#         print(f"{i} x 8 = {i*8}")
#     if a==9:
#         print(f"{i} x 9 = {i*9}")
#     if a==10:
#         print(f"{i} x 10 = {i*10}")
# else:
#     print("pls give num between 1-10")

# #2nd table format
# a=int(input("enter the num :"))
# for i in range (1,11):
#     print(f"{i} x {a} = {i*a}")


#total sum
# sum_even = 0
# sum_odd = 0
# for i in range (1,11):
#     if i%2 == 0:
#         print(i)
#         sum_even = sum_even+i
#     else:
#         print(i)
#         sum_odd += i
# print(f"{sum_odd}is the total sum value for odd number")
# print(f"{sum_even} is the total sum value")


# sum_even = 0
# sum_odd = 0
# for i in range (1,11):
#     if i%2 == 0:
#         print(i)
#         sum_even = sum_even+i
#     if i%2 != 0:
#         print(i)
#         sum_odd += i
# print(f"{sum_odd}is the total sum value for odd number")
# print(f"{sum_even} is the total sum value")


# for num in range (100):
#     if num ==50:
#         break
#     print(num)


# for num in range (10):
#     if num ==5:
#         continue
#     print(num)


# for num in range (1,100,+8):
#     print(num)


# c = 0
# for i in range (1001,2179):
#     if i%3 == 0 and i%4 == 0  and i%7 == 0 :
#         print (i)
#         c += 1
#     print(c)


# method 1
# prime number

# num = int(input("enter the num to check prime number or not :"))
# for i in range (2,num):
#     if num%i == 0:
#         print(f"{num}is not a prime number")
#         break
# else:
#     print(f"{num}is a prime number")

# method 2
#  prime number

# num = int (input("enter the number to check prime number or not : "))
# count = 0
# if num > 1:
#     for i in range (1,num+1):
#         if num%i == 0:
#             count += 1
#     if count == 2:
#         print("it is prime number")
#     else:
#         print("it not a prime number")
# else:
#     print("pls  enter num more than 1")



# swapping

# num1 = int(input("enter the num1 : "))
# num2 = int(input("enter the num2 : "))
# print(f"the number before swapping is {num1}")
# print(f"the number before swapping is {num2}")

# #approach
# # temp=num1
# # num1=num2
# # num2=temp

# #approach
# # num1,num2=num2,num1

# #approach
# num1 = num1+num2
# num2 = num1-num2
# num1 = num1-num2

# print(f"the number after swapping is {num1}")
# print(f"the number after swapping is {num2}")

 
# #factorial
# num = int(input("enter the number : "))
# f = 1
# for i in range (1,num+1):
#     f *=i
# print(f)


#fibanocci series
# num = int(input("enter the number : "))
# n1 = 0
# n2 = 1
# print(n1)
# print(n2)
# for i in range (2,num+1):
#     sum=n1+n2
#     print(sum)
#     n1 =  n2
#     n2 = sum



# for i in range (1,100):
#     for j in range (i):
#         print( " * " , end =" ")
#     print()


# for i in range (1,5):
#     print(f"week : {i}")
#     for j in range  (1,8):
#         print(f"day : {j}")



# for i in range (1,6):
#     for j in range (1,5):
#         print(f"{i*j:3}",end = " ")
#     print()



# #retangle
# for i in range (4):
#     for j in range (5):
#         print( "*", end="")
#     print()


# #coordinates
# for i in range (3):
#     for j in range (3):
#         print(f"({i},{j})",end=" ")
#     print()


# # pyramid patten
# num = int(input("enter the number : "))
# for i in range (1,num+1):
#     for j in range (num-i):
#         print( " " ,end=" ")
#     for k in range (2 * i - 1):
#         print ("*", end=" ")
#     print()


#dimond pattern
# #upper part of diamond
# num = int(input("enter the number : "))
# for i in range (1,num+1):
#      for j in range (num-i):
#          print( " " ,end=" ")
#      for k in range (2 * i - 1):
#          print ("*" , end=" ")
#      print()

# #lower part of the diamond
# for i in range (num-1,0,-1):
#     for j in range (num - i):
#         print(" ", end=" ")
#     for k in range (2 * i - 1):
#         print("*" , end=" ") 
#     print() 




#while loop

# while 1 ==1:
#     print("ASHOK" , end = " ")


# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1


# i = 2
# while i <=100:
#     print(i , end =" ")
#     i = i + 2


#first 5 number
# i = 1
# while i < 6:
#     print(i)
#     i = i + 1


# #reverse
# i=1000
# while i>20:
#     print(i,end=" ")
#     i=i-20
#     print()

#sum
# i = 1
# s = 0
# while  i <= 5:
#     s = s + i
#     i = i + 1
# print(s)



# n = int(input("enter the number : "))
# i = 1
# p = 0
# while i <= n:
#     p = n * i
#     i = i + 1
# print(p)


# # table in while loop
# n = int(input("enter the number : "))
# i = 1
# while i<=10:
#     print(f"{i} x {n} = {i*n}")
#     i = i + 1

# while True :
#     num = int(input("enter the number : "))
#     if num == 0:
#         print("exiting loop")
#         break
#     print(f"enter the num : {num} ")



# #reverse a string
# input_string = input("enter the string : ")
# reversed_string = " "
# index = len(input_string)-1
# while index >=0:
#     reversed_string +=input_string[index]
#     index = index - 1
# print(f" reversed string is : {reversed_string}")

#sum of digit of number
# num = int(input("enter the num : "))
# sum_digits = 0
# while num >0:
#     digit = num % 10
#     sum_digits = sum_digits + digit
#     num //=10
# print (f"sum of the digits is : {sum_digits}")


#sum of count of number
# num = int(input("enter the number : "))
# count = 0
# while num >0:
#     digit = num % 10
#     count = count + 1
#     num //=10
# print(f"sum of the digits is : {count}")


#fibonacci sequence
# n = int(input("enter the number : "))
# a = 0
# b = 1
# count = 0
# while count < n:
#     print(a)
#     a , b = b ,a + b
#     count = count +1


# #prime number
# num = int(input("enter the number : "))
# if num < 2:
#     print(f"{num} is not a prime number ")
# else:
#     is_prime = True
#     divisor = 2
#     while divisor <=num//2:
#         if num % divisor == 0 :
#             is_prime = False
#             break
#         else:
#             divisor +=1
#     if is_prime :
#         print(f"{num} is a prime number ")
#     else:
#         print(f"{num} is not a prime number")


#palindrome check
# input_string = input("enter the string : ")
# left = 0
# right = len(input_string)-1
# is_palindrome = True
# while left < right :
#     if input_string[left] != input_string[right]:
#         is_palindrome = False
#         break
#     left +=1
#     right -=1
# if is_palindrome:
#     print(f"{input_string} is a palindrone ")
# else:
#     print(f"{input_string} is not a palindrone")



# s = input("enter the string : ")
# a = s[:: -1]
# if (a==s):
#     print(f"{s} is a palindrome")
# else:
#     print(f"{s} is not a palindrone ")

#guess the random number
# import random
# secret_number = random.randint(1,10)
# guess = 0
# while guess != secret_number:
#     guess = int(input("guess the number (between 1-10) : "))
#     if guess < secret_number:
#         print(" too low ")
#     elif guess 


#function

# a = input("enterthe name : ")
# b = input("enter the password : ")
# def password(b):
#     if (b.lower() == "ashok118"):
#         return (f"hai {a} , the acess has been granted")
#     else:
#         return (f"sorry.....{a} , the access has denied")
# print(password(b))


# print lenth of the given input in function ?(user input)


# a = input("Please enter something: ")
# def length(a):
#     length = len(a)
#     return (f"The length of the input is: {length}")
# print(length(a))


# 



# def fun (movie , *desc , **details ):
#     print(movie)
#     print(*desc)
#     for key , value in details .items():
#         print(f"{key} : {value}")
# fun("mankatha" , "its" , "my" , "fav" , "movie" , chennel = "Ktv" , time = "7-10.30"  , genre = "action" )



#lambda

# def sum (a,b):
#     return a+b
# print(sum(2,3))

# x =  lambda a,b : a+b
# print(x(2,3))



# min = lambda a,b:a if a<b else b
# print(min(8,3))


# def  mul (l1):
#     l2 = []
#     for i in (l1):
#         l2.append(i*2)
#     return l2
# l1 = [2,4,6,8,]
# print(mul(l1))

# list comprehension
# n = [2,4,6,8]
# print([i*2 for i in n])


# def mul (l1):
#     l2 = l1[0]
#     for i in range (1,len(l1)):
#         l2 *= l1[i]
#     return l2
# print(mul([1,2,3,4]))
    




# import functools as ft
# n = [2,3,4,5]
# def fun (a,b):
#     return a*b
# print(ft.reduce(fun,n))


# import functools as ft
# n =[2,3,4,5]
# print(ft.reduce(lambda a,b : a*b,n))


#  oops function

# class moblie():
#     def details(self):
#         self.price = 0 
#         self.processor = ""
#         self.ram = ""
# mi = moblie()
# apple = moblie()
# mi.price = 50000
# mi.processor = "snapdrogan"
# mi.ram = "16"
# apple.price = 150000
# apple.processor = "ios"
# apple.ram = "none"
# print(mi.price)
# print(mi.processor)
# print(mi.ram)
# print(apple.price)
# print(apple.ram)
# print(apple.processor)




# class cartoon :
#     def __init__(self):
#         self.cartoon = ""
#         self.time = ""
#         self.gender = ""
#         self.chennal =""
#     def show(self):
#         print("show the content")
#         print(self.cartoon)
#         print(self.time)
#         print(self.gender)
#         print(self.chennal)

# ben10 = cartoon()
# droganbooster = cartoon()
# ben10.cartoon = ben10
# ben10.time = "8 to 10"
# ben10.gender = "kids"
# ben10.chennal = "cartoon network"
# droganbooster.cartoon = droganbooster
# droganbooster.time = "8 to 10"
# droganbooster.gender = "kids"
# droganbooster.chennal = "pogo"
# ben10.show()
# droganbooster.show()



# class laptop :
#     ram = "16gb"
#     def __init__(self,price,processor):
#         self.price = price
#         self.processor = processor
#     def show(self):
#         print(f"price={self.price}")
#         print(f"processor={self.processor}")
#         print(f"ram : {self.ram}")
# hp = laptop(50000 ,"i5")
# dell = laptop(80000 , "i7")
# dell.ram = "16gb"
# hp.show()
# dell.show()




# multiple  inheritance

# class bikes:
#     def pulsar(self):
#         print("its is pulsar 150 ")
#     def endfield(self):
#         print("it is himalaiyan 490")
# class cars:
#     def benz(self):
#         print("i have a benz")
#     def audi(self):
#         print("i dont have audi")
# class name (bikes , cars):
#     def ashok(self):
#         print("hai ,i am ashok ")
# ashok = name()
# ashok.ashok()
# ashok.endfield()
# ashok.benz()

# hierarchial inheritance

# class earbuds:
#     def noice (self):
#         print("i have noice earbuds")
#     def apple (self):
#         print("i dont have apple earbuds")
# class person1(earbuds):
#     pass
# class person2(earbuds):
#     pass
# class person3(earbuds):
#     pass
# ashok = person1()
# vimal = person2()
# ashok.noice()
# vimal.apple()


# hybird inheritance 

# class food():
#     def biriyani(self):
#         print("i like biriyani ")
#     def parotta (self):
#         print("i dont like parotta")
# class offer():
#     def discount (self):
#         print ("only biriyani has an offer")
# class person1(food):
#     pass
# class person2 (offer):
#     pass
# class person3(food,offer):
#     pass
# ashok = person1()
# vinith = person3()
# vimal = person2()
# ashok.biriyani()
# vinith.parotta()
# vimal.discount()
# off = offer()
# off.discount()


# super keyword

# class person1:
#     def __init__(self) -> None:
#         print("ashok")
#     def name(self):
#         print("name of the person :")
# class person2:
#     def __init__(self):
#         print ("kumar")
#         super().__init__()
# class person3:
#     def __init__(self):
#         print("kamaraj")
#         super().__init__()



# polymorphism

# def add(a,b):
#     print(a+b)
# add(10,40) 


# def add ( a=0 , b=0 , c=0 , d=0 , e=0 ):
#     print(a+b-c)
# add(10,20,30,40,50)


# def sub(a,b,c,d,e,f):
#     print(a+b+c-f)
# sub(10,20,30,40,50,10)
# sub(10,20,30,40,50,10)



# class cars():
#     def benz(self):
#         print("benz g cls")
#     def benz





# class person ():
#     def __init__(self,name):
#         self.name = name

# class collage (person):
#     def __init__ (self,grade,name):
#         self.grade = grade 
#         # self.name = name
#         super().__init__(name)

#     def show (self):
#         print(self.grade)
#         print(self.name)
        

# stud = collage("Ashok","A")
# stud.show()








# encapsulation 

# class identity():
#     def culture (self):
#         print("tamil")
# tamilnadu = identity()
# tamilnadu.culture()



# class identity():
#     def __init__(self):
#         self.culture ="tamil"
# tamilnadu = identity()
# print(tamilnadu.culture)



# private

# class identity ():
#     def __init__(self):
#         self.__culture ="tamil"
# tamilnadu = identity()
# print(tamilnadu.__culture)


# class identity():
#     def __init__ (self):
#         self.__culture ="tamil"
#     def culture(self):
#         print(self.__culture)
# tamilnadu = identity()
# tamilnadu.culture()


# protected

# class identity():
#     def __init__(self):
#         self.__culture = "tamil"
# tamilnadu = identity()
# tamilnadu._culture = "english"
# print(tamilnadu._culture)


# class identity ():
#     def __init__(self):
#         self._culture = "tamil"
# class sample(identity):
#     pass



#  collage 
# id
# Name
# Dept
# batch







class  collage :
    def __init__(self) :
        self.student = {} 

#addimg students
def add_stud(self, stud_id , name , dept , batch ):
    if stud_id in self.student :
        print("employee id already exists")
    else:
        self.student [stud_id] = { "name" : name , "dept" : dept , "batch" : batch}
    print("student added successfully")

#to update details of student

def update_stud( self , stud_id , name = None , dept = None , batch = None):
    if stud_id in self.student :
        if name :
            self.student [stud_id]["name"] = name
        if dept :
            self.student [stud_id]["dept"] = dept
        if batch :
            self.student [stud_id]["batch"] = batch
        print("student details update successfully")
    else:
        print("stud_id not founded")





























































































 




























































    































