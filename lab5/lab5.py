#Consider a sine wave with frequency 3hz, amplitude 1 and phase 0. Plot the sine wave starting from 0sec to 10sec. Consider Nyquist theorem for sampling.
import numpy as np
import matplotlib.pyplot as plt

freq = 3  # Frequency in Hz
amp = 1   # Amplitude
phase = 0 # Phase
sampling_rate = 30  # Sampling rate in Hz
nyquist_freq = sampling_rate / 2  # Nyquist frequency

t = np.arange(0, 10, 1/sampling_rate)  # Time vector from 0 to 10 seconds
y = amp * np.sin(2 * np.pi * freq * t + phase)  # Sine wave samples

plt.plot(t, y, 'r', linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave with f = 3 Hz, Sampling Rate = 30 Hz")
plt.grid()
plt.show()
