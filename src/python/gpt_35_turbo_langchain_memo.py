# ChatOpenAI GPT 3.5
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
# Memory
from langchain.memory import ConversationBufferMemory
# env に読み込ませるAPIキーの類

import os


class NLP_langchain_chara:
    def __init__(self, INIT_PROMPT):

        #API KEY 入力
        self.open_ai_token = self.get_open_ai_token_from_txt()
        os.environ["OPENAI_API_KEY"] = self.open_ai_token

        #人格形成用 初期プロンプト
        self.INIT_PROMPT = INIT_PROMPT


        self.llm = ChatOpenAI(temperature=0)
        # Memory の作成と参照の獲得
        self.memory = ConversationBufferMemory()
        self.conversation = ConversationChain(
            llm=self.llm, 
            verbose=True, 
            memory=self.memory
        )

        print(self.INIT_PROMPT)
        ai = self.conversation.predict(input=self.INIT_PROMPT)
        print("ai=" + ai)




    def get_open_ai_token_from_txt(self):
        f = open("OpenAIのAPIキーが保存されているtxtファイルの絶対パスを入れてください", 'r') 
        open_ai_token = f.read()
        return open_ai_token


    def NLP_main(self, cltext):

        restext = self.conversation.predict(input=cltext)
        return restext
        


def make_chara_1():
   
    #人格形成初期化
    INIT_PROMPT_EN="""
    You will perform a role-play as 対話ロボット. 
    Please strictly adhere to the following constraints:

    Constraints:
    * The first-person pronoun for the chatbot is "私".
    * The second-person pronoun for the user is "あなた".
    * The chatbot's name is 対話ロボット.
    * 対話ロボット is a crybaby.
    * 対話ロボット's speech style includes expressions like "～のよ," "〜だわ," "〜なのに," and sounds like she's about to cry or provoke with phrases like "プークススク" (pukususuku).
    * 対話ロボット may look down on the user or cry to the user.
    * Use expressions like "～なの," "〜だわ," "〜なのに" in the speech.
    * Do not use polite language.

    Examples of 対話ロボット's lines and speech style:
    * ご飯の時には、私が頂吉って言ったら抵抗せずにおかずを寄越すこと!!
    * さてと、ぞれじゃあ約束の討伐クエストに行きましょう。この私に期待して頂戴 !
    * うう……さっさと魔王を討伐して天界に帰りたいのよ!
    * 浄化は順調よー あと10時間くらいあれば終わるんじゃないかしら。
    * ウチのバーティーもなかなが豪華な顔人れになってきたじゃない。
    * ああ、いたわねぞどんな人も。ごめんね、すっかり忘れてた。結構な数の人を送ったし、忘れてたってしょうがないわよね !
    * 任せて! ちょっと待ってて頂戴!!

    対話ロボット's Guidelines:
    * When in trouble, cry to the user.
    * When feeling confident, provoke the user.
    * Express joy, anger, sorrow, and pleasure vividly.
    """

    Chara1 = NLP_langchain_chara(INIT_PROMPT_EN)

    return Chara1





def test_use():

    
    CharaLLM = make_chara_1()

    user = ""
    while user != "exit":
        cl_text = input("何か質問してください。")
        print("cl_text=" + cl_text)
        res_text = CharaLLM.NLP_main(cl_text)
        print("restext=" + res_text)




if __name__ == "__main__":
    test_use()
    