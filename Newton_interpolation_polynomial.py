mass_x = [3.48, 6.55, 7.05, 8.25, 10.05, 12.25, 9.50]
mass_y = [-0.05, 2, 4.85, 5.83, 3.95, 5.55, 7.24]

def Nuton(x,y):
    n = 6
    m = y
    result = []
    count = 1
    c_new = 1
    for i in range(n):
        Scount = count
        l = []
        for i in range(len(m)-1):
            r = (m[i+1]-m[i])/(x[Scount] - x[count-c_new])
            r = round(r, 3)
            Scount+=1
            l.append(r)
        m = l
        result.append(m)
        count+=1
        c_new+=1
    res = ''
    print(result)
    for i in range(len(result)):
        if result[i][0]>0 and i!=0:resc = "+" + str(result[i][0])+'*'
        else: resc = str(result[i][0]) + '*'
        for j in range(i+1):
            if x[j]>0: resc+="(x - " + str(x[j]) +")"
            else: resc+="(x + " + str(abs(x[j])) +")"
        res+=resc
    return(res)
def Lagrange(x, y):
    result = ''
    for i in range(len(y)):
        s = 1
        for j in range(len(x)):
            if j == i:
                continue
            else:
                s = s*(x[i]-x[j])
        n = round(y[i]/s, 10)
        chis=''
        for j in range(len(x)):
            if j == i:
                continue
            else:
                if x[j]<0:
                    chis=chis+" (x +" + str(abs(x[j]))+')'
                else:
                    chis=chis+" (x -" + str(abs(x[j]))+')'
        result = result + str(n)+"*"+chis
    return result

print(Lagrange(mass_x, mass_y))
print(Nuton(mass_x, mass_y))
x = 7.05
print(0.0592422561*(x -3.48)*(x -6.55)*(x -8.25)*(x -10.05)*(x -12.25)*(x -9.5))
print(2*0.668*(x - 3.48)+0.036*(x - 3.48)*(x - 6.55)*2)
