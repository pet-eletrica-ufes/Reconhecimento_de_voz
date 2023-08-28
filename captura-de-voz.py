import sounddevice as sd 
import wavio as wv 
import numpy
import time
from scipy.io.wavfile import write
Nome=str(input("Digite o seu nome:"))
for i in range(15):
    freq=16000
    tempo=3
    gravar=sd.rec(int(tempo*freq), samplerate=freq, channels=2)
    sd.wait()
    sampwidth=2
    write(f"voice-{Nome}-{i+1}.wav", freq, gravar)
    wv.write(f"voice-{Nome}-{i+1}.wav", gravar, freq, sampwidth=sampwidth)
    time.sleep(1)
