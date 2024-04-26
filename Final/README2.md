import tkinter as tk
from tkinter import ttk
import numpy as np
import sounddevice as sd


# Importing necessary libries for computations as well as building up UI;
'tkinter' is the standard GUI (Graphical User Interface) library for Python. It provides tools to create windows, buttons, entry fields, and other GUI elements.
'ttk' is a submodule within tkinter that offers themed widgets for a more modern and consistent appearance.
'numpy' is a numerical computing library used for array manipulation and mathematical operations. Here, it helps in generating the waveform data.
'sounddevice' is a library for inputing and outputing audio.


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

# Definitions of different parameters:
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
#I used GPT as a reference for this step because I could not get any sound at the begining, so I threw these whole programe into GPT and let it debug for me, and it gave me this line of code
#This line normalizes the waveform by dividing each sample by the maximum absolute value in the waveform. This ensures that the waveform's amplitude stays within the valid range (-1 to 1).

sd.play(waveform, f_s)
sd.wait()
#sd.play(waveform, f_s): Plays the waveform using the Sounddevice library with the specified sample rate f_s.
sd.wait(): Waits until the audio playback is finished before continuing with the code execution.

def update_parameters():
    global f_s, duration_s, f_c, f_m, k
    f_s = int(sample_rate_entry.get())
    duration_s = float(duration_entry.get())
    f_c = float(carrier_freq_entry.get())
    f_m = float(modulation_freq_entry.get())
    k = float(modulation_index_entry.get())
    generate_waveform()

# Parameter Update Function:
update_parameters(): This function is triggered when the user clicks the "Update Parameters" button in the GUI. It reads the values entered by the user in the entry fields for sample rate, duration, carrier frequency, modulation frequency, and modulation index. These values are then converted to the appropriate data types (integer or float) and used to update the global variables. After updating the parameters, generate_waveform() is called to regenerate the waveform with the new parameters.

root = tk.Tk()
root.title("Waveform Generator")


# Main GUI setup
root = tk.Tk(): Creates the main window for the GUI application.
root.title("Waveform Generator"): Sets the title of the window.

# Defining parameters
f_s = 44100
duration_s = 3
f_c = 400.0
f_m = 100.0
k = 5

#Generate initial waveform
generate_waveform()

# UI Elements
sample_rate_label = tk.Label(root, text="Sample Rate:")
#Labels are used to display static text or instructions to the user.
In this code, sample_rate_label is a label widget created using tk.Label that displays the text "Sample Rate:".

sample_rate_label.grid(row=0, column=0)

sample_rate_entry = ttk.Entry(root)
#Entry fields provide a space for users to input data, such as numbers or text.
sample_rate_entry is an entry field widget created using ttk.Entry where users can input the sample rate value.
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

#Applying the same principle on every parameters in the UI

update_button = ttk.Button(root, text="Update Parameters", command=update_parameters)
update_button.grid(row=5, column=0, columnspan=2)

play_button = ttk.Button(root, text="Play Waveform", command=play_waveform)
play_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
