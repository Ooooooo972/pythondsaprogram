n=56879

num=n
count=0
while num>0:
  digit=num%10
  count=count+1
  num=num//10
print("The number of digits in",n,"is",count)