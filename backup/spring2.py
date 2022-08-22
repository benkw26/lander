# uncomment the next line if running in a notebook
# %matplotlib inline
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

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x0_array = v*np.sqrt(m/k)*np.sin(np.sqrt(k/m)*t_array)
v0_array = v*np.cos(np.sqrt(k/m)*t_array)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x0_array, label='x (m)')
plt.plot(t_array, v0_array, label='v (m/s)')
plt.legend()
plt.show()
