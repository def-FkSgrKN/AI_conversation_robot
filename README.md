# AI_conversation_robot


# DEMO
RCC(立命館コンピュータクラブ)で立命館BKC学園祭で展示したときの様子です
(準備中)

ハードウェアの構造はこちらです。
(準備中)

 
# Features
5種類のキャラクタを用意しました。

[顎の開閉]
音声発声前にサーボモータの角度を10度にする、発生後に120度にすることで顎を開閉させることができます。
既存の対話ロボットでは画面上の絵が動くのみのものが多かったのですが、この対話ロボットでは実世界の物体が挙動している点が異なります。

[音声認識]
googleのspeech_recognitionを使用することで、文章で聞き取ることができます。
5秒で音声認識を強制的に中断させることで、雑音が多い場所でも音声認識し続けるというような不具合がないようにしています。

[自然言語処理]
gpt3.5-turboだけでなく、langchainで会話を記録させることで、人格形成のプロンプトを1回の入力で済ませています。 また、プロンプトを#という区切り文字にしたり、キャラ名やセリフなど日本語でしか表現できない場所以外を英語で表記することで、キャラが設定事項自体を話にくくしています。

[音声合成]
VOICEVOX(https://voicevox.hiroshiba.jp/)を使用することで、機械のようにならず、柔軟な声を出すことができます。

 
# Requirement
 
動作環境
OS:Windows10/11
言語:Python3.8以上
音声合成ソフトVOICEVOX 

ライブラリ
langchain>=0.0.348
serial>=3.5
speech_recognition>=3.8.1
requests>=2.28.2 
json>=2.0.9
sounddevice>=0.4.3
numpy>=1.22.2

# Installation
 
 
```Pythonの導入
https://www.python.org/downloads/
から好きなバージョン(3.8以上)を導入してください

インストール時に環境変数のパスを通す項目があるので必ず✓マークをつけてください
```

ライブラリの導入
```sh
#以下のコマンドを実行 同レポジトリ一番上の階層から
pip install -r requirements.txt
```

VOICEVOXの導入
https://voicevox.hiroshiba.jp/
のダウンロードから導入してください。
(Desktopにショートカットを作成すると起動しやすくなります。)

 
# Usage

(前準備) Servoモータを使用する場合
1. 
同レポジトリ/src/arduino内のPythonSerialServo.inoをArduinoに焼き込みます
(焼き込む際にUSBのPort番号(ex COM4)を確認してください--> Pythonから送る際に使用します)
(Servoモータのライブラリがない場合はご自身で導入の方をお願いします。)
(ArduinoはPCに接続したままにしてください)

2. 
同レポジトリ/src/python内のmove_jay.pyの10行目
```python
self.ser =serial.Serial("COM4", 9600)
```
"COM4"を先ほど確認したPort番号に書き換えます


(前準備) Servoモータを使用しない場合 (ArduinoやServoモータを所有していない)
同レポジトリ/src/python内のmain_process_system_gpt35.pyのサーボモータを使用したくないキャラ
のmain関数を呼び出している行の第3引数 TrueをFalseに変更の上ご使用ください

ex) chara0関数内では main(INIT_PROMPT, speaker, True)が130行目に呼び出されているので
main(INIT_PROMPT, speaker, False)に変更します


(起動)
1. VOICEVOXのアイコンをクリックして起動します
2. 同レポジトリ/src/python内にcdコマンドを使い入り、
```sh
python main_process_system_gpt35.py
```
を実行してください

 
# Note
* プロンプトの口調を変えてみよう!

 
# Author
* Sogo Furukawa
* Ritsumeikan University, club:RCC and Ri-one
* Twitter:https://twitter.com/FkSg16KN
 
# License
"AI_conversation_robot" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
 
