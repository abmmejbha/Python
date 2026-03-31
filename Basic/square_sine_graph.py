import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Create an array of time values
t = np.linspace(0, 1, 100)

# Generate the square wave signal
square_wave = signal.square(5 * np.pi * 1 * t)

# Plot the square wave
plt.plot(t, square_wave)
plt.title("Square Wave using Matplotlib")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


# Plot both sine and square waves
plt.plot(x, y, label='Sine', color='green')
plt.plot(t, square_wave, label='Square', color='blue')
plt.title("Sine and Square Waves using Matplotlib")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(false)
plt.show()
