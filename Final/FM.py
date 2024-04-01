import numpy as np
import scipy.signal as signal
import sounddevice as sd

def generate_fm_signal(duration, sampling_freq, carrier_freq, modulator_freq, modulation_index):
    # Generate time array
    t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)

    # Generate modulating signal
    modulator_signal = np.sin(2 * np.pi * modulator_freq * t)

    # Generate carrier signal
    carrier_signal = np.sin(2 * np.pi * carrier_freq * t + modulation_index * np.sin(2 * np.pi * modulator_freq * t))

    # FM signal is simply the product of carrier and modulator
    fm_signal = carrier_signal

    return fm_signal

def play_audio(signal, sampling_freq):
    sd.play(signal, samplerate=sampling_freq)
    sd.wait()

if __name__ == "__main__":
    duration = 3  # Duration of the signal in seconds
    sampling_freq = 44100  # Sampling frequency in Hz
    carrier_freq = 440  # Frequency of the carrier signal in Hz
    modulator_freq = 5  # Frequency of the modulating signal in Hz
    modulation_index = 10  # Modulation index

    fm_signal = generate_fm_signal(duration, sampling_freq, carrier_freq, modulator_freq, modulation_index)
    play_audio(fm_signal, sampling_freq)
