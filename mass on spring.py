import matplotlib.pyplot as plt

# Net force and Newton's Second Law

def acc(f_1, f_2, m):
    f_net = f_1-f_2
    acc = f_net/m
    return acc

# Hooke's Law

def f_spring(k, x):
    f_spring = -(k*x)
    return f_spring

# One dimanetional motion equations

def velo(u, a, t):
    v = u+(a*t)
    return v

def displacement(u, a, t):
    s = (u*t)+(0.5*a*(t**2))
    return s


# Simulating motion of mass hung from spring

def simulate(m, g, k, t_gap, duration, L):
    f_g = m*g
    x = 0
    a = f_g
    u = 0
    t_elapsed = 0
    x_total = 0
    length_total = [L]
    li_time = [0]
    while t_elapsed < duration:
        t_elapsed += t_gap # elapsed time increases by a little bit
        li_time.append(t_elapsed)
        v_now = velo(u, a, t_gap) # we consider motion in uniform acceleration for that short time, using previous net acceleration
        x = displacement(u, a, t_gap) # displacement during that time (again, considering no change in acceleration during that short time)
        x_total += x
        length_total.append(L+x)
        u = v_now
        a = acc(f_g, (k*x_total), m) # net acceleration calculated again for improvement
    
    return length_total, li_time

m = 100
g = 9.8
k = 5
t_gap = 0.01
duration = 200
L = 10
length_total = simulate(m, g, k, t_gap, duration, L)[0]
li_time = simulate(m, g, k, t_gap, duration, L)[1]

plt.plot(li_time, length_total) # Plotting the result (time in x axis, position of mass in y axis)