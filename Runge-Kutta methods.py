import math


def func_x(x, y, t):
    return math.exp(-2*t*t)+y


def func_y(x, y, t):
    return math.exp(-2*t*t)-x


def func_one(x, y, h):
    t = 0
    while t<=10:
        if x>0: x_n = ' ' +str(round(x,3))
        else: x_n = str(round(x,3))
        if y>0: y_n = ' ' +str(round(y,3))
        else: y_n = str(round(y,3))
        if int(t*10) % 5 == 0: print('t = '+str(round(t, 3)) + ' x = '+x_n + ' y = ' + y_n)
        t = round(t, 1)
        x = x + h * (func_x(x, y, t))
        y = y + h * (func_y(x, y, t))
        t += 0.1


def func_two(x, y, h):
    t = 0
    while t <= 10:
        if int(t*10) % 5 == 0: print('t = '+str(round(t, 3)) + ' x = '+str(round(x,3)) + ' y = ' + str(round(y, 3)))
        t = round(t, 1)
        x_n = x + h / 2
        y_n = y + (h / 2) * func_y(x, y, t)
        x = x + h * (func_x(x_n, y_n, t))
        y = y + h * (func_y(x_n, y_n, t))
        t += 0.1


def func_three(x, y, h):
    t = 0

    while t <= 10:
        if int(t*10) % 5 == 0: print('t = '+str(round(t, 3)) + ' x = '+str(round(x,3)) + ' y = ' + str(round(y, 3)))
        k1_x = func_x(x, y, t)
        k1_y = func_y(x, y, t)
        k2_x = func_x(x+2/3*h*k1_x, y+2/3*h*k1_y, t+2/3*h)
        k2_y = func_y(x+2/3*h*k1_x, y+2/3*h*k1_y, t+2/3*h)
        k3_x = func_x(x - h * k1_x + h * k2_x, y - h * k1_y + h * k2_y, t)
        k3_y = func_y(x+1/2*h*k2_x, y+1/2*h*k2_y, t)

        x_n = 3/4 * k2_x + 1/4 * k3_x
        y_n = 3/4 * k2_y + 1/4 * k3_y
        t += 0.1
        t = round(t, 1)
        x = x + h * x_n
        y = y + h * y_n


def func_four(x, y, h):
    t = 0
    while t <= 10:
        if int(t*10) % 5 == 0: print('t = '+str(t) + ' x = '+str(round(x,3)) + ' y = ' + str(round(y, 3)))
        k1_x = func_x(x, y, t)
        k1_y = func_y(x, y, t)
        k2_x = func_x(x+1/2*h*k1_x, y+1/2*h*k1_y, t+1/2*h)
        k2_y = func_y(x+1/2*h*k1_x, y+1/2*h*k1_y, t+1/2*h)
        k3_x = func_x(x+1/2*h*k2_x, y+1/2*h*k2_y, t+1/2*h)
        k3_y = func_y(x+1/2*h*k2_x, y+1/2*h*k2_y, t+1/2*h)
        k4_x = func_x(x+h*k3_x, y+h*k3_y, t+h)
        k4_y = func_y(x+h*k3_x, y+h*k3_y, t+h)
        t += 0.1
        t = round(t, 1)
        x = x + 1 / 6 * h * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        y = y + 1 / 6 * h * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
x = 0
y = 0
h = 0.1
func_one(x, y, h)
print('########################')
func_two(x, y, h)
print('########################')
func_three(x, y, h)
print('########################')
func_four(x, y, h)
