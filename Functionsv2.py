
import numpy as np
import matplotlib.pyplot as plt

def semiImplicitEuler(dthetadt,dPthetadt, F0, dt, tf):

    t = np.arange(0, tf + dt, dt) # Numerical grid
    theta = np.zeros(len(t))
    Ptheta = np.zeros(len(t))
    theta[0] = F0[0]
    Ptheta[0] = F0[1]
    for i in range(1,len(t)):
        theta[i] = theta[i-1] + dt*dthetadt(t[i-1],Ptheta[i-1])
        Ptheta[i] = Ptheta[i-1] + dt*dPthetadt(t[i-1],theta[i])

    return Ptheta, theta, t

def ExplicitEuler(dthetadt,dPthetadt, F0, dt, tf):

    t = np.arange(0, tf + dt, dt) # Numerical grid    
    theta = np.zeros(len(t))
    Ptheta = np.zeros(len(t))
    theta[0] = F0[0]
    Ptheta[0] = F0[1]

    for i in range(1,len(t)):
        theta[i] = theta[i-1] + dt*dthetadt(t[i-1],Ptheta[i-1])
        Ptheta[i] = Ptheta[i-1] + dt*dPthetadt(t[i-1],theta[i-1])

    return Ptheta, theta, t

def implicitEuler(dthetadt,dPthetadt, F0, dt, tf):

    t = np.arange(0, tf + dt, dt) # Numerical grid
    S = np.zeros(len(t))
    S[0] = F0

    for i in range(1,len(t)):
        S[i] = S[i-1] + dt*F(S[i],t[i])

    return t, S
    

def hamiltonian():
    omega = 9.80665 # Frequency m/s^2

    # Hamiltonian equations
    dthetadt = lambda t, Ptheta: Ptheta
    dPthetadt = lambda t, theta: -np.sin(theta)*omega 
    return dthetadt, dPthetadt

F0 = np.array([np.pi/4, 0]) # Initial conditions
dt = 0.01 # Step size
t = 20 # Final time

dthetadt,dPhetadt = hamiltonian()
Ptheta_exp, theta_exp, t_exp = ExplicitEuler(dthetadt, dPhetadt, F0, dt, t)
Ptheta_sem, theta_sem, t_sem = semiImplicitEuler(dthetadt, dPhetadt, F0, dt, t)
# t, sol = ExplicitEuler(f, s0, dt, t)

# print()
plt.figure()

plt.plot(Ptheta_exp, theta_exp)
plt.plot(Ptheta_sem, theta_sem)
plt.title('Phase Space')
plt.xlabel('Ptheta')
plt.ylabel('theta')
plt.legend(['Explicit Euler', 'Semi-Implicit Euler'])
plt.grid()
plt.xlim([-5,5])
plt.ylim([-2,2])
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.tight_layout()
plt.show()


# def ImplicitEuler():