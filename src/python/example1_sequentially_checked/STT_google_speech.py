import time
import speech_recognition as sr
import pyaudio

import numpy as np
import pyopenjtalk


def STT_main(MIC_DEVICE_IDX, TIMEOUT_SEC, PHRASE_TIME_LIMIT_SEC, LANGAGE):

    # マイクの設定    
    r = sr.Recognizer()
    with sr.Microphone(device_index=MIC_DEVICE_IDX) as source:

        #発話の合図を送る
        print("Say something!")
        audio1 = r.listen(source, timeout=TIMEOUT_SEC, phrase_time_limit=PHRASE_TIME_LIMIT_SEC)

        # recognize speech using Google Speech Recognition
        
        try:
            #print("L22")
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            texts1 = r.recognize_google(audio1, language=LANGAGE)
            return texts1

        except sr.UnknownValueError:
            #print("sr.UnknownValueError=" + str(sr.UnknownValueError))
            return "Unknown_Error"

        except sr.RequestError as e:
            #print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "Network_Error"

        
def use_text():
    MIC_DEVICE_IDX = 1
    TIMEOUT_SEC = 60
    PHRASE_TIME_LIMIT_SEC = 5
    LANGAGE = "ja-JP"

    cl_text = STT_main(MIC_DEVICE_IDX, TIMEOUT_SEC, PHRASE_TIME_LIMIT_SEC, LANGAGE)
    print(cl_text)


if __name__ == "__main__":
    use_text()