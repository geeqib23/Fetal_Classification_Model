import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def apply_bandpass_filter(signal_data, fs, lowcut, highcut):
    # Design an IIR bandpass filter using butterworth filter
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = signal.butter(N=4, Wn=[low, high], btype='band')

    # Apply the filter to the signal
    filtered_signal = signal.lfilter(b, a, signal_data)

    return filtered_signal
