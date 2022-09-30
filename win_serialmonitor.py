#윈도우 창을 이용해서 아두이노 시리얼 모니터를 띄운다

import sys

from turtle import width
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from gui_serialmonitor import Ui_Dialog

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
        self.textBrowser.append("this is a trst progam.")

    def my_fn1(self):
        pass
#비정상 종료 방지
app1 = QApplication.instance()
if app1 is None:
    app1 = QApplication(sys.argv)

width, height = 710, 540
myWindow1 = MainWindow(width, height)

if __name__ == '__main__':
    myWindow1.show()
    sys.exit(app1.exec_())




    