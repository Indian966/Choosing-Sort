def gcd1(a, b):
   if a<b :
      a,b = b,a
   while b>0:
      a,b = a-b, b
      if a<b :
         a,b = b,a
   return a

def gcd2(a,b) :
   while b>0 :
      a,b = b, a%b
   return a

def gcd3(a,b) :
   while b>0 :
      a,b = b, a%b
      gcd3(a,b)
   return a

print( gcd1(12, 28) )
print( gcd2(12, 28) )
print( gcd3(12, 28) )