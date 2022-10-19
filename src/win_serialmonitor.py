#윈도우 창을 이용해서 아두이노 시리얼 모니터를 띄운다

import sys

from turtle import width
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
#qt disinener
from gui_serialmonitor import Ui_Dialog
# serial  
import threading 
import signal 
import serial    
# (check point) pip install pyserial

line = [] # 시리얼 통신으로 라인 단위로 데이터 가져올 리스트 변수 
exitThread = False   # 시리얼 통신 쓰레드 종료용 변수 

#윈도우 창
class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, width0, height0, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("pyqt widget")
        
        self.width0, self.height0 = width0, height0
        self.setGeometry(10, 30, self.width0, self.height0)
    
        self.pushButton.clicked.connect(self.butten_Click)
    #클릭 이벤트
    def butten_Click(self):
        # self.textBrowser.append("this is a test progam.")
        Send_Data()
    def my_fn1(self):
        pass
#비정상 종료 방지
app1 = QApplication.instance()
if app1 is None:
    app1 = QApplication(sys.argv)

width, height = 710, 540
myWindow1 = MainWindow(width, height)

# 시리얼 통신 쓰레드 종료용 시그널 함수 
def handler(signum, frame): 
     exitThread = True 

# 시리얼 통신 읽기 쓰레드 
def readThread(ser): 
    global line 
    global exitThread 

    # 쓰레드 종료될때까지 계속 돌림 
    while not exitThread: 
        #데이터가 있있다면 
        for c in ser.read(): 
            #line 변수에 차곡차곡 추가하여 넣는다. 
            line.append(chr(c)) 

            if (c == 10) or (c == 13): #라인의 끝을 만나면..  
                # 새줄(New Line/Line Feed-다음줄로) : 'ascii' 10 
                #데이터 처리 함수로 호출 
                strLine = "".join(line)   # 문자리스트를 문자열로 변환 : "".joint(char[]) 
                # strLine을 이용한 소스를 여기에 추가하세요.
                myWindow1.textBrowser.append(strLine)
                del line[:] #line 변수 초기화 

def Send_Data():  # Function of the button  

    ser.write(bytes(myWindow1.lineEdit.text()+'\r\n', encoding='ascii'))  # ser.write(bytes('C01\r\n', encoding='ascii'))    

signal.signal(signal.SIGINT, handler) #종료 시그널 등록 
ser = serial.Serial("COM3", 115200) 
thread = threading.Thread(target=readThread, args=(ser,)) #시리얼 읽기 쓰레드 생성 

if __name__ == '__main__':
    thread.start()#시리얼 스래드 읽기 시작
    myWindow1.show()
    sys.exit(app1.exec_())

#MY Aduino com port to 3
