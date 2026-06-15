#TP 07 - Tecnicas para el Análisis del Audio - Práctica
# %% 1-Analizar el audio AnalisisTextos.mp3 con MediaInfo
#   -Informar: formato
#   -tasa de bits
#   -canales
#   -frecuencia de muestreo

# 2-Realizar el sampleo con ffmpeg

# 3-Analizar el audio nuevamente con MediaInfo
#   -Informar: formato
#   -tasa de bits
#   -canales
#   -formato de muestreo

# 4-Con python :
#   -Mostrar el Vector de la señal segmentada
#   -Mostrar la cantidad de elementos de la muestra
#   -Mostrar la Frecuencia de Muestreo
#   -Mostrar la duración en segundos del audio

# 5-Imprimir la señal sonora

# 6-Reproducir la señal original

# 7-Modificar la frecuencia de muestreo para que dure más y menos tiempo. Explicar que sucede con el sonido

# 8-Bajar la calidad del audio y reproducir la señal.Explicar cuál es el proceso.

# %%
import IPython.display
import matplotlib.pyplot as plt
import numpy as np
# AUDIO
import librosa
import librosa.display
import soundfile as sf
from IPython.display import Audio

audio, sr = sf.read('AnalisisTextos.mp3')
print(audio)
print('Largo array:', len(audio))
print("Frecuencia de Muestreo:",sr)
print('Duración:', len(audio)/sr)
plt.plot(audio)
plt.show()
Audio(audio,rate=sr)

## reproducción de array diferente profundidad de bits
#y = (audio*2**3).astype(np.int8)
#Audio(y,rate=sr)
# %%
