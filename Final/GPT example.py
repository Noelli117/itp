import numpy as np
import pyaudio

class FMsynth:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.stream = pyaudio.PyAudio().open(format=pyaudio.paFloat32,
                                              channels=1,
                                              rate=sample_rate,
                                              output=True)

    def generate_wave(self, freq, duration):
        t = np.arange(0, duration, 1 / self.sample_rate)
        modulator = np.sin(2 * np.pi * 5 * t)  # Modulator frequency = 5 Hz
        carrier = np.sin(2 * np.pi * freq * t + 100 * modulator)  # Modulate the carrier frequency
        return carrier

    def play_wave(self, wave):
        self.stream.write(wave.astype(np.float32).tobytes())

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        pyaudio.PyAudio().terminate()

if __name__ == "__main__":
    synth = FMsynth()
    freq = 440  # Frequency of the carrier wave (A4 note)
    duration = 2  # Duration of the sound in seconds
    wave = synth.generate_wave(freq, duration)
    synth.play_wave(wave)
    synth.close()
