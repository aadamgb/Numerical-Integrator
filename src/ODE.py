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


#############################
#     DEFING FUNCTIONS      #
#############################

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
    s1[0], s2[0] = F0[0], F0[1]

    for i in range(N - 1):
        s2[i + 1] = s2[i] + dt * f2(t[i], s1[i])
        s1[i + 1] = s1[i] + dt * f1(t[i], s2[i])

    return s1, s2

# Semi-Implicit Method Integrator
def SemiImplicitEuler(f1, f2, F0, t):
    N = len(t)
    s1 = np.zeros(N)
    s2 = np.zeros(N)
    s1[0], s2[0] = F0[0], F0[1]

    for i in range(N - 1):
        s2[i + 1] = s2[i] + dt * f2(t[i], s1[i])
        s1[i + 1] = s1[i] + dt * f1(t[i], s2[i + 1])

    return s1, s2

# Implicit Method Integrator
def ImplicitEuler(f1, f2, F0, t):
    N = len(t)
    s1 = np.zeros(N)
    s2 = np.zeros(N)
    s1[0], s2[0] = F0[0], F0[1]
    
    for i in range(N - 1):
        def equations(vars):
            s1_next, s2_next = vars
            eq1 = s1_next - s1[i] - dt * f1(t[i + 1], s2_next)
            eq2 = s2_next - s2[i] - dt * f2(t[i + 1], s1_next)
            return [eq1, eq2]

        s1_next, s2_next = fsolve(equations, [s1[i], s2[i]])
        s1[i + 1], s2[i + 1] = s1_next, s2_next

    return s1, s2

#############################
# RUNING THE ODE INTEGRATOR #
#############################

# Simulation Parameters
tf = 10
dt = 0.01
t_span = np.arange(0, dt + tf, dt)

f1, f2, F0 = PendEq()

theta_explicit, ptheta_explicit = ExplicitEuler(f1, f2, F0, t_span)
theta_semi, ptheta_semi = SemiImplicitEuler(f1, f2, F0, t_span)
theta_implicit, ptheta_implicit = ImplicitEuler(f1, f2, F0, t_span)


# PLOTTING RESULTS #
plt.figure()
plt.plot(theta_explicit, ptheta_explicit, label = "Explicit")
plt.plot(theta_semi, ptheta_semi, label = "Semi-Implicit")
plt.plot(theta_implicit, ptheta_implicit, label = "Implicit")
print(theta_implicit)
print(f"{ptheta_implicit}")
plt.title("Pendulum Phase Diagram")
plt.xlabel("Theta")
plt.ylabel("Ptheta")
plt.legend()
plt.show()
