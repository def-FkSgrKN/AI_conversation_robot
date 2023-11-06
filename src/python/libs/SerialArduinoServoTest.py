#パソコン関連もろもろ, Arduinoでサーボを動かす（Pythonとのシリアル通信), https://touch-sp.hatenablog.com/entry/2020/05/20/024607, 2022年5月2日. 

import serial, time

print("Open Port")
ser =serial.Serial("COM4", 9600)
time.sleep(1.5)

angle = 60

while(True):

    a = input('角度入力:')

    if(a == 'q'):
        break

    #40から120までがおすすめ
    try:
        angle = int(a)
        angle = 179 if angle > 179 else angle
        angle = 0 if angle < 0 else angle
    except:
        None

    send_data = angle.to_bytes(1, 'big')
    ser.write(send_data)

while(True):
    a = input('動作入力:')
    FirstArg = 60
    LastArg = 140

    if a == "Close":
        #for i in range(FirstArg, LastArg, 5):
        #    angle = int(i)
        #    data = angle.to_bytes(1, 'big')
        #    ser.write(data)
            #time.sleep(0.01)
        angle = int(10)
        data = angle.to_bytes(1, 'big')
        ser.write(data)
        time.sleep(0.01)

    elif a == "Open":
        #for i in range(LastArg, FirstArg, -5):
        #    angle = int(i)
        #    data = angle.to_bytes(1, 'big')
        #    ser.write(data)
            #time.sleep(0.01)
        angle = int(150)
        data = angle.to_bytes(1, 'big')
        ser.write(data)
        time.sleep(0.01)

    


print("Close Port")
ser.close()