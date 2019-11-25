#1
def printStars(a):
  for i in range(1,a):
    print("+"*i)
a = int(input("Enter a size:"))    
printStars(a)    

#2
def leap(n):
  if n % 100 == 0 and n % 400 != 0:
    return False
  elif n % 4 == 0:
    return True  
  else:
    return False
print(leap(int(input())))      

#3 
def factorial(n):
  if  n < 0:
    return "Factorial does not exist for negative numbers"
  elif  n == 0:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(int(input())))    

#4
def factorial(i):
  if i == 0:
    return 1 
  else:
    return i * factorial(i-1)           
def sum(n): 
    sumnum = 0.0
    for i in range(n): 
        sumnum += 1.0 / factorial(i) 
    print(sumnum) 
n = 10
sum(n) 
 
#5
def getMax(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    return max(lst[0],getMax(lst[1:]))  
a = int(input())
b = int(input())
c = int(input())
lst = [a,b,c]
print(getMax(lst))

#6
def outer(x):
  def inner(y):
    return x + y
  return inner
x = outer(3)
print x(4)

#SyntaxError occured. Invalid syntax

#7
def gg():
  number = 1
  return number
number = 2 * gg() 
print(number)

#even though same variables , since they are in different scopes there is no interconnection between them.     



