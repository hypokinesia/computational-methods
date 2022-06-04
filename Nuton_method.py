import math
def myFunc(x):
    ##return math.sqrt(x+1)-(1/x)
    return 3*x-math.cos(x)-1
    ##return math.exp(2*x)+3*x-4

def myDef(x):
    ##return math.sqrt(x+1)-(1/x)
    return 3+math.sin(x)
    ##return 3-2*math.exp(x)

e = float(input())
x = float(input())
st=""
while True:
    y = myFunc(x)
    y_def = myDef(x)
    x_k = -1*y/y_def
    st+=str(round(x,6))+" "+str(round(y,6))+" "+str(round(y_def,6))+" "+str(round(x_k,6))+"\n"
    x1 = x+x_k
    if abs(x1-x)<e: break
    x=x1

print(round(x,4))
print(st)

