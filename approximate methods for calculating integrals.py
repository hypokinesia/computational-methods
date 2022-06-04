import math

def Simpson(y, h):
    res = (2*h)/6
    n = len(y)-1
    s = 0
    for i in range(len(y)):
        if i==0: s+=y[0][1]
        elif i==n: s+=y[n][1]
        elif i%2!=0: s+=4*y[i][1]
        elif i%2==0: s+=2*y[i][1]
    return (round(res*s, 3))

def rectangle(h, y):
    s = 0
    for i in range(len(y)-2):
        s += y[i][1]
    return(round(h*s, 3))

def trapezoid(h, y):
    s = (y[0][1]+y[len(y)-1][1])/2
    for i in range(len(y)-1):
        if i==0: continue
        else:
            s+=y[i][1]
    return(round(h*s, 3))
def func(x):
    y = math.sin(3*x)*math.sin(5*x)
    return round(y,3)

a = 0
b = 1.4
h = 0.2
y = []
while a<=b:
    a = round(a,1)
    n = []
    n.append(a)
    n.append(func(a))
    y.append(n)
    a = a+h
print(y)
print(Simpson(y,h))
print(rectangle(h, y))
print(trapezoid(h, y))
