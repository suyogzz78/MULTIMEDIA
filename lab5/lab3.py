# Consider a sine wave with frequency 3hz, amplitude 1 and phase 0. Generate 10
#different samples from the sine wave at interval of 0.3 starting from 0sec. Plot the
#samples against time using python matplotlib.
import numpy as np
import matplotlib.pyplot as plt

freq = 3
amp = 1
phase = 0
t = np.arange(0, 3.1, 0.3)
y = amp * np.sin(2 * np.pi * freq * t + phase)
plt.plot(t, y, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('10 Samples of Sine Wave with f = 3 Hz')
plt.grid()
plt.show()
