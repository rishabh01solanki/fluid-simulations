import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
q = 1 # 1.6e-19  # Charge of the particle (C)
m = 1 #9.1e-31  # Mass of the particle (kg)
B = 1.5  # Magnitude of the magnetic field (T)
E = np.array([0.5, 0])  # Electric field (N/C)

# Initial position and velocity of the particle
x0 = np.array([0, 0])
v0 = np.array([1, 1])

# Time step and total time for the simulation
dt = 0.1
total_time = 2

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Initialize the particle's position and velocity
x = x0
v = v0

# Initialize the electric and magnetic force on the particle
F_e = q * E
F_b = q * np.array([-v[1], v[0]]) * B

# Initialize the list of positions for the animation
positions = [x]

# Function to update the position and velocity of the particle
# at each time step
def update(i):
    global x, v
    # Update the position and velocity of the particle
    a = (F_e + F_b) / m
    x = x + v * dt + 0.5 * a * dt**2
    v = v + a * dt
    # Add the new position to the list of positions
    positions.append(x)
    # Clear the axis for the new plot
    ax.clear()
    # Plot the path of the particle
    ax.plot([p[0] for p in positions], [p[1] for p in positions])
    # Set the axis limits to fit the path of the particle
    ax.set_xlim(min([p[0] for p in positions]) - 1, max([p[0] for p in positions]) + 1)
    ax.set_ylim(min([p[1] for p in positions]) - 1, max([p[1] for p in positions]) + 1)
    # Add labels for the x and y axes
    # Add labels for the x and y axes
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Plot the electric field as a quiver plot
    ax.quiver(0, 0, E[0], E[1], color='red', scale=1, scale_units='xy')
 

    # Plot the magnetic field as a circle around the origin
    circle = plt.Circle((0, 0), B, color='blue', fill=False)
    ax.add_artist(circle)
    
  


# Create the animation using the update function
anim = FuncAnimation(fig, update, frames=np.arange(0, total_time, dt), repeat=False)

# Show the plot
plt.show()
