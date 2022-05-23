""" proj1-2_potential_well.py - bound energy in potential well Joonha Kim """
import numpy as np
from bisection_module import bisection
def f_even(x):
    return(np.tan(x)-(np.sqrt(Clambda - x*x))/x)
def f_odd(x):
    return(1./np.tan(x)+(np.sqrt(Clambda - x*x))/x)

Clambda = 25.*np.pi*np.pi/4.  # lambda

j = 0
x= []
energy = []

while True:
    print(j,x)
    if j%2 == 0:
        if j != 0 and (Clambda - (j*np.pi/2)**2) <=0:
            break
        x += bisection(f_even, xL = 0.01 + j*np.pi/2, h=0.01)
        energy.append(x[j]**2/Clambda-1)
        
    else:
        if j !=0 and (Clambda - (j*np.pi/2)**2) <= 0:
            break
        x += bisection(f_odd,  xL = 0.01 + j*np.pi/2, h=0.01)
        energy.append(x[j]**2/Clambda-1)
    j += 1

for j in range(len(energy)):
    print("%dth bound energy=%.5f" % (j, energy[j]))