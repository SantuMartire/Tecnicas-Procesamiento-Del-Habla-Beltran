# AUDIO
import librosa
import librosa.display
import soundfile as sf
from IPython.display import Audio

audio, sr = sf.read('marita.wav')

#Guardar audio
sf.write('output.wav', audio, samplerate=sr)
print("Archivo guardado como output.wav")
