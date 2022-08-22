# uncomment the next line if running in a notebook
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)

# analytical solution
x0_array = v*np.sqrt(m/k)*np.sin(np.sqrt(k/m)*t_array)
v0_array = v*np.cos(np.sqrt(k/m)*t_array)

# initialise empty lists to record trajectories
x_list = []
v_list = []

# Euler integration for inital 2 as assuming initial conditions may be inaccurate
for t in range(2):

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a

# Verlet integration for the remaining 
for t in range(2, len(t_array)):
    
    # calculate new position and velocity
    a = -k * x / m
    x = 2 * x_list[t-1] - x_list[t-2] + (dt)**2*a 
    v = (x_list[t-1] - x_list[t-2]) / dt

    # append current state to trajectories 
    x_list.append(x)
    v_list.append(v)

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
#plt.plot(t_array, x0_array, label='Analytical x (m)')
#plt.plot(t_array, v0_array, label='Analytical v (m/s)')
plt.plot(t_array, x_array, label='Verlet x (m)')
plt.plot(t_array, v_array, label='Verlet v (m/s)')
plt.legend()
plt.show()
