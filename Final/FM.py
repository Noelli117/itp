import numpy as np
import sounddevice as sd
import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Initialize the game controller
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Define initial parameters
carrier_freq = 440.0
modulator_freq = 10.0
modulation_index = 10.0
duration = 2
sample_rate = 44100

# Function 
def fm_synthesizer(carrier_freq, modulator_freq, modulation_index, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # sin(2pi*(f_c*t+m*sin(2pi*f_m*t)))
    return np.sin(2 * np.pi * (carrier_freq * t + modulation_index * np.sin(2 * np.pi * modulator_freq * t)))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update parameters based on controller input
    carrier_freq = joystick.get_axis(0) * 1000.0  # Map joystick X-axis to carrier frequency
    modulator_freq = joystick.get_axis(1) * 1000.0  # Map joystick Y-axis to modulator frequency
    modulation_index = (joystick.get_axis(2) + 1) * 50.0  # Map joystick Z-axis to modulation index

    # Generate FM signal
    fm_signal = fm_synthesizer(carrier_freq, modulator_freq, modulation_index, duration, sample_rate)

    # Play the FM signal
    sd.play(fm_signal, sample_rate)
    sd.wait()

# Clean up
pygame.quit()
