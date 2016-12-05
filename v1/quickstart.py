

def micinput():
    import struct
    import wave
    import pyaudio
    import os
    WIDTH = 2           # bytes per sample
    CHANNELS = 1
    RATE = 16000        # Sampling rate (samples/second)
    BLOCKSIZE = 1024
    DURATION = 2      # Duration in seconds

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
        'mic_input.wav')
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

micinput()
def run_quickstart():
    # [START speech_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import speech

    # Instantiates a client
    speech_client = speech.Client()

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'author.wav')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio_sample = speech_client.sample(
            content,
            source_uri=None,
            encoding='LINEAR16',
            sample_rate=16000)

    # Detects speech in the audio file
    alternatives = speech_client.speech_api.sync_recognize(audio_sample)

    for alternative in alternatives:
        print('Transcript: {}'.format(alternative.transcript))
    # [END speech_quickstart]


if __name__ == '__main__':
    run_quickstart()
