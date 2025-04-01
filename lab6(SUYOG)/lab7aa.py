import wave
import numpy as np

# Parameters for the wave file
sample_rate = 44100  # samples per second
duration = 2.0  # seconds
frequency = 440.0  # sine wave frequency (Hz)

# Generate the sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Convert to 16-bit PCM format
sine_wave = np.int16(sine_wave * 32767)

# Create a wave file
file_path = "output.wav"
with wave.open(file_path, "w") as wav_file:
    wav_file.setnchannels(1)  # mono
    wav_file.setsampwidth(2)  # 2 bytes per sample
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(sine_wave.tobytes())

print(f"Wave file created: {file_path}")
