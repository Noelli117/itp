import numpy as np
import sounddevice as sd

def generate_sine_wave(freq, duration, sample_rate):
    """
    Generate a sine wave signal.

    Parameters:
        freq (float): Frequency of the sine wave.
        duration (float): Duration of the signal in seconds.
        sample_rate (int): Sample rate of the signal.

    Returns:
        numpy.ndarray: Sine wave signal.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def fm_synthesizer(carrier_freq, modulator_freq, modulation_index, duration, sample_rate):
    """
    Generate a Frequency Modulated (FM) signal.

    Parameters:
        carrier_freq (float): Frequency of the carrier signal.
        modulator_freq (float): Frequency of the modulating signal.
        modulation_index (float): Modulation index.
        duration (float): Duration of the signal in seconds.
        sample_rate (int): Sample rate of the signal.

    Returns:
        numpy.ndarray: FM signal.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    carrier_wave = generate_sine_wave(carrier_freq, duration, sample_rate)
    modulator_wave = generate_sine_wave(modulator_freq, duration, sample_rate)
    return np.sin(2 * np.pi * (carrier_freq * t + modulation_index * np.sin(2 * np.pi * modulator_freq * t)))

# Example usage
carrier_freq = 100.0  # Frequency of the carrier signal (Hz)
modulator_freq = 120.0  # Frequency of the modulating signal (Hz)
modulation_index = 30.0  # Modulation index
duration = 2  # Duration of the signal (seconds)
sample_rate = 44100  # Sample rate of the signal (samples per second)

fm_signal = fm_synthesizer(carrier_freq, modulator_freq, modulation_index, duration, sample_rate)

# Play the FM signal
sd.play(fm_signal, sample_rate)
sd.wait()
