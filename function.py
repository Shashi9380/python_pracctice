# def add (num1,num2):
#     out = num1+num2
#     return out
# out1=add(1,2)
# print(out1)

# def add (num1,num2):
#     out = num1+num2
#     if out==100:
#         return "100"
#     return 
# out1=add(50,50)
# print(out1)

# def add2numbers(num1,num2):
#     sum=num1+num2
#     return_var=sum
#     if sum==0:
#         return_var=100
#     return return_var
# out=add2numbers(0,0)
# print(out)


# def maths(num1,num2):
#     return(num1+num2,num1-num2,num1*num2,num1/num2)
# add,sub,mul,div=maths(6,3)
# print(add,sub,mul,div)

# def greatestof3(a,b,c):
#     if a>b and a>c:
#         print(f"a is greater{a}")
#     elif b>a and b>c:
#         print(f"b is greter{b}")
#     else:
#         print(f"c is greter {c}")

# input1=int(input("enter the value input1"))
# input2=int(input("enter the value input2"))
# input3=int(input("enter the value input3"))
# greatestof3(input1,input2,input3)

# def fact(num1):
#     out=1
#     while num1:
#         out *= num1
#         num1 -=1
#     return out
# fact1=fact(5)
# print(fact1)

# def fact(num):
#     out=1
#     for i in range(1,num+1):
#         out *= i
#     return out
# fact1=fact(4)
# print(fact1)

# def fact(num):
#     out=1
#     for i in range(num,0,-1):
#         out *= i
#     return out
# fact1=fact(4)
# print(fact1)



# postion argument =====>
# ---------------------------
# def pointDetails(fn,ln,age):
#     print(f"hey i am {fn+ln}and my age is {age}")
# pointDetails("shashi","kiran",30)

#named argument========>
#--------------------------
# def pointDetails(fn,ln,age):
#     print(f"hey i am {fn+ln}and my age is {age}")
# pointDetails("shashi",age=30,ln="kiran",)

#default argument=======>
#------------------------
# def pointDetails(fn,ln="kohile",age=36):
#     print(f"hey i am {fn+ln}and my age is {age}")
# pointDetails("shashi",age=30)
                   
# def calSum(*num):
#     print(sum(num))
# calSum(1,2,3,4,5,6)
#      or


# def calsum(*num):
#   out=""
#   for data in num:
#     out +=str(data)
#   print(out)
# calsum("shashi","kiran","3","4")

# lst1=[]
# def addsomething(data):
#     coutry_list=["india"]
#     data=coutry_list
# addsomething(lst1)
# print(lst1)

# lst1=[]
# def addsomething(data):
#     lst1.extend(["india","pak"])
    #   data=["india","pak"]
    #   list.extend(data)
    
# addsomething(lst1)
# print(lst1)

# lst1=[["india"],"pak"]
# def addsomething(data):
#     data1=data.copy()
#     data1[0].append("india")
#     print(data1)
#     print(id(data1),id(data.copy()))
# addsomething(lst1)
# print(lst1)
# print(id(lst1))

# lst1=[]
# def addsomething(data):
#     data.append("india")
# addsomething(lst1.copy())
# print(lst1)

# x=100
# def value1():
#     print(x)
# def value2():
#     global x
#     x=10
#     print(x)
# def value3():
#     print(x+1)
# value1()
# value2()
# value3()
# print(x)

# def outer():
#     x=10
#     def inner():
#         print(x)
#     inner()
# outer()

# def outfu():
#     def innerfu():
#         return 100
#     return innerfu()
# out=outfu()
# print(out)


# def func1():
#     print("older")
# def main():
#     func1()
#     print("in the middle of main function")
#     func1()
# def func1():
#     print("older")
# main()


# def main():
#     x=30
#     def func1():
#       nonlocal x
#       x=10
#       print(x)
#     func1()
#     print(f"the value of x is {x}")
# main()

# def main():
#     x=30
#     def func1():
#     #   nonlocal x
#     #   x +=10
#         print(x)
#     func1()
#     print(f"the value of x is {x}")
# main()

# x=100
# def main (x):
#     y=100
#     def func1():
#         global x
#         nonlocal y
#         x=x+y
#         print (x)
#     func1()
# main(10)
# note:- we canot use global and nonlocal for same value for different vslue we can use




