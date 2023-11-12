from STT_google_speech import STT_main
from NLP_gpt4free_api import NLP_main
from TTS_voicevox_local_api import TTC_voicevox_local_api_chara



def main():

    STATES = {"MOVE_STT":0, "MOVE_NLP":1, "MOVE_TTS":2} #状態遷移で管理する
    now_state = STATES["MOVE_STT"] #現在の状態を保持する
    #now_state = STATES["MOVE_NLP"]
   
    
    while True:


        
        if now_state == STATES["MOVE_STT"]:

            """
            音声認識部分
            """

            MIC_DEVICE_IDX = 1
            TIMEOUT_SEC = 60
            PHRASE_TIME_LIMIT_SEC = 5
            LANGAGE = "ja-JP"

            cl_txt = STT_main(MIC_DEVICE_IDX, TIMEOUT_SEC, PHRASE_TIME_LIMIT_SEC, LANGAGE)
            #print(cl_text)
            now_state = STATES["MOVE_NLP"]


        
            
        elif now_state == STATES["MOVE_NLP"]:
            """
            自然言語処理部分
            """

            PROMPT_front = '''
                            Please provide your response(Japanese) to user's lines entered by the user in the json format below.
                            {'''

            PROMPT_json_format = f'''
                                "user's statement":"{cl_txt}",
                                "assistant's statement":output'''
                            
            PROMPT_back = '''
                            }
                            '''
            
            ALL_PROMPT = PROMPT_front + PROMPT_json_format + PROMPT_back

            print("ALL_PROMPT=")
            print(ALL_PROMPT)

            MODEL = "gpt-3.5-turbo"

            res_txt = NLP_main(ALL_PROMPT, MODEL, output_key_idx=1)
            print("res_txt = " + res_txt)

            #成功したら
            if res_txt != "NLP_func_ERROR":
                now_state = STATES["MOVE_TTS"]
                


        elif now_state == STATES["MOVE_TTS"]:
            """
            音声合成部分
            """

            TTS_zundamon_class = TTC_voicevox_local_api_chara(speaker=2)
            #TTS_zundamon_class.TTS_main("こんにちはー!")
            TTS_zundamon_class.TTS_main(res_txt)

            now_state = STATES["MOVE_STT"]



if __name__ == "__main__":
    main()

    