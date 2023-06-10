import math
import numpy as np
from scipy.io import wavfile

#Inspired by https://ccrma.stanford.edu/~jos/sasp/Example_1_Low_Pass_Filtering.html

def filterSignal(samplerate, wav_data):
    # define parameters
    signal_length = wav_data.shape[0]
    num_channels = wav_data.shape[1]
    filterLength = math.ceil(30. * 1. / cutofffreq * samplerate)
    Nfft = 2 ** math.ceil(math.log2(filterLength + signalLength))

    # generate filter (windowed time-domain sinc() <-> low-pass = smooth step function in frequency domain)
    flt_timepoints = np.arange(-(filterLength - 1) / 2, (filterLength - 1) / 2 + 1) / samplerate
    flt_sinc = (2 * cutofffreq / samplerate) * np.sinc(2 * cutofffreq * flt_timepoints)
    flt_timedomain = np.hamming(filterLength) * flt_sinc
    flt_padded = np.append(flt_timedomain, np.zeros(Nfft - filterLength))
    flt_FT = np.fft.fft(flt_padded)
    print("flt_FT: ", flt_FT)

    # process channels
    out_data = []
    for channel in range(0, num_channels):
        data_raw = wav_data[:, channel] / (2 ** 15 - 1) # format-specific!
        data_padded = np.append(data_raw, np.zeros(Nfft - signalLength))
        data_FT = np.fft.fft(data_padded)

        print("Channel ", channel, " data_FT: ", data_FT)

        conv_FT = flt_FT * data_FT

        print("Channel ", channel, " conv_FT: ", conv_FT)
        conv_result = np.real(np.fft.ifft(conv_FT))
        out_channel = conv_result.astype(np.int16)



        if channel == 0:
            out_data = conv_result
        else:
            out_data = np.stack((out_data, conv_result), axis=-1)

    return out_data


input_path = input("Path to WAV file" + '\n')
fc = int(input("Cutoff Frequency" + '\n'))
output_path = input("Path for output" + '\n')


try:
    samplerate, wav = wavfile.read(inputpath)
except:
    print("Failed to load '%s'" % input_path)
    exit(1)

filtered_data = filterSignal(samplerate, wav)

wavfile.write(outputpath, samplerate, filtered_data) # out_data.astype(np.int16))

