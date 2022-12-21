import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt

# Set the size of the fluid domain
nx = 50
ny = 50

# Set the physical properties of the fluid
rho = 100.0
nu = 0.1

# Set the timestep
dt = 0.02

dx = 1.0  # Set the spacing between grid points in the x-direction
dy = 1.0  # Set the spacing between grid points in the y-direction


# Set the number of timesteps to calculate
n_steps = 100

# Set the initial velocity field
u = np.ones((ny, nx)) * 0.5  # Set a constant velocity in the x-direction
v = np.zeros((ny, nx))  # Set zero velocity in the y-direction


# Set the initial pressure field
p = np.zeros((ny, nx))

# Set the boundary conditions
u[:, 0] = 10.0  # Left wall is moving with velocity 1.0 in the x direction
u[:, -1] = 0.0  # Right wall is stationary
v[0, :] = 0.0  # Top wall is stationary
v[-1, :] = 0.0  # Bottom wall is stationary

# Set the kinematic viscosity
kinematic_viscosity = nu * rho

# Set the constants for the finite difference method
const_1 = dt / (rho * dx**2)
const_2 = dt / (rho * dy**2)
const_3 = kinematic_viscosity * dt / dx**2
const_4 = kinematic_viscosity * dt / dy**2

# Loop through the timesteps
for i in range(1, n_steps):
  # Calculate the intermediate velocity fields
  u_star = u.copy()
  v_star = v.copy()
  for j in range(1, ny-1):
    for k in range(1, nx-1):
      u_star[j, k] = u[j, k] - const_1 * (p[j+1, k] - p[j-1, k]) + const_3 * (u[j, k+1] - 2 * u[j, k] + u[j, k-1]) + const_4 * (u[j+1, k] - 2 * u[j, k] + u[j-1, k])
      v_star[j, k] = v[j, k] - const_2 * (p[j, k+1] - p[j, k-1]) + const_4 * (v[j, k+1] - 2 * v[j, k] + v[j, k-1]) + const_3 * (v[j+1, k] - 2 * v[j, k] + v[j-1, k])
  # Calculate the pressure at each point on the grid
  p_new = p.copy()
  for j in range(1, ny-1):
    for k in range(1, nx-1):
      p_new[j, k] = (const_1 * (u_star[j, k+1] - u_star[j, k-1]) + const_2 * (v_star[j+1, k] - v_star[j-1, k])) / (2 * (const_1 + const_2))
  # Calculate the final velocity fields
  u[1:-1, 1:-1] = u_star[1:-1, 1:-1] - (dt / rho) * (p_new[1:-1, 2:] - p_new[1:-1, :-2])
  v[1:-1, 1:-1] = v_star[1:-1, 1:-1] - (dt / rho) * (p_new[2:, 1:-1] - p_new[:-2, 1:-1])
  # Update the pressure field
  p = p_new  # Update the pressure field

# Set the initial position of the particle
x_pos = nx/2
y_pos = ny/2

# Set up the figure and axis for the plot
fig, ax = plt.subplots()

# Set the limits of the plot
ax.set_xlim(0, nx)
ax.set_ylim(0, ny)

# Create arrays with the x and y coordinates of the grid points
X, Y = np.meshgrid(np.arange(nx), np.arange(ny))

# Set up the quiver plot for the velocity field
velocity_field = ax.quiver(X, Y, u, v)

# Set up the particle scatter plot
particle = ax.plot([], [], 'o', color='red')

# Define the update function for the animation
def update(i):
  global x_pos, y_pos
  
  # Update the position of the particle
  x_pos += u[y_pos, x_pos] * dt
  y_pos += v[y_pos, x_pos] * dt

# Apply periodic boundary conditions
  x_pos = x_pos % nx
  y_pos = y_pos % ny

  
  # Update the particle scatter plot
  particle.set_data(x_pos, y_pos)
  
  return velocity_field, particle

# Set up the animation using the update function
anim = animation.FuncAnimation(fig, update, frames=range(n_steps), blit=True)

plt.show()


'''
# Set up the figure and axis for the plot
fig, ax = plt.subplots()

# Set the limits of the plot
ax.set_xlim(0, nx)
ax.set_ylim(0, ny)

# Set the title and labels for the plot
ax.set_title('Fluid Flow')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Create arrays with the x and y coordinates of the grid points
X, Y = np.meshgrid(np.arange(nx), np.arange(ny))

# Create quiver plot to show the velocity field
quiver = ax.quiver(X, Y, u, v)

def animate(i):
    # Update the velocity field at each timestep
    quiver.set_UVC(u[:,:], v[:,:])
    return quiver


# Set the interval between frames (in milliseconds)
interval = 1

# Create the animation object
anim = animation.FuncAnimation(fig, animate, frames=range(n_steps), interval=interval)

# Show the plot
plt.show()
'''
