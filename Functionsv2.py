
import numpy as np
import matplotlib.pyplot as plt

def semiExplicitEuler(dthetadt,dPthetadt, F0, dt, tf):

    t = np.arange(0, tf + dt, dt) # Numerical grid
    theta = np.zeros(len(t))
    Ptheta = np.zeros(len(t))
    theta[0] = F0[0]
    Ptheta[0] = F0[1]
    for i in range(1,len(t)):
        theta[i] = theta[i-1] + dt*dthetadt(t[i-1],Ptheta[i-1])
        Ptheta[i] = Ptheta[i-1] + dt*dPthetadt(t[i-1],theta[i])

    return Ptheta, theta, t

def ImplicitEuler(F, F0, dt, tf):

    t = np.arange(0, tf + dt, dt) # Numerical grid
    S = np.zeros(len(t))
    S[0] = F0

    for i in range(1,len(t)):
        S[i] = S[i-1] + dt*F(S[i],t[i])

    return t, S
    
# Define parameters
f = lambda t, s: s+ np.exp(-t) # ODE
dt = 0.01 # Step size
t = 1
s0 = -1 # Initial Condition


def hamiltonian():
    omega = 9.80665 # Frequency m/s^2

    # Hamiltonian equations
    dthetadt = lambda t, Ptheta: Ptheta
    dPhetadt = lambda t, theta: -np.sin(theta)*omega 
    return dthetadt, dPhetadt

F0 = np.array([np.pi/4, 0]) # Initial conditions
dt = 0.01 # Step size
t = 100 # Final time

dthetadt,dPhetadt = hamiltonian()
Ptheta, theta, t = semiExplicitEuler(dthetadt, dPhetadt, F0, dt, t)

# t, sol = ExplicitEuler(f, s0, dt, t)

# print()
plt.plot(Ptheta, theta)
plt.show()


# def ImplicitEuler():