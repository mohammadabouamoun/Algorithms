def factorial(n):

 result = 1
 if n < 0 :
    return "Factorial is not used for negative numbers."
 while n > 0 :
    result *= n 
    n = n-1 
 return result 
# print(factorial(0))
# print(factorial(5))
# print(factorial(-4))

 
    