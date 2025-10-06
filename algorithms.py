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