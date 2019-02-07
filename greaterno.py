c=int(input())
b=int(input())
a=int(input())
if(c>b and c>a):
  print(c)
elif(b>a and b>c):
  print(b)
elif(a>c and a>b):
  print(a)
else:
  print("INVALID")
