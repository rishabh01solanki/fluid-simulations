import numpy as np

def alpha_viscosity(r, sigma, v_r, v_phi, G, M):
    """
    Calculate the alpha viscosity in a self-similar model for a self-gravitating disk.
    
    Parameters:
    - r: radius of the disk (in cm)
    - sigma: surface density of the disk (in g/cm^2)
    - v_r: radial velocity of the disk (in cm/s)
    - v_phi: azimuthal velocity of the disk (in cm/s)
    - G: gravitational constant (in cm^3/g/s^2)
    - M: mass of the central object (in g)
    
    Returns:
    - alpha: alpha viscosity of the disk
    """
    # Calculate the sound speed in the disk
    c_s = np.sqrt(G * M / r)
    
    # Calculate the shear rate in the disk
    shear_rate = (v_phi - v_r) / r
    
    # Calculate the alpha viscosity
    alpha = - sigma * shear_rate / (2 * c_s**2)
    
    return alpha


alpha = alpha_viscosity(1, 1, 5, 10, 6.67e-8, 1)
print(alpha)
