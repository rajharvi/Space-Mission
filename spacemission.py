import math
import matplotlib.pyplot as plt
import numpy as np

# Constants 
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30  # Mass of the Sun (kg)
AU = 1.496e11  # Astronomical Unit (meters)

# Function to calculate Hohmann transfer
def hohmann_transfer(r1, r2):
    # Semi-major axis of transfer ellipse
    a = (r1 + r2) / 2
    
    # Orbital velocities
    v1 = math.sqrt(G * M_sun / r1)  # Velocity at departure
    v2 = math.sqrt(G * M_sun / r2)  # Velocity at arrival
    v_transfer_1 = math.sqrt(G * M_sun * (2 / r1 - 1 / a))  # Transfer orbit velocity at departure
    v_transfer_2 = math.sqrt(G * M_sun * (2 / r2 - 1 / a))  # Transfer orbit velocity at arrival
    
    # Delta-v calculations (difference in velocity for fuel requirement)
    delta_v1 = v_transfer_1 - v1
    delta_v2 = v2 - v_transfer_2
    total_delta_v = abs(delta_v1) + abs(delta_v2)
    
    return total_delta_v

# Function to visualize orbits and trajectory
def visualize_orbit(r1, r2):
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Plot orbits
    fig, ax = plt.subplots()
    ax.plot(r1 * np.cos(theta), r1 * np.sin(theta), label='Orbit 1')
    ax.plot(r2 * np.cos(theta), r2 * np.sin(theta), label='Orbit 2')
    
    # Plot transfer ellipse
    r_transfer = (r1 + r2) / 2
    ax.plot(r_transfer * np.cos(theta), r_transfer * np.sin(theta), label='Transfer Orbit', linestyle='--')
    
    ax.set_aspect('equal', 'box')
    ax.set_title('Hohmann Transfer Orbit')
    plt.legend()
    plt.show()

# User input
start = input("Enter starting planet's distance from Sun (AU): ")
destination = input("Enter destination planet's distance from Sun (AU): ")

# Convert distances from AU to meters
r1 = float(start) * AU
r2 = float(destination) * AU

# Calculate fuel requirements using Hohmann transfer
delta_v = hohmann_transfer(r1, r2)
print(f"Total Delta-v required for transfer: {delta_v:.2f} m/s")

# Visualize the orbits
visualize_orbit(r1, r2)

