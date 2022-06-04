import math
x = [3.48, 5.49, 7.50, 9.51, 11.52, 13.53]
y = [-0.05, 2.00, 4.85, 5.83, 3.95, 5.55]

def riz(y):
    res = []
    m = []
    m = y
    for i in range(len(y)-1):
        l = []
        for i in range(len(m)):
            if i == 0: continue
            else: l.append(round(m[i]-m[i-1], 3))
        m = l
        res.append(m)
    return res

def rid_one(x, y, res):
    n = 1
    h = x[1]-x[0]
    Sres = ''
    for i in res:
        k = round(i[0]/(math.factorial(n)*pow(h, n)),3)
        if k<0:Sres = Sres + str(k)
        else: Sres = Sres + '+' + str(k)
        for j in range(n):
            Sres += '(x - ' + str(x[j])+')'
        n=n+1
    return Sres

def rid_two(x, y, res):
    n = 1
    h = x[1]-x[0]
    Sres = ''
    o = len(x)-1
    for i in res:
        k = round(i[len(i)-1]/(math.factorial(n)*pow(h, n)),3)
        if k<0:Sres = Sres + str(k)
        else: Sres = Sres + '+' + str(k)
        on = o
        for j in range(n):
            Sres += '(x - ' + str(x[on])+')'
            on = on-1
        n=n+1
    return Sres

res = riz(y)
print('Розділені різниці:'+str(res))
print('Поліном першого роду:')
print(str(y[0])+' '+str(rid_one(x, y, res)))
print('Поліном другого роду:')
print(str(y[len(y)-1])+' '+str(rid_two(x, y, res)))
x = 9.51
print(-0.05 +1.02*(x - 3.48)+0.099*(x - 3.48)*(x - 5.49)-0.055*(x - 3.48)*(x - 5.49)*(x - 7.5))
print(5.55 +0.796*(x - 13.53)+0.431*(x - 13.53)*(x - 11.52))
