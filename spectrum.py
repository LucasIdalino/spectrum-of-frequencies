import matplotlib.pyplot as plt
import scipy.io.wavfile as wavefile


fs, aud = wavefile.read("caminho do arquivo", 'r') #selecione o arquivo .wav
aud = aud[:, 1] #selecione um canal
first = aud[:] #passe o tempo de duração para análise no espectrograma

power_spectrum, frequencies_found, time, image_axis = plt.specgram(first, Fs=fs)
plt.show()
