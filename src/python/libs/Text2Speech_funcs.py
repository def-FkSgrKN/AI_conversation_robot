import pyaudio
import numpy as np
import pyopenjtalk


def tts_by_openjtalk(sentence):

    wave, sampling_rate = pyopenjtalk.tts(sentence)

    p = pyaudio.PyAudio()
    """
    pyaudio.paFloat32, np.float32でやると音声が砂嵐でホラー
    """
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, frames_per_buffer = len(wave))


    stream.write(wave.astype(np.int16).tostring())
    stream.stop_stream()
    stream.close()



def main_use():
    tts_by_openjtalk("こんにちは")


if __name__ == "__main__":
    main_use()