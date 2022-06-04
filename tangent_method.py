import math
def myFunc(x):
    return 3*x-2*math.exp(x)+2
    ##return math.exp(2*x)+3*x-4

e = float(input())
x = float(input())
x1 = float(input())
st=""
while True:
    if abs(x1-x)<=e: break
    y = myFunc(x)
    st+=str(round(x,4))+" "+str(round(y,4))+"\n"
    y1 = myFunc(x1)
    x2 = (x*y1-x1*y)/(y1-y)
    x=x1
    x1=x2

print(round(x1,4))
print(st)
