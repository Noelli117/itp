import numpy as np
import sounddevice as sd

# Constants
sample_rate = 44100
duration = 5  # seconds
freq_carrier = 440  # Carrier frequency (Hz)
freq_modulator = 220  # Modulator frequency (Hz)
modulation_index = 5  # Modulation index

# Generate time array
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Generate carrier and modulator waveforms
carrier_wave = np.sin(2 * np.pi * freq_carrier * t)
modulator_wave = np.sin(2 * np.pi * freq_modulator * t)

# FM synthesis
fm_wave = np.sin(2 * np.pi * (freq_carrier + modulation_index * modulator_wave) * t)

# Normalize the waveform
fm_wave /= np.max(np.abs(fm_wave))

# Play the FM waveform
sd.play(fm_wave, sample_rate)
sd.wait()
