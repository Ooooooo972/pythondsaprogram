def primeno(n):
  if n>1:
    for i in range(2,n):
      if(n%i==0):
        return False
    return True
  else:
    return False
  
n=int(input("Enter a number: "))

if primeno(n):
  print(n,"is a prime number")  
else:  print(n,"is not a prime number")