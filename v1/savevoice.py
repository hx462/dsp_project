import pyaudio
import struct
import datetime
import wave
import numpy as np

def savevoice(file_sample):

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
                output_wavefile = 'sample1.wav'
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
                        sample_recorded = 1
                        wait = True
                        print "Finished recording sample 1"
                        avg_fft[file_sample] = fft_sum/(DURATION * RATE)
                        print "The average is for the first sample is ", avg_fft[file_sample]
                        #file_sample = 1
                        break
        elif file_sample == 1:
                output_wavefile = 'sample2.wav'
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
                        sample_recorded = 1
                        wait = True
                        print "\nFinished recording sample 2"
                        avg_fft[file_sample] = fft_sum/(DURATION * RATE)
                        print "The average is for the second sample is ", avg_fft[file_sample]
                        #file_sample = 2
                        break

        else:
            output_wavefile = 'sample2.wav'
            wf = wave.open(output_wavefile, 'wb')      # wave file
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(WIDTH)
            wf.setframerate(RATE)
            while (wait == False and file_sample == 2):
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
                    sample_recorded = 1
                    wait = True
                    print "\nFinished recording sample 3"
                    avg_fft[file_sample] = fft_sum/(DURATION * RATE)
                    print "The average is for the third sample is ", avg_fft[file_sample]
                    break

        if(sample_recorded == 1):
            return avg_fft[file_sample]
        

#savevoice(1)
        
