import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import time

#Parameters that controls the waveform:
f_s = 44100
duration_s = 5.0
f_c= 440.0
f_m= 220.0
k = 25
#f_s=sample rate,duration_s=duration time in seconds,f_c=carrier frequency, f_m=modulation frequency,k=modulator index

