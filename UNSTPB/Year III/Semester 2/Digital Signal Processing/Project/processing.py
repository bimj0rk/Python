import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the audio file
file_path = 'D:\\GitHub Repositories\\Python\\UNSTPB\\Year III\\Semester 2\\Digital Signal Processing\\Project\\0.WAV'
fs, audio = wavfile.read(file_path)

# Parameters
fs = 10000
ft = 250
fc = 150
rp = 0.2
rs = 35

# Frequency calculations
wp = np.array(fc + ft/2)/(fs/2)
ws = np.array(fc - ft/2)/(fs/2)

# Design the notch filter
N, w = sp.buttord(wp, ws, rp, rs)
b, a = sp.butter(N, w, btype='high')


# Apply the notch filter to the audio signal
filtered_audio = sp.filtfilt(b, a, audio)

# Save the normalized filtered audio to a new file
output_path = 'D:\\GitHub Repositories\\Python\\UNSTPB\\Year III\\Semester 2\\Digital Signal Processing\\Project\\filtered_audio.wav'
wavfile.write(output_path, fs, filtered_audio.astype(np.int16))

# Plot the original and filtered audio for comparison
w, h = sp.freqz(b, a)
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.xlim(0, 0.5*fs)
plt.title("Frequency Response")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()
plt.subplot(3, 1, 2)
plt.plot(audio)
plt.title('Original Audio')
plt.subplot(3, 1, 3)
plt.plot(filtered_audio)
plt.title('Filtered Audio')
plt.tight_layout()
plt.show()