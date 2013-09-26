from bregman.suite import *
from pylab import *
import wave, struct
from matplotlib import pyplot
import pyfftw
import numpy as np

a1 = os.path.join(audio_dir,"ra.wav")

w = wave.open(a1)


length = w.getnframes()
"""
for i in range(0,length):
    wd = w.readframes(1)
    print wd
    data = struct.unpack("<H", wd)
    print int(data[0])


print "channels: ", w.getnchannels()
print "sample width:", w.getsampwidth()
print "framerate: ", w.getframerate()
print "frames: ", length
wd = w.readframes(1)
print wd
data = struct.unpack("<i", wd)
print "frames ex.: ", int(data[0])
"""


f = zeros(length)

for i in range(0,length):
    wd1 = w.readframes(1)
    if len(wd1)==4:
        data1 = struct.unpack("<i", wd1)
    elif len(wd1)==2:
        data1 = struct.unpack("<H", wd1)
    f[i] = int(data1[0])

fnorm = complex64(f/f.max())
t = range(0,size(f))

fft = complex64(np.ndarray(length))

#print type(fnorm), type(fft)

pyfftw.FFTW(fnorm,fft)
#plot(t,fft)

#plot(t,fnorm)
