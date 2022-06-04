import math
def myFunc(x):
    ##return 3*x-2*math.exp(x)+2
    ##return math.exp(2*x)+3*x-4
    ##e = math.e
    ##return math.log(((3*x+2)/2), e)
    try: return (-1*math.cos(x)-1)/3
    except: return 0
    ##return math.log((4-3*x),e)/2

e = float(input())
x = float(input())
st=""
n = 1
while True:
    y = myFunc(x)
    st+=str(round(x,4))+" "+str(round(y,4))+"\n"
    if abs(y-x)<=e: break
    if n==50: break
    n+=1
    x = y

print(round(x,4))
print(st)

