import math
def myFunc(x):
    ##return math.sqrt(x+1)-(1/x)
    return 3*x-2*math.exp(x)+2
    ##return math.exp(2*x)+3*x-4

e = float(input())
aO = float(input())
bO = float(input())
st=""
while True:
    c = (aO+bO)/2
    fA = myFunc(aO)
    fB = myFunc(bO)
    fC = myFunc(c)
    st+=str(round(aO,3))+" "+str(round(bO,3))+" "+str(round(fA,3))+" "+str(round(fB,3))+" "+str(round((aO+bO)/2,5))+' '
    if(fA*fC<0):
        bO = c
    else:
        aO = c
    st+=str(round(myFunc((bO+aO)/2),6))+"\n"
    if ((bO-aO)<2*e):
        print("x=" + str((bO+aO)/2))
        break
    
print(st)
