import wave
import math

frequency = 440  # Frequency of the sine wave in Hz
amplitude = 400  # Amplitude of the sine wave
phase = 0  # Phase of the sine wave
duration = 1  # Duration of the sine wave in seconds
sample_rate = 44100  # Sample rate in Hz

num_samples = int(sample_rate * duration)  # Total number of samples

with wave.open('wave.wav', 'w') as file:
    file.setnchannels(1)  # Mono channel
    file.setsampwidth(2)  # Sample width in bytes (16 bits)
    file.setframerate(sample_rate)  # Sample rate

    for i in range(num_samples):
        time = i / sample_rate  # Current time in seconds
        sample = amplitude * math.sin(2 * math.pi * frequency * time + phase)  # Calculate the sample value

        # Normalize the sample to the range [-1.0, 1.0]
        normalized_sample = max(min(sample / amplitude, 1.0), -1.0)
        
        # Convert the normalized sample to 16-bit PCM format
        sample_int = int(normalized_sample * 32767)
        sample_bytes = sample_int.to_bytes(2, byteorder='little', signed=True)
        
        file.writeframes(sample_bytes)
