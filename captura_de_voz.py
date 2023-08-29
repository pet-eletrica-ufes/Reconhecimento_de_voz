import sounddevice as sd 
import wavio as wv 
import numpy
import time
from scipy.io.wavfile import write
def captura_voz(falante):
    for i in range(1):
        freq=16000
        tempo=3
        gravar=sd.rec(int(tempo*freq), samplerate=freq, channels=2)
        sd.wait()
        sampwidth=2
        write(f"voice-{falante}-{i+1}.wav", freq, gravar)
        wv.write(f"voice-{falante}-{i+1}.wav", gravar, freq, sampwidth=sampwidth)
        time.sleep(1)
    return falante
