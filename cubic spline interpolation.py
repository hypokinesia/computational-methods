x = [6.25, 12.32, 15.75, 17.98, 24.04, 34.11]
y = [5.55, 7.77, 8.88, 6.67, 3.83, 1.61]

def mass_h(x):
    h = []
    for i in range(len(x)):
        if i == len(x)-1: continue
        else:
            h.append(round(x[i+1]-x[i],3))
    return h

def mass_u(h):
    u = []
    for i in range(len(h)):
        if i == 0: continue
        else:
            u.append(h[i])
    print(h)
    print(u)
    return u

def mass_w(h):
    w = []
    for i in range(len(h)):
        if i == len(h)-1: continue
        else:
            w.append(h[i])
    print(w)
    return w

def mass_v(u, w):
    v = []
    for i in range(len(u)):
        v.append((-2)*(u[i]+w[i]))
    print(v)
    return v

def mass_F(y, h):
    F = []
    for i in range(len(h)-1):
        n_1 = (y[i+2]-y[i+1])
        n_2 = (y[i+1]-y[i])
        n_1 = n_1/h[i+1]
        n_2 = n_2/h[i]
        F.append(round(3*(n_1-n_2), 3))
    print(F)
    return F

def syst(w, v, u, F):
    print("маємо систему:")
    c = 1
    for i in range(len(w)):
        print(str(w[i])+'*c'+str(c)+'+'+str(abs(v[i]))+'*c'+str(c+1)+'+'+str(h[i])+'*c'+str(c+2)+'='+str(F[i]))
        c=c+1
def mass_A(u, v, w):
    mass_a=[]
    mass_a.append(round(u[0]/v[0], 3))
    n=0
    for i in range(len(u)):
        if i<1: continue
        mass_a.append(round(u[i]/(v[i]-w[i]*mass_a[n]), 3))
        n=n+1
    print(mass_a)
    return mass_a

def mass_B(u, v, w, A, F):
    mass_b=[]
    mass_b.append(round(-1*F[0]/v[0], 3))
    print(str(-1*F[0])+'/'+str(v[0]))
    n=0
    for i in range(len(u)):
        if i<1: continue
        mass_b.append(round((w[i]*mass_b[n]-F[i])/(v[i]-w[i]*A[i-1]), 3))
        n=n+1
    print(mass_b)
    return mass_b

def mass_c(a, b):
    c = []
    c.append(b[len(b)-1])
    n = len(b)-2
    for i in range(len(a)-1):
        try: c.append(round(a[n]*c[i]+b[n], 3))
        except: continue
        n=n-1
    i = len(c)-1
    c_new =[]
    c_new.append(0)
    while i>=0:
        c_new.append(c[i])
        i=i-1
    c_new.append(0)
    return c_new

h = mass_h(x)
print('h = ' + str(h))
u = mass_u(h)
print('u = ' + str(u))
w = mass_w(h)
print('w = ' + str(w))
v = mass_v(u, w)
print('v = ' + str(v))
F = mass_F(y, h)
print('F = ' + str(F))
syst(w, v, u, F)
a = mass_A(u, v, w)
print('A = ' + str(a))
b = mass_B(u, v, w, a, F)
print('B = ' + str(b))
c = mass_c(a,b)
print('c = ' + str(c))
a_n = y
b_n = []
for i in range(len(c)-1):
    n_1 = (1/h[i])*(y[i+1]-y[i])
    n_2 = (1/3)*(2*c[i]+c[i+1])*h[i]
    b_n.append(round((n_1-n_2), 3))
d_n = []
for i in range(len(c)-1):
    d_n.append(round((c[i+1]-c[i])/(3*h[i]),3))
print('a = ' + str(a_n))
print('b = ' + str(b_n))
print('d = ' + str(d_n))
print(c)
print(x)
for i in range(len(a_n)-1):
    print(i)
    print(str(a_n[i])+'+'+str(b_n[i])+'*(x-'+str(x[i])+')'+'+'+str(c[i])+'*(x-'+str(x[i])+')^2'+'+'+str(d_n[i])+'*(x-'+str(x[i])+')^3')
