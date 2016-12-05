import pyaudio
import struct
import datetime
import wave
import numpy as np
import os

def savetransc():
    WIDTH = 2           # bytes per sample
    CHANNELS = 1
    RATE = 16000        # Sampling rate (samples/second)
    BLOCKSIZE = 1024
    DURATION = 6      # Duration in seconds

    NumBlocks = int( DURATION * RATE / BLOCKSIZE )

    # Open audio device:
    p = pyaudio.PyAudio()
    PA_FORMAT = p.get_format_from_width(WIDTH)
    stream = p.open(format = PA_FORMAT,
                    channels = 1,
                    rate = RATE,
                    input = True,
                    output = False)

    output_wavefile = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'mic_input1.wav')

    wf = wave.open(output_wavefile, 'wb')      # wave file
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(WIDTH)
    wf.setframerate(RATE)

    for n in range(0,NumBlocks):
        input_string = stream.read(BLOCKSIZE)
        input_tuple = struct.unpack('h'*BLOCKSIZE, input_string)
        output_string = struct.pack('h'*BLOCKSIZE, *input_tuple)
        wf.writeframes(output_string)


    stream.stop_stream()
    stream.close()
    p.terminate()
        
