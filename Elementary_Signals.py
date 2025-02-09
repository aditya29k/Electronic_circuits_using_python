import numpy as np
import matplotlib.pyplot as plt

# defining functions

def gen_impulse(time, pos):
  dis_signal = np.zeros(time)
  dis_signal[pos] = 1
  return dis_signal

def gen_unit(time):
  dis_signal = np.ones(time)
  return dis_signal

def gen_ramp(time):
  dis_signal = np.arange(0, time+1)
  return dis_signal

def gen_sin(time, amp, f):
  t = np.arange(0, time+1)
  dis_signal = amp*np.sin(2*np.pi*f*t)
  return dis_signal

def gen_cos(time, amp, f):
  t = np.arange(0, time+1)
  dis_signal = amp*np.cos(2*np.pi*f*t)
  return dis_signal

# calling funSctions

impulse_signal = gen_impulse(25, 6)
unit_signal = gen_unit(11)
ramp_signal = gen_ramp(15)
sin_signal= gen_sin(80, 1, 0.9)
cos_signal= gen_cos(80, 1, 0.9)

# plotting functions

plt.figure(figsize=(10, 14))

plt.subplot(7,1,1)
plt.title("Impulse Signal Plot")
plt.stem(impulse_signal)
plt.xlabel("time")
plt.ylabel("impulse response")

plt.subplot(7,1,2)
plt.title("Unit Signal Plot")
plt.stem(unit_signal)
plt.xlabel("time")
plt.ylabel("unit response")

plt.subplot(7,1,3)
plt.title("Ramp Signal Plot")
plt.stem(ramp_signal)
plt.xlabel("time")
plt.ylabel("ramp response")

plt.subplot(7,1,4)
plt.title("Sin Signal Discrete")
plt.stem(sin_signal)
plt.xlabel("time")
plt.ylabel("sin")

plt.subplot(7,1,5)
plt.title("Sin Signal Continuous")
plt.plot(sin_signal)
plt.xlabel("time")
plt.ylabel("sin")

plt.subplot(7,1,6)
plt.title("Cos Signal Discrete")
plt.stem(cos_signal)
plt.xlabel("time")
plt.ylabel("cos")

plt.subplot(7,1,7)
plt.title("Cos Signal Continuous")
plt.plot(cos_signal)
plt.xlabel("time")
plt.ylabel("cos")

plt.tight_layout()
plt.show()
