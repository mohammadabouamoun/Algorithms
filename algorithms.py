def factorial(n):# time complexity : O(n)

  result = 1
  if n < 0 :
     return "Factorial is not used for negative numbers."
  while n > 0 :#  while loop O(n) 
     result *= n 
     n = n-1 
  return result 
#  print(factorial(0))
#  print(factorial(5))
#  print(factorial(-4))

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////
# time complexity : O(n)
def find_max(numbers):
    max_num = numbers[0]
    for i in  numbers :
      if max_num < i :
        max_num = i 

    return max_num

# maximum = find_max([2,4,34,54,65,743,4,1,2])
# print(maximum)

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////

# time complexity : O(n)

def linear_search(numbers, x):
   for i in numbers: #  for loop O(n) 
         if i == x :  # if statement O(1)
          return True
   return False
# print(linear_search([2,23,43,5,23,1,24,3],6))      
# print(linear_search([2,23,43,5,23,1,24,3],5))     

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////


# time complexity : O(n)
def fibonacci(n):
  a = 1
  b = 0
  for i in range(n):#  for loop O(n)
     add = a + b 
     b = a 
     a = add 
  return b
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(5 ))

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////


# time complexity : O(n)
def rec_fibonacci(n, a =0,b=1 ):
   if n ==0 : # if statement O(1)
    return a
   if n ==1 :# if statement O(1)
    return b
   if n > 0 :   # if statement O(1)
      inc = a+b 
   return rec_fibonacci(n-1, a = b , b = inc )# calling the function O(n)
 
# print(rec_fibonacci(6))   

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////


# time complexity : O(1)
def login() :
   username = input(" please enter username ")
   password = input("please enter the password ")
   if username == "admin123" and password == "123456789" :
      print("you have succesfully logged in ")
      return True
   else:
        print("Invalid username or password.")
        return False

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////

loggedin = False
while True :


 print('''     
    Choose an option:
  1. Factorial
  2. Find Max
  3. Linear Search
  4. Fibonacci
  5. Login
  6. Exit
  ''')
 user_input= input("please choose an option  (remember to  login  first)")

 if user_input == "1" :
   if  loggedin == False :
      print("you should login first")
   else :
    ask = input("please give a number ")
    print("the factorial number of",ask,"is", factorial(int(ask))) 


 if user_input == "2" :
   if  loggedin == False :
      print("you should login first")
   else:   
    Numbers = []
    while True :
      ask1 = input("enter the numbers of the list one by one.(write done when you finish the numbers)").strip()
      if ask1 == "done":
        break 
      else : 
         Numbers.append(int(ask1))
    find_max(Numbers)    
    print("the maximum number in the list is ",find_max(Numbers) )  
  
  
   

 if user_input == "3" :
   if  loggedin == False :
      print("you should login first")

   else:   
     Number = [2,4,5,6,67,7,3,4,5,64,61]
     
     target = int(input("please give the number you are searching for inside the list"))
     print(linear_search(Number,target))


 if user_input == "4" :
   if  loggedin == False :
      print("you should login first")
   else:
    ask = input( "please give a number ")   
    print(fibonacci(int(ask)))


 if user_input == "5":
   if not loggedin :
           loggedin =  login() 
   else:
      print("you are already logeedin")        
   
 if user_input == "6" :
   break