#パソコン関連もろもろ, Arduinoでサーボを動かす（Pythonとのシリアル通信), https://touch-sp.hatenablog.com/entry/2020/05/20/024607, 2022年5月2日. 
from cgi import test
import serial
import time
from UDP_Socket_module import make_server_socket, socket_receve_data, close_socket

class Serial_Move_Jay():

    def __init__(self):
        print("Open Port")
        self.ser =serial.Serial("COM4", 9600)
        time.sleep(3)

        self.STATE_DIC = {"Other":0, "Speeching":1}
        self.now_state = self.STATE_DIC["Other"]

        #顎を開閉させるときに必要なサーボモータの動作角度
        self.ANGLE_MIN = 60 #[deg]
        self.ANGLE_MAX = 120 #[deg]
        self.SLEEP_TIME = 0.5 #[s]

        #主処理との通信Socketを初期化
        self.HOST = "127.0.0.1"
        self.PORT = 5000
        self.server_socket = make_server_socket(self.HOST, self.PORT)
        self.MSG_DIC = {"Stop":0, "Speeching":1, "Close":2}

        #主処理からmsgを受け取る
        self.MESSAGE_SIZE = 8192

    def Send_Servo_Angle(self, angle):
        send_data = angle.to_bytes(1, 'big')
        self.ser.write(send_data)

    def main(self):

        while self.now_state == self.STATE_DIC["Speeching"]:

            self.Send_Servo_Angle(self.ser, self.ANGLE_MIN)
            time.sleep(self.SLEEP_TIME)

            self.Send_Servo_Angle(self.ser, self.ANGLE_MAX)
            time.sleep(self.SLEEP_TIME)



        


    """
    def main(self):        

        while(True):

            message, address = socket_receve_data(self.server_socket, self.MESSAGE_SIZE)
            print("message=" + message + ", address=" + str(address))

            #主処理からのmsgで状態を変える
            if message == str(self.MSG_DIC["Stop"]):
                now_state = self.STATE_DIC["Other"]

            elif message == str(self.MSG_DIC["Speeching"]):
                now_state = self.STATE_DIC["Speeching"]

            elif message == str(self.MSG_DIC["Close"]):
                break

            print("now_state=" + str(now_state) + "\n")

            #発話状態のときに顎を開閉する
            if now_state == self.STATE_DIC["Speeching"]:    

                self.Send_Servo_Angle(self.ser, self.ANGLE_MIN)
                time.sleep(self.SLEEP_TIME)

                self.Send_Servo_Angle(self.ser, self.ANGLE_MAX)
                time.sleep(self.SLEEP_TIME)


        print("Close Port")
        self.ser.close()
        close_socket()
    """

def test_use():
    smj = Serial_Move_Jay()

    smj.now_state = smj.MSG_DIC["Speeching"]
    smj.main()

    time.sleep(2)
    smj.now_state = smj.MSG_DIC["Other"]



if __name__ == "__main__":
   test_use()