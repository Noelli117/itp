import numpy as np
import sounddevice as sd

#This two lines of codes imports the necessary libries for numerical computations and Sounddevice library for audio input and output operations.

f_s = 44100
duration_s = 3
f_c = 400.0
f_m = 1000.0
k = 15

#Defining different parameters:
f_s=Sample rate in Hz (samples per second).
duration_s=Duration of the waveform in seconds.
f_c=Carrier frequency in Hz.
f_m=Modulation frequency in Hz.
k=Modulator index,the modulation index is defined as the ratio of frequency deviation to the modulating frequency.It determines the extent to which the carrier wave's frequency or phase varies in response to changes in the modulating signal's amplitude.

t = np.linspace(0, duration_s, int(f_s * duration_s), False)
#This line creates a time array t using NumPy's linspace function. It starts from 0 seconds, ends at duration_s seconds, and contains f_s * duration_s samples.The time array is set up to create a sequence of time points that correspond to the duration of the waveform.

carrier = np.sin(2 * np.pi * f_c * t)
#Here, carrier represents the carrier wave.The formula used (np.sin(2 * np.pi * f_c * t)) generates a sine wave with a frequency of f_c Hz over time t.

modulator = np.sin(2 * np.pi * f_m * t)
#The modulator wave is generated similarly to the carrier wave but with a frequency of f_m Hz. In FM, this wave's amplitude or frequency variations (depending on the modulation index) affect the carrier wave.

waveform = np.sin(2 * np.pi * (carrier + k * modulator) * t)
#In FM, the carrier wave's frequency is modulated by the instantaneous amplitude of the modulating wave (the modulator). The term carrier + k * modulator combines the carrier wave and the modulated component, where k is the modulation index，which is frequency deviation divided by modulator frequency.

waveform /= np.max(np.abs(waveform))
#This line normalizes the waveform by dividing each sample by the maximum absolute value in the waveform. This ensures that the waveform's amplitude stays within the valid range (-1 to 1).

sd.play(waveform, f_s)
sd.wait()
#sd.play(waveform, f_s): Plays the waveform using the Sounddevice library with the specified sample rate f_s.
sd.wait(): Waits until the audio playback is finished before continuing with the code execution.