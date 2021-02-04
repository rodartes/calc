#This is identical to calculator.py but it only contains functions for testing

def sum(x,y):
   s = x + y
   return s

def diff(x,y):
   d = x - y
   return d

def prod(x,y):
   p = x * y
   return p
			 
def quo(x,y):
   if y == 0:
      q = "Undefined"
   else:
      q = x/y
   return q


