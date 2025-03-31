
import numpy as np
import matplotlib.pyplot as plt

def ExplicitEuler(F, F0, dt, tf):

    t = np.arange(0, tf + dt, dt) # Numerical grid
    S = np.zeros(len(t))
    S[0] = F0

    for i in range(1,len(t)):
        S[i] = S[i-1] + dt*F(S[i-1],t[i-1])

    return t, S

def ImplicitEuler(F, F0, dt, tf):

    t = np.arange(0, tf + dt, dt) # Numerical grid
    S = np.zeros(len(t))
    S[0] = F0

    for i in range(1,len(t)):
        S[i] = S[i-1] + dt*F(S[i],t[i])

    return t, S
    
# Define parameters
f = lambda t, s: s+ np.exp(-t) # ODE
dt = 0.1 # Step size
t = 1
s0 = -1 # Initial Condition


t, sol = ExplicitEuler(f, s0, dt, t)

print(sol)
plt.plot(t, sol)
plt.show()


# def ImplicitEuler():