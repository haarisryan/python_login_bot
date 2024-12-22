import sounddevice as sd
import numpy
from scipy.io.wavfile import write
import wavio as wv
freq=44100
duration=10
recording=sd.rec(int(duration*freq),samplerate=freq,channels=2,dtype='int16')
sd.wait()
write("recording0.wav",freq,recording)
# wv.write("recording0.wav",freq,recording,sampwidth=2)
sd.play()