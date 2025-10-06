def factorial(n):

  result = 1
  if n < 0 :
     return "Factorial is not used for negative numbers."
  while n > 0 :
     result *= n 
     n = n-1 
  return result 
#  print(factorial(0))
#  print(factorial(5))
#  print(factorial(-4))



def find_max(numbers):
    max_num = numbers[0]
    for i in  numbers :

      if max_num < i :
        max_num = i 

    return max_num

# maximum = find_max([2,4,34,54,65,743,4,1,2])
# print(maximum)
 
def linear_search(numbers, x):
   for i in numbers:
      if i == x :
         return True
   return False
# print(linear_search([2,23,43,5,23,1,24,3],6))      
# print(linear_search([2,23,43,5,23,1,24,3],5))     


def fibonacci(n):
  a = 1
  b = 0
  for i in range(n):
     add = a + b 
     b = a 
     a = add 
  return b
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(5 ))



def rec_fibonacci(n, a =0,b=1 ):
 
   if n ==0 : 
    return a
   if n ==1 :
    return b
   if n > 0 :   
      inc = a+b 
   return rec_fibonacci(n-1, a = b , b = inc )
 
# print(rec_fibonacci(6))   