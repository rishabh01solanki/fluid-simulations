import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Set the number of particles
n_particles = 40

# Set the initial positions and velocities of the particles
x0 = np.random.uniform(-1, 1, n_particles)
y0 = np.random.uniform(-1, 1, n_particles)
vx0 = np.random.uniform(-1, 1, n_particles)
vy0 = np.random.uniform(-1, 1, n_particles)

# Set the timestep
dt = 0.01

# Set the number of timesteps to calculate
n_steps = 100

# Set the gravitational constant
G = 1

# Initialize the position and velocity arrays
x = np.zeros((n_steps, n_particles))
y = np.zeros((n_steps, n_particles))
vx = np.zeros((n_steps, n_particles))
vy = np.zeros((n_steps, n_particles))

# Set the initial positions and velocities
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

# Loop through the timesteps
for i in range(1, n_steps):
  # Loop through the particles
  for j in range(n_particles):
    # Calculate the acceleration of the particle due to gravity
    ax = 0
    ay = 0
    for k in range(n_particles):
      if k != j:
        dx = x[i-1, k] - x[i-1, j]
        dy = y[i-1, k] - y[i-1, j]
        r = np.sqrt(dx**2 + dy**2)
        ax += G * dx / r**2
        ay += G * dy / r**2
    # Use Euler's method to calculate the position and velocity
    x[i, j] = x[i-1, j] + vx[i-1, j] * dt
    y[i, j] = y[i-1, j] + vy[i-1, j] * dt
    vx[i, j] = vx[i-1, j] + ax * dt
    vy[i, j] = vy[i-1, j] + ay * dt

# Set up the plot
fig, ax = plt.subplots()
scatter = ax.scatter([], [])
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Function to update the plot at each timestep
def update(i):
  scatter.set_offsets(np.column_stack((x[i], y[i])))
  return scatter,

# Show the animation
anim = animation.FuncAnimation(fig, update, frames=n_steps, interval=10)
plt.show()