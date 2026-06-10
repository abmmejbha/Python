import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Create an array of X values
x = np.linspace(0, 1 * np.pi, 100)

# Plot the square sine curve
y = np.sin(x) * np.sign(np.sin(x))

# Compute the corresponding Y values for the square sine function
t = np.linspace(0, 1, 100)
square_wave = signal.square(2*np.pi * 1 *t)

# Plot the sine wave
plt.plot(t, square_wave)

plt.plot(x, y, label='Square Sine')
plt.axhline(y=0, color='k', linestyle=':')  # Add a horizontal line at y=0
plt.axvline(x=0, color='k', linestyle=':')  # Add a vertical line at x=0
plt.title("Square Sine Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()
