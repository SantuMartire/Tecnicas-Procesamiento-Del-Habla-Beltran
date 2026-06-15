# %%

import matplotlib.pyplot as plt
import numpy as np
# AUDIO
import librosa
import librosa.display
import soundfile as sf
from IPython.display import Audio

audio, sr = sf.read('marita.wav')
# reproducción de array diferente profundidad de bits
y = (audio*2**3).astype(np.int8)
Audio(y,rate=sr)

# %%
