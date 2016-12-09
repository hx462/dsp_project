import pyaudio
import struct
import datetime
import wave
import numpy as np

def savecombination(file_sample):

    THRESHOLD = 5000   # Threshold to start writing to wave file
    WIDTH = 2           # bytes per sample
    CHANNELS = 1
    RATE = 16000        # Sampling rate (samples/second)
    BLOCKSIZE = 1024
    DURATION = 60       # Duration in seconds

    NumBlocks = int( DURATION * RATE / BLOCKSIZE )

    print('  ** Waiting ** ...')

    # Open audio device:
    p = pyaudio.PyAudio()
    PA_FORMAT = p.get_format_from_width(WIDTH)
    stream = p.open(format = PA_FORMAT,
                    channels = 1,
                    rate = RATE,
                    input = True,
                    output = True)
    i = 0
    endTime = 0

    wait = True
    sample_recorded = 0
    avg_fft = [0 for n in range(3)]
    
    avg_comb = [0 for c in range(2)]

    wait = True

    while True:
        fft_sum = 0
        input_string = stream.read(BLOCKSIZE)                     # Read audio input stream
        input_tuple = struct.unpack('h'*BLOCKSIZE, input_string)  # Convert
        output_block = np.array(input_tuple)
        X = np.fft.fft(input_tuple)
        fft_sum += sum(abs(X))

        if wait == True:
            m = max(abs(output_block))
            if m >= THRESHOLD:
                wait = False
                print "Recording..."
                endTime = datetime.datetime.now() + datetime.timedelta(seconds=5)

        if file_sample == 0:
            output_wavefile = 'first_combination.wav'
            wf = wave.open(output_wavefile, 'wb')      # wave file
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(WIDTH)
            wf.setframerate(RATE)

            while (wait == False):
                input_string = stream.read(BLOCKSIZE)                     # Read audio input stream
                input_tuple = struct.unpack('h'*BLOCKSIZE, input_string)  # Convert
                output_block = np.array(input_tuple)
                X = np.fft.fft(input_tuple)
                fft_sum += sum(abs(X))
                # Convert values to binary string
                output_string = struct.pack('h' * BLOCKSIZE, *output_block)
                # Write to wave file
                wf.writeframes(output_string)
                if datetime.datetime.now() >= endTime:
                    wait = True
                    print "\nFinished recording the frist combination"
                    avg_comb[file_sample] = fft_sum/(DURATION * RATE)
                    print "The average is for the first combination is ", avg_comb[file_sample]
                    sample_recorded = 1
                    break

        if file_sample == 1:
            output_wavefile = 'second_combination.wav'
            wf = wave.open(output_wavefile, 'wb')      # wave file
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(WIDTH)
            wf.setframerate(RATE)

            while (wait == False):
                input_string = stream.read(BLOCKSIZE)                     # Read audio input stream
                input_tuple = struct.unpack('h'*BLOCKSIZE, input_string)  # Convert
                output_block = np.array(input_tuple)
                X = np.fft.fft(input_tuple)
                fft_sum += sum(abs(X))
                # Convert values to binary string
                output_string = struct.pack('h' * BLOCKSIZE, *output_block)
                # Write to wave file
                wf.writeframes(output_string)
                if datetime.datetime.now() >= endTime:
                    wait = True
                    print "\nFinished recording the frist combination"
                    avg_comb[file_sample] = fft_sum/(DURATION * RATE)
                    print "The average is for the first combination is ", avg_comb[file_sample]
                    sample_recorded = 1
                    break

        if(sample_recorded == 1):
            return avg_comb[file_sample]


#savecombination(1)
        
