a = float(input("Enter the first number: "))
b = float(input("Enter the second number:  "))

def sum(x,y):
   s = a + b
   return s

def diff(x,y):
   d = a - b
   return d

def prod(x,y):
   p = a * b
   return p

def quo(x,y):
   if b == 0:
      q = "Undefined"
   else: 
      q = a/b
   return q

print(a, "+", b, "=", sum(a,b))
print(a, "-", b, "=", diff(a,b))
print(a, "*", b, "=", prod(a,b))
print(a, "/", b, "=", quo(a,b))
