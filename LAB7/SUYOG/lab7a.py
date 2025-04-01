import wave

wav_file = wave.open("wave.wav","r")
num_channels = wav_file.getnchannels()
sample_width = wav_file.getsampwidth()
sample_rate = wav_file.getframerate()
num_samples = wav_file.getnframes()

wav_file.close()

print("Number of channels: ", num_channels)

print("Sampling width (bit depth): ", sample_width)

print("Sampling rate: ", sample_rate)

print("Number of samples: ", num_samples)
