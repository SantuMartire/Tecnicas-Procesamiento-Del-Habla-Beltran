import matplotlib.pyplot as plt
import numpy as np
# %%
# AUDIO
import librosa
import librosa.display
import soundfile as sf
from IPython.display import Audio

audio, sr = sf.read('marita.wav')
print(audio)
print('Largo array:', len(audio))
print('Frecuencia de Muestreo:',sr)
print('Duración:', len(audio)/sr)
# reproducción de array diferente frecuencia de muestreo
Audio(audio,rate=sr*2)

