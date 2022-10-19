import sys

from turtle import width
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
#qt disinener
from gui_xor import Ui_Form
# serial  
import threading 
import signal 
import serial    
# (check point) pip install pyserial

line = [] # 시리얼 통신으로 라인 단위로 데이터 가져올 리스트 변수 
exitThread = False   # 시리얼 통신 쓰레드 종료용 변수 

#윈도우 창
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, width0, height0, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("pyqt widget")
        
        self.width0, self.height0 = width0, height0
        self.setGeometry(10, 30, self.width0, self.height0)
    
    #     self.pushButton.clicked.connect(self.butten_Click)
    # #클릭 이벤트
    # def butten_Click(self):
    #     # self.textBrowser.append("this is a test progam.")
    #     Send_Data()
    def my_fn1(self):
        pass
#비정상 종료 방지
app1 = QApplication.instance()
if app1 is None:
    app1 = QApplication(sys.argv)

width, height = 1280, 720
myWindow1 = MainWindow(width, height)

if __name__ == "__main__":
    myWindow1.show()
    sys.exit(app1.exec_())
