# UPSAMPLING and DOWNSAMPLING
from scipy.io import wavfile
import scipy.signal as signal

sample_rate, data = wavfile.read('music.wav')

# Upsampling
k = 50
new_sample_rate = sample_rate * k
upsampled_data = signal.resample(data, len(data) * k)


wavfile.write('upsampled_audio.wav', new_sample_rate, upsampled_data.astype(data.dtype))

# Downsampling
p = 50
new_sample_rate = int(sample_rate / p)
downsampled_data = signal.resample(data, int(len(data) / p))


wavfile.write('downsampled_audio.wav', new_sample_rate, downsampled_data.astype(data.dtype))

print("succesfull")
