import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate_alpha_viscosity(grid, viscosity, dt, dx):
    # Compute the viscosity coefficient
    alpha = viscosity * dt / (dx ** 2)
    
    # Compute the new velocities for each grid cell
    new_velocities = np.zeros_like(grid)
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            new_velocities[i, j] = grid[i, j] + alpha * (grid[i+1, j] + grid[i-1, j] + grid[i, j+1] + grid[i, j-1] - 4 * grid[i, j])
    
    # Update the velocities in the grid
    grid[1:-1, 1:-1] = new_velocities[1:-1, 1:-1]
    
    return grid

# Set the size of the grid (number of cells in each dimension)
nx = 100
ny = 100

# Set the spacing between grid cells (in meters)
dx = 0.1
dy = 0.1

# Set the time step (in seconds)
dt = 0.01

# Set the kinematic viscosity of the fluid (in m^2/s)
viscosity = 0.1

# Set the initial velocities in the grid
velocities = np.zeros((nx, ny))
velocities[:, 0] = 10.0  # Initial velocity from left to right at 10 m/s
velocities[0, :] = 10.0  # Initial velocity from right to left at 10 m/s

# Set up the animation figure
fig, ax = plt.subplots()

# Function to update the plot for each frame of the animation
def update(t):
    global velocities
    velocities = simulate_alpha_viscosity(velocities, viscosity, dt, dx)
    ax.clear()
    
    # Generate the x and y coordinates of the arrows using np.meshgrid
    x, y = np.meshgrid(np.arange(nx), np.arange(ny))
    ax.quiver(x, y, velocities[:,:], velocities[:,:])

# Run the animation
ani = animation.FuncAnimation(fig, update, frames=1000, repeat=False)
plt.show()
