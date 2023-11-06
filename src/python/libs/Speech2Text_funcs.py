import time
import speech_recognition as sr
import pyaudio

import numpy as np
import pyopenjtalk




# マイクの設定
MIC_DEVICE_IDX = 1
r = sr.Recognizer()
with sr.Microphone(device_index=MIC_DEVICE_IDX) as source:

    TIMEOUT_SEC = 60
    PHRASE_TIME_LIMIT_SEC = 5

    while True:

        print("Say something!")
        #r.adjust_for_ambient_noise(source)
        #audio = r.listen(source)
        audio1 = r.listen(source, timeout=TIMEOUT_SEC, phrase_time_limit=PHRASE_TIME_LIMIT_SEC)
        print("audio1=" + str(audio1))

        # recognize speech using Google Speech Recognition
        
        try:
            #print("L22")
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            texts1 = r.recognize_google(audio1, language="ja-JP")
            print("texts1=" + texts1)

            #texts2 = r.recognize_google(audio2, language="ja-JP")
            #print("texts1=" + texts2)


            #texts2 = r.recognize_google(audio2, language="ja-JP")
            #print("texts1=" + texts2)
            #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))


        except sr.UnknownValueError:
            print("sr.UnknownValueError=" + str(sr.UnknownValueError))
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        #time.sleep(0.1)

