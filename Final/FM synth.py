#Importing necessary librires:
import numpy as np
import sounddevice as sd


#Parameters that controls the waveform:
f_s = 44100
duration_s = 3
f_c= 400.0
f_m= 1000.0
k = 15
#f_s=sample rate,duration_s=duration time in seconds,f_c=carrier frequency, f_m=modulation frequency,k=modulator index

#Generated time array
t = np.linspace(0, duration_s, int(f_s * duration_s), False)

#The actual function:
carrier=np.sin(2 * np.pi * f_c * t)
modulator=np.sin(2 * np.pi * f_m* t)
waveform=np.sin(2 * np.pi * (carrier + k * modulator) * t)

#Normalizing the waveform:
waveform /= np.max(np.abs(waveform))

#Play it out:
sd.play(waveform, f_s)
sd.wait()