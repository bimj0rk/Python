import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt
from scipy.io import wavfile

file_path = '/Volumes/WALLET/0.WAV'
fs, audio = wavfile.read(file_path)

fs = 16000
ft = 250
fc = 80
rp = 0.2
rs = 35

wp = np.array(fc + ft/2)/(fs/2)
ws = np.array(fc - ft/2)/(fs/2)

N, w = sp.buttord(wp, ws, rp, rs)
b, a = sp.butter(N, w, btype='high')

filtered_audio = sp.filtfilt(b, a, audio)

output_path = '/Volumes/WALLET/filtered_audio.wav'
wavfile.write(output_path, fs, filtered_audio.astype(np.int16))

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