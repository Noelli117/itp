#Importing libries
import tkinter as tk
from tkinter import ttk
import numpy as np
import sounddevice as sd

#Defining function for FM
def generate_waveform():
    global waveform, f_s, duration_s, f_c, f_m, k
    t = np.linspace(0, duration_s, int(f_s * duration_s), False)
    carrier = np.sin(2 * np.pi * f_c * t)
    modulator = np.sin(2 * np.pi * f_m * t)
    waveform = np.sin(2 * np.pi * (carrier + k * modulator) * t)
    waveform /= np.max(np.abs(waveform))

def play_waveform():
    global waveform, f_s
    sd.play(waveform, f_s)
    sd.wait()

def update_parameters():
    global f_s, duration_s, f_c, f_m, k
    f_s = int(sample_rate_entry.get())
    duration_s = float(duration_entry.get())
    f_c = float(carrier_freq_entry.get())
    f_m = float(modulation_freq_entry.get())
    k = float(modulation_index_entry.get())
    generate_waveform()

#UI setup
root = tk.Tk()
root.title("Waveform Generator")

# Parameters
f_s = 44100
duration_s = 3
f_c = 400.0
f_m = 100.0
k = 5

# Generate initial waveform
generate_waveform()

# UI Elements
sample_rate_label = tk.Label(root, text="Sample Rate:")
sample_rate_label.grid(row=0, column=0)
sample_rate_entry = ttk.Entry(root)
sample_rate_entry.grid(row=0, column=1)
sample_rate_entry.insert(0, str(f_s))

duration_label = tk.Label(root, text="Duration (s):")
duration_label.grid(row=1, column=0)
duration_entry = ttk.Entry(root)
duration_entry.grid(row=1, column=1)
duration_entry.insert(0, str(duration_s))

carrier_freq_label = tk.Label(root, text="Carrier Frequency:")
carrier_freq_label.grid(row=2, column=0)
carrier_freq_entry = ttk.Entry(root)
carrier_freq_entry.grid(row=2, column=1)
carrier_freq_entry.insert(0, str(f_c))

modulation_freq_label = tk.Label(root, text="Modulation Frequency:")
modulation_freq_label.grid(row=3, column=0)
modulation_freq_entry = ttk.Entry(root)
modulation_freq_entry.grid(row=3, column=1)
modulation_freq_entry.insert(0, str(f_m))

modulation_index_label = tk.Label(root, text="Modulation Index:")
modulation_index_label.grid(row=4, column=0)
modulation_index_entry = ttk.Entry(root)
modulation_index_entry.grid(row=4, column=1)
modulation_index_entry.insert(0, str(k))

update_button = ttk.Button(root, text="Update Parameters", command=update_parameters)
update_button.grid(row=5, column=0, columnspan=2)

play_button = ttk.Button(root, text="Play Waveform", command=play_waveform)
play_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
