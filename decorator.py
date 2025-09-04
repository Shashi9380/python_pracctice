# def greet():
#     return "hello all"

# def wish():
#     return "happy morning"

# def main(f):
#     out=f()
#     print(out)
# main(greet)
# main(wish)


# def loggedin(func):
#     def wrapper():
#         print("checking authenticate")
#         func()
#         print("executing completed")
#     return wrapper
# @loggedin
# def checkwishlist():
#     print("your wishlist")
# @loggedin
# def checkorder():
#     print("your order")
# checkwishlist()
# checkorder()


# def loggedin(func):
#     def wrapper(*args):
#         print("checking authentication")
#         func(*args)
#         print("checking completed")
#     return wrapper
# @loggedin
# def checkwishlist(num1):
#     print("your whishlist")
# checkwishlist(2)

# import time
# def time_date(func):
#     def wrapper(*args):
#         start_time=time.time()
#         func(*args)
#         end_time=time.time()
#         print(f"time for execution==>{end_time-start_time}")
#     return wrapper
# @time_date
# def addition(num1,num2):
#     print(f"sum of two numer {num1+num2}")
# @time_date
# def subtraction(num1,num2):
#     if num1 > num2:
#         print(f"{num1-num2}")
#     else:
#         print("num1 should greater then num2")
# @time_date
# def factorial(num1):
#     out=1
#     for i in range(1,num1+1):
#         out *= i
        
#     print(out)    
    
# addition(10,11)
# subtraction(3,1)
# factorial(5)



    





