import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the audio file
file_path = 'D:\\GitHub Repositories\\Python\\UNSTPB\Year III\\Semester 2\\Digital Signal Processing\\Project\\test.WAV'
fs, audio = wavfile.read(file_path)

# Define the notch filter parameters
f0 = 60.0  # Frequency to be removed (Hz)
Q = 30.0   # Quality factor

# Design the notch filter
b, a = signal.iirnotch(f0, Q, fs)

# Apply the notch filter to the audio signal
filtered_audio = signal.filtfilt(b, a, audio)

# Save the filtered audio to a new file
output_path = 'D:\\GitHub Repositories\\Python\\UNSTPB\Year III\\Semester 2\\Digital Signal Processing\\Project\\filtered_audio.wav'
wavfile.write(output_path, fs, filtered_audio.astype(np.int16))

# Plot the frequency response of the notch filter
freq, h = signal.freqz(b, a, fs=fs)
plt.figure(figsize=(10, 4))
plt.plot(freq, 20 * np.log10(abs(h)), 'b')
plt.title('Notch Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid(True)
plt.show()

# Plot the original and filtered audio signals for comparison
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(audio)
plt.title('Original Audio Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(filtered_audio)
plt.title('Filtered Audio Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()