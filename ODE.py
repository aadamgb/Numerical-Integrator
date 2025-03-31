import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

## INITIAL CONDITIONS ##
# Physical Parameters
m = 1
l = 1
g = 9.81
omega = np.sqrt(g/l)
theta0 = np.pi/4
ptheta0 = 0

# Simulation Parameters
tf = 10
dt = 0.01
t_span = np.arange(0, dt + tf, dt)


# Defining Pendulum Hamiltionian
def PendEq():
    dthetadt = lambda t, ptheta: ptheta / (m*l**2)
    dpthetadt = lambda t, theta: -m*l**2*omega**2*np.sin(theta)
    F0 = [theta0, ptheta0]
    return dthetadt, dpthetadt, F0


# Explicit Method Integrator
def ExplicitEuler(f1, f2, F0, t):
    N = len(t)
    s1 = np.zeros(N)
    s2 = np.zeros(N)
    s1[0] = F0[0]
    s2[0] = F0[1]

    for i in range(N-1):
        s1[i+1] = s1[i] + dt * f1(t[i], s2[i])
        s2[i+1] = s2[i] + dt * f2(t[i], s1[i])
    return s1, s2

def SemiImplicitEuler(f1, f2, F0, t):
    N = len(t)
    s1 = np.zeros(N)
    s2 = np.zeros(N)
    s1[0] = F0[0]
    s2[0] = F0[1]

    for i in range(N-1):
        s2[i+1] = s2[i] + dt * f2(t[i], s1[i])
        s1[i+1] = s1[i] + dt * f1(t[i], s2[i+1])

    return s1, s2


f1, f2, F0 = PendEq()

# theta, ptheta = ExplicitEuler(f1, f2, F0, t_span)
theta, ptheta = SemiImplicitEuler(f1, f2, F0, t_span)

plt.figure()
plt.plot(theta, ptheta)
plt.show()
