import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Constants
m = 1.0  # mass
l = 1.0  # length
g = 9.81  # gravity
omega_sq = g / l  # omega^2

# Time settings
dt = 0.01  # time step
T = 10  # total simulation time
N = int(T / dt)  # number of time steps

# Initial conditions
theta0 = np.pi / 4  # initial angle
p_theta0 = 0.0  # initial angular momentum

# Explicit Euler Method
def explicit_euler(theta0, p_theta0, N, dt):
    theta = np.zeros(N)
    p_theta = np.zeros(N)
    theta[0], p_theta[0] = theta0, p_theta0

    for i in range(N - 1):
        theta[i + 1] = theta[i] + dt * p_theta[i] / (m * l**2)
        p_theta[i + 1] = p_theta[i] - dt * m * l**2 * omega_sq * np.sin(theta[i])

    return theta, p_theta

# Implicit Euler Method (requires solving nonlinear equations)
def implicit_euler(theta0, p_theta0, N, dt):
    theta = np.zeros(N)
    p_theta = np.zeros(N)
    theta[0], p_theta[0] = theta0, p_theta0

    for i in range(N - 1):
        # Define implicit system
        def equations(vars):
            theta_next, p_theta_next = vars
            eq1 = theta_next - theta[i] - dt * p_theta_next / (m * l**2)
            eq2 = p_theta_next - p_theta[i] + dt * m * l**2 * omega_sq * np.sin(theta_next)
            return [eq1, eq2]

        # Solve using fsolve
        theta_next, p_theta_next = fsolve(equations, [theta[i], p_theta[i]])
        theta[i + 1], p_theta[i + 1] = theta_next, p_theta_next

    return theta, p_theta

# Semi-Implicit Euler Method (Symplectic Euler)
def semi_implicit_euler(theta0, p_theta0, N, dt):
    theta = np.zeros(N)
    p_theta = np.zeros(N)
    theta[0], p_theta[0] = theta0, p_theta0

    for i in range(N - 1):
        p_theta[i + 1] = p_theta[i] - dt * m * l**2 * omega_sq * np.sin(theta[i])  # Update momentum first
        theta[i + 1] = theta[i] + dt * p_theta[i + 1] / (m * l**2)  # Update position using new momentum

    return theta, p_theta

# Run simulations
theta_exp, p_theta_exp = explicit_euler(theta0, p_theta0, N, dt)
theta_imp, p_theta_imp = implicit_euler(theta0, p_theta0, N, dt)
theta_semi, p_theta_semi = semi_implicit_euler(theta0, p_theta0, N, dt)

# Phase Space Plot (p_theta vs theta)
plt.figure(figsize=(10, 5))
plt.plot(theta_exp, p_theta_exp, label="Explicit Euler", linestyle="--", alpha=0.7)
plt.plot(theta_imp, p_theta_imp, label="Implicit Euler")
plt.plot(theta_semi, p_theta_semi, label="Semi-Implicit Euler", linestyle="-.")
plt.xlabel("Theta (rad)")
plt.ylabel("p_theta (kg m²/s)")
plt.legend()
plt.title("Phase Space Trajectory: p_theta vs Theta")
plt.grid()
plt.show()
