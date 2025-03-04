from pydub import AudioSegment
import numpy as np 
import matplotlib.pyplot as plt
from scipy.fft import fft


def main():

    audio = AudioSegment.from_file("assets/daisy.wav")
    samples = np.array(audio.get_array_of_samples())

    # Perform FFT
    fft_result = fft(samples)
    frequencies = np.abs(fft_result)

        # Plotting Frequency Spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies)
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.show()

    pass 




if __name__ == '__main__':
    main()