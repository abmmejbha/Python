import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Create an array of time values
t = np.linspace(0, 2, 400)

# Generate the triangle wave signal
triangle_wave = 2 * signal.sawtooth(2 * np.pi * 1 * t, 0.5)  # Adjust frequency and duty cycle

# Plot the triangle wave
plt.plot(t, triangle_wave)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Triangle Wave")
plt.grid(True)
plt.show()
