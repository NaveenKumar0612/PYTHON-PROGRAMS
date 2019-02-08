#ArmStrong
n=int(input())
c=list(map(int,str(n)))
d=list(map(lambda x:x**3,c))
if(sum(d)==n):
    print("yes")
else:
    print("no")
