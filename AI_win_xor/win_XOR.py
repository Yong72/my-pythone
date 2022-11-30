import sys

from turtle import width
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
#qt disinener
from gui_xor import Ui_Form

# keras (XOR) 
import fun_XOR
from keras.callbacks import LambdaCallback 
from keras import backend as K   # https://faroit.com/keras-docs/2.0.8/activations/ 
import numpy as np 

global sData 
sData = ""  

class TimerMessageBox(QMessageBox): 

    def __init__(self, width0, height0, timeout=3, parent=None): 
        super(TimerMessageBox, self).__init__(parent) 
        self.height0 = height0 
        self.width0 = width0  
        self.setWindowTitle("wait") 
        self.setGeometry(self.width0,self.height0,1,1)  
        self.time_to_wait = timeout 
        self.setText("Update the weights") 
        self.setStandardButtons(QMessageBox.NoButton) 
        self.timer = QTimer(self) 
        self.timer.setInterval(1) 
        self.timer.timeout.connect(self.changeContent) 
        self.timer.start() 

    def changeContent(self): 
        self.setText("Update the weights") 
        self.time_to_wait -= 1 
        if self.time_to_wait <= 0: 
            self.close() 

    def closeEvent(self, event): 
        self.timer.stop() 
        event.accept() 

#윈도우 창
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, width0, height0, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("XOR Neural Network")
        self.width0, self.height0 = width0, height0
        self.setGeometry(10, 30, self.width0-60, self.height0-60)

        self.pushButton_1.clicked.connect(self.pb1_Clicked)
        self.pushButton_2.clicked.connect(self.pb2_Clicked)

    def pb1_Clicked(self):
        self.clear_callback() 
        fun_XOR.print_np_ver() 
        fun_XOR.print_keras_ver() 
        fun_XOR.bulid_model() 
        fun_XOR.compile_model() 
        fun_XOR.model_2._initial_weights 

        global sData 
        for iCount in range(1,151) :  # range(1,151) => 150회 x 10 = 1500 
            fun_XOR.fit_model(10)
            self.display_weights(iCount)  

    def pb2_Clicked(self):
        #self.display_weights(0)
        fun_XOR.test_model() 

        self.display_weights(0) 

        f = open("str_weights.txt", 'r') 
        line = f.readline() 
        f.close() 
        list_weight_bias = line.split(';')  # line은 1줄 문자열이며, ";"으로 구분 가능  
        float_weight_bias = list(np.float_(list_weight_bias)) 

        # lineEdit_1-2 
        sInData1 = self.lineEdit_1.text() 
        sInData2 = self.lineEdit_2.text() 
        
        sInData = sInData1+';'+ sInData2   # lineEdit로 읽어드린 두 개의 문자열을 구분자(";")를 추가하면서 새로운 한 줄의 문자열로 만듦 
        list_sInData = sInData.split(';')  # 문자열 sInData ";"을 기준으로 쪼개면서 문자열 리스트를 만듦 
        float_InData = list(np.float_(list_sInData)) # 문자열 리스트를 연산이 가능한 실수형 리스트로 데이터형을 변환 
        print("float_InData : ", float_InData)  # print("float_InData : %i" float_InData) # This code has an error. 

        # la_x1_h101-116, la_y1_h101-116 
        # la_x1_h101-116 
        # sum ( 입력값(input) * 가중치(weight) ) + bias 
        float_x1_h101 = float_InData[0]*float_weight_bias[0] + float_InData[1]*float_weight_bias[16] + float_weight_bias[32]   
        float_x1_h102 = float_InData[0]*float_weight_bias[1] + float_InData[1]*float_weight_bias[17] + float_weight_bias[33] 
        float_x1_h103 = float_InData[0]*float_weight_bias[2] + float_InData[1]*float_weight_bias[18] + float_weight_bias[34] 
        float_x1_h104 = float_InData[0]*float_weight_bias[3] + float_InData[1]*float_weight_bias[19] + float_weight_bias[35]
        float_x1_h105 = float_InData[0]*float_weight_bias[4] + float_InData[1]*float_weight_bias[20] + float_weight_bias[36]
        float_x1_h106 = float_InData[0]*float_weight_bias[5] + float_InData[1]*float_weight_bias[21] + float_weight_bias[37]
        float_x1_h107 = float_InData[0]*float_weight_bias[6] + float_InData[1]*float_weight_bias[22] + float_weight_bias[38]
        float_x1_h108 = float_InData[0]*float_weight_bias[7] + float_InData[1]*float_weight_bias[23] + float_weight_bias[39]
        float_x1_h109 = float_InData[0]*float_weight_bias[8] + float_InData[1]*float_weight_bias[24] + float_weight_bias[40]
        float_x1_h110 = float_InData[0]*float_weight_bias[9] + float_InData[1]*float_weight_bias[25] + float_weight_bias[41]
        float_x1_h111 = float_InData[0]*float_weight_bias[10] + float_InData[1]*float_weight_bias[26] + float_weight_bias[42]
        float_x1_h112 = float_InData[0]*float_weight_bias[11] + float_InData[1]*float_weight_bias[27] + float_weight_bias[43]
        float_x1_h113 = float_InData[0]*float_weight_bias[12] + float_InData[1]*float_weight_bias[28] + float_weight_bias[44]
        float_x1_h114 = float_InData[0]*float_weight_bias[13] + float_InData[1]*float_weight_bias[29] + float_weight_bias[45]
        float_x1_h115 = float_InData[0]*float_weight_bias[14] + float_InData[1]*float_weight_bias[30] + float_weight_bias[46]
        float_x1_h116 = float_InData[0]*float_weight_bias[15] + float_InData[1]*float_weight_bias[31] + float_weight_bias[47]

        self.la_x1_h101.setText(format(float_x1_h101, ".6f")) 
        self.la_x1_h102.setText(format(float_x1_h102, ".6f")) 
        self.la_x1_h103.setText(format(float_x1_h103, ".6f"))
        self.la_x1_h104.setText(format(float_x1_h104, ".6f"))
        self.la_x1_h105.setText(format(float_x1_h105, ".6f"))
        self.la_x1_h106.setText(format(float_x1_h106, ".6f"))
        self.la_x1_h107.setText(format(float_x1_h107, ".6f"))
        self.la_x1_h108.setText(format(float_x1_h108, ".6f"))
        self.la_x1_h109.setText(format(float_x1_h109, ".6f"))
        self.la_x1_h110.setText(format(float_x1_h110, ".6f"))
        self.la_x1_h111.setText(format(float_x1_h111, ".6f"))
        self.la_x1_h112.setText(format(float_x1_h112, ".6f"))
        self.la_x1_h113.setText(format(float_x1_h113, ".6f"))
        self.la_x1_h114.setText(format(float_x1_h114, ".6f"))
        self.la_x1_h115.setText(format(float_x1_h115, ".6f"))
        self.la_x1_h116.setText(format(float_x1_h116, ".6f"))

        # la_y1_h101-116 
        float_y1_h101 = K.relu(float_x1_h101, alpha=0.0, max_value=None)  # relu 함수   
        float_y1_h102 = K.relu(float_x1_h102, alpha=0.0, max_value=None) 
        float_y1_h103 = K.relu(float_x1_h103, alpha=0.0, max_value=None)
        float_y1_h104 = K.relu(float_x1_h104, alpha=0.0, max_value=None)
        float_y1_h105 = K.relu(float_x1_h105, alpha=0.0, max_value=None)
        float_y1_h106 = K.relu(float_x1_h106, alpha=0.0, max_value=None)
        float_y1_h107 = K.relu(float_x1_h107, alpha=0.0, max_value=None)
        float_y1_h108 = K.relu(float_x1_h108, alpha=0.0, max_value=None)
        float_y1_h109 = K.relu(float_x1_h109, alpha=0.0, max_value=None)
        float_y1_h110 = K.relu(float_x1_h110, alpha=0.0, max_value=None)
        float_y1_h111 = K.relu(float_x1_h111, alpha=0.0, max_value=None)
        float_y1_h112 = K.relu(float_x1_h112, alpha=0.0, max_value=None)
        float_y1_h113 = K.relu(float_x1_h113, alpha=0.0, max_value=None)
        float_y1_h114 = K.relu(float_x1_h114, alpha=0.0, max_value=None)
        float_y1_h115 = K.relu(float_x1_h115, alpha=0.0, max_value=None)
        float_y1_h116 = K.relu(float_x1_h116, alpha=0.0, max_value=None)

        self.la_y1_h101.setText(format(float_y1_h101, ".6f")) 
        self.la_y1_h102.setText(format(float_y1_h102, ".6f")) 
        self.la_y1_h103.setText(format(float_y1_h103, ".6f"))
        self.la_y1_h104.setText(format(float_y1_h104, ".6f"))
        self.la_y1_h105.setText(format(float_y1_h105, ".6f"))
        self.la_y1_h106.setText(format(float_y1_h106, ".6f"))
        self.la_y1_h107.setText(format(float_y1_h107, ".6f"))
        self.la_y1_h108.setText(format(float_y1_h108, ".6f"))
        self.la_y1_h109.setText(format(float_y1_h109, ".6f"))
        self.la_y1_h110.setText(format(float_y1_h110, ".6f"))
        self.la_y1_h111.setText(format(float_y1_h111, ".6f"))
        self.la_y1_h112.setText(format(float_y1_h112, ".6f"))
        self.la_y1_h113.setText(format(float_y1_h113, ".6f"))
        self.la_y1_h114.setText(format(float_y1_h114, ".6f"))
        self.la_y1_h115.setText(format(float_y1_h115, ".6f"))
        self.la_y1_h116.setText(format(float_y1_h116, ".6f"))

        # la_x1_out1, la_y1_out1 
        # la_x1_out1 
        # sum ( 입력값(input) * 가중치(weight) ) + bias 
        float_x1_out =              + float_y1_h101*float_weight_bias[48]  
        float_x1_out = float_x1_out + float_y1_h102*float_weight_bias[49]  
        float_x1_out = float_x1_out + float_y1_h103*float_weight_bias[50]  
        float_x1_out = float_x1_out + float_y1_h104*float_weight_bias[51]
        float_x1_out = float_x1_out + float_y1_h105*float_weight_bias[52]
        float_x1_out = float_x1_out + float_y1_h106*float_weight_bias[53]
        float_x1_out = float_x1_out + float_y1_h107*float_weight_bias[54]
        float_x1_out = float_x1_out + float_y1_h108*float_weight_bias[55]
        float_x1_out = float_x1_out + float_y1_h109*float_weight_bias[56]
        float_x1_out = float_x1_out + float_y1_h110*float_weight_bias[57]
        float_x1_out = float_x1_out + float_y1_h111*float_weight_bias[58]
        float_x1_out = float_x1_out + float_y1_h112*float_weight_bias[59]
        float_x1_out = float_x1_out + float_y1_h113*float_weight_bias[60]
        float_x1_out = float_x1_out + float_y1_h114*float_weight_bias[61]
        float_x1_out = float_x1_out + float_y1_h115*float_weight_bias[62]
        float_x1_out = float_x1_out + float_y1_h116*float_weight_bias[63]
        float_x1_out = float_x1_out + float_weight_bias[64] # bias 
        self.la_x1_out1.setText(format(float_x1_out, ".6f")) 

        # la_y1_out1 
        float_y1_out1 = K.sigmoid(float_x1_out)   # sigmoid 함수   
        self.la_y1_out1.setText(format(float_y1_out1, ".6f")) 

        # la_target1, la_error1 
        if ((float_InData[0] == 0) and (float_InData[1] == 0 )) :  
            self.la_target1.setText("0") 
            error1 = 0 - float_y1_out1 
            self.la_error1.setText(format(error1, ".6f")) 

        elif ((float_InData[0] == 1) and (float_InData[1] == 0 )) :  
            self.la_target1.setText("1") 
            error1 = 1 - float_y1_out1 
            self.la_error1.setText(format(error1, ".6f")) 

        elif((float_InData[0] == 0) and (float_InData[1] == 1 )) :  
            self.la_target1.setText("1") 
            error1 = 1 - float_y1_out1 
            self.la_error1.setText(format(error1, ".6f")) 

        elif((float_InData[0] == 1) and (float_InData[1] == 1 )) :  
            self.la_target1.setText("0") 
            error1 = 0 - float_y1_out1 
            self.la_error1.setText(format(error1, ".6f")) 

        else :  
            self.la_target1.setText("0.00") 
            self.la_error1.setText("0.00") 


        # This code has any problem that is unknown. 
        pred1 = fun_XOR.model_predict(float_InData) 
        self.la_target1.setText(f'{pred1[1]}') 
        

         
        # QMessageBox 예제 (양호) 
        dlg = QMessageBox(self) 
        dlg.setWindowTitle("MessageBox : 연산결과") 
        dlg.setText("입력값에 대한 추론(연산)을 완료하였습니다.") 
        dlg.exec() 

    def save_lamda(self, data11):
        # save_lamda_weight(self, data11)함수용 소 

        n1 = len(data11)  # list의 길이(개수)를 파악 
        A11 = data11[n1-4][0] # list 개수만큼 데이터를 분리 
        A12 = data11[n1-4][1]  
        B1 = data11[n1-3]      # list의 시작은 0번 부터 
        C1 = data11[n1-2] 
        D1 = data11[n1-1]  

#  File "f:\01\05\교재2\Tensorflow20\XOR11\gui_XOR_220812.py", line 95, in save_lamda_weight 
#    A12 = data11[n1-4][1] 
#IndexError: index 1 is out of bounds for axis 0 with size 1 

        sA11 = ' '.join(str(e) for e in A11) # list 데이터 안에 숫자를 모두 문자열로 변경 : str(e) for e in A1 
        sA12 = ' '.join(str(e) for e in A12) 
        sB1 = ' '.join(str(e) for e in B1) # 공백(' ')으로 데이터를 모두 합치기 
        sC1 = ' '.join(str(e) for e in C1) 
        sD1 = ' '.join(str(e) for e in D1) 

        sA11 = sA11.replace("[","")  # "[" 제거 
        sA11 = sA11.replace("]","")  # "]" 제거 
        sA11 = sA11.replace(","," ") # "," 제거하고 공백(" ") 추가 
        sA12 = sA12.replace("[","")  # s : String 
        sA12 = sA12.replace("]","") 
        sA12 = sA12.replace(","," ") 
        sB1 = sB1.replace("[","")   
        sB1 = sB1.replace("]","") 
        sB1 = sB1.replace(","," ") 
        sC1 = sC1.replace("[","") 
        sC1 = sC1.replace("]","") 
        sC1 = sC1.replace(","," ") 
        sD1 = sD1.replace("[","") 
        sD1 = sD1.replace("]","") 
        sD1 = sD1.replace(","," ") 

        ltA11 = sA11.split() # split()함수에 특정 문자를 지정하지 않았기 때문에  
        ltA12 = sA12.split() 
        ltB1 = sB1.split()  # 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다. 
        ltC1 = sC1.split()  # lt : list 
        ltD1 = sD1.split() 

        sA11 = ';'.join(ltA11) # 구분자로 ';'를 사용하여 데이터를 모두 다시 합치기 
        sA12 = ';'.join(ltA12) 
        sB1 = ';'.join(ltB1) 
        sC1 = ';'.join(ltC1) 
        sD1 = ';'.join(ltD1)         

        # sdata11 = sA11+','+sA12+','+sB1+','+sC1+','+sD1 
        sdata11 = sA11+';'+sA12+';'+sB1+';'+sC1+';'+sD1 

        f2 = open("str_weights.txt", 'w') # 파일에 저장 
        f2.write(sdata11) 
        f2.close()  

        f = open("weights00.txt", 'w') # 파일에 저장 
        f.write(f'{A11}')  # la_w_in1_h101-116, la_w_in2_h101-116 
        f.write('\n\n') 
        f.write(f'{A12}')  # la_w_in1_h101-116, la_w_in2_h101-116 
        f.write('\n\n') 
        f.write(f'{B1}')   # la_bias1_h101-116  
        f.write('\n\n') 
        f.write(f'{C1}')   # la_w_h101_out1-116 
        f.write('\n\n') 
        f.write(f'{D1}')   # la_bias1_out1         
        f.close() 

    def clear_callback(self):
        # clear_cal_data(self)함수용 소스 

        self.lineEdit_1.setText("Vector_1") 
        self.lineEdit_2.setText("Vector_2") 

        self.la_x1_h101.setText("Don't display") # "N/A" : Not Applicable, 해당 사항 없음 
        self.la_x1_h102.setText("Don't display") # Don't display : 표시 안 함 
        self.la_x1_h103.setText("Don't display") 
        self.la_x1_h104.setText("Don't display") 
        self.la_x1_h105.setText("Don't display") 
        self.la_x1_h106.setText("Don't display") 
        self.la_x1_h107.setText("Don't display") 
        self.la_x1_h108.setText("Don't display") 
        self.la_x1_h109.setText("Don't display") 
        self.la_x1_h110.setText("Don't display") 
        self.la_x1_h111.setText("Don't display") 
        self.la_x1_h112.setText("Don't display") 
        self.la_x1_h113.setText("Don't display") 
        self.la_x1_h114.setText("Don't display") 
        self.la_x1_h115.setText("Don't display") 
        self.la_x1_h116.setText("Don't display") 

        self.la_y1_h101.setText("Don't display") 
        self.la_y1_h102.setText("Don't display") 
        self.la_y1_h103.setText("Don't display") 
        self.la_y1_h104.setText("Don't display") 
        self.la_y1_h105.setText("Don't display") 
        self.la_y1_h106.setText("Don't display") 
        self.la_y1_h107.setText("Don't display") 
        self.la_y1_h108.setText("Don't display") 
        self.la_y1_h109.setText("Don't display") 
        self.la_y1_h110.setText("Don't display") 
        self.la_y1_h111.setText("Don't display") 
        self.la_y1_h112.setText("Don't display") 
        self.la_y1_h113.setText("Don't display") 
        self.la_y1_h114.setText("Don't display") 
        self.la_y1_h115.setText("Don't display") 
        self.la_y1_h116.setText("Don't display") 

        self.la_x1_out1.setText("Don't display") 
        self.la_y1_out1.setText("Don't display") 

        self.la_target1.setText("Lable") 
        self.la_error1.setText("Don't display")   

    def display_weights(self, count):
        # display_weights(self, count)함수용 소스 

        self.la_epoch.setText(str(count*5)) 
        f = open("str_weights.txt", 'r') 
        line = f.readline() 
        f.close() 
        data1 = line.split(';')  # line은 1줄 문자열이며, ";"으로 구분 가능  
        n_data1 = len(data1)     # data1은 문자열 리스트. 개수는 총 65개 
        float_data1 = list(np.float_(data1)) 

        # print("n_data1 : %d" %n_data1) 
        # print("data1 : %s" %data1) 
        # print("float_data1 : %s" %float_data1) 
        # la_w_in1_h101-116, la_w_in2_h101-116, la_bias1_h101-116 
        # la_w_in1_h101-116
        self.la_w_in1_h101.setText(format(float_data1[0], ".6f")) 
        self.la_w_in1_h102.setText(format(float_data1[1], ".6f")) 
        self.la_w_in1_h103.setText(format(float_data1[2], ".6f")) 
        self.la_w_in1_h104.setText(format(float_data1[3], ".6f")) 
        self.la_w_in1_h105.setText(format(float_data1[4], ".6f")) 
        self.la_w_in1_h106.setText(format(float_data1[5], ".6f")) 
        self.la_w_in1_h107.setText(format(float_data1[6], ".6f")) 
        self.la_w_in1_h108.setText(format(float_data1[7], ".6f")) 
        self.la_w_in1_h109.setText(format(float_data1[8], ".6f")) 
        self.la_w_in1_h110.setText(format(float_data1[9], ".6f")) 
        self.la_w_in1_h111.setText(format(float_data1[10], ".6f")) 
        self.la_w_in1_h112.setText(format(float_data1[11], ".6f")) 
        self.la_w_in1_h113.setText(format(float_data1[12], ".6f")) 
        self.la_w_in1_h114.setText(format(float_data1[13], ".6f")) 
        self.la_w_in1_h115.setText(format(float_data1[14], ".6f")) 
        self.la_w_in1_h116.setText(format(float_data1[15], ".6f")) 

        # la_w_in2_h101-116 
        self.la_w_in2_h101.setText(format(float_data1[16], ".6f")) 
        self.la_w_in2_h102.setText(format(float_data1[17], ".6f")) 
        self.la_w_in2_h103.setText(format(float_data1[18], ".6f")) 
        self.la_w_in2_h104.setText(format(float_data1[19], ".6f")) 
        self.la_w_in2_h105.setText(format(float_data1[20], ".6f")) 
        self.la_w_in2_h106.setText(format(float_data1[21], ".6f")) 
        self.la_w_in2_h107.setText(format(float_data1[22], ".6f")) 
        self.la_w_in2_h108.setText(format(float_data1[23], ".6f")) 
        self.la_w_in2_h109.setText(format(float_data1[24], ".6f")) 
        self.la_w_in2_h110.setText(format(float_data1[25], ".6f")) 
        self.la_w_in2_h111.setText(format(float_data1[26], ".6f")) 
        self.la_w_in2_h112.setText(format(float_data1[27], ".6f")) 
        self.la_w_in2_h113.setText(format(float_data1[28], ".6f")) 
        self.la_w_in2_h114.setText(format(float_data1[29], ".6f")) 
        self.la_w_in2_h115.setText(format(float_data1[30], ".6f")) 
        self.la_w_in2_h116.setText(format(float_data1[31], ".6f")) 

        # la_bias1_h101-116 
        self.la_bias1_h101.setText(format(float_data1[32], ".6f")) 
        self.la_bias1_h102.setText(format(float_data1[33], ".6f")) 
        self.la_bias1_h103.setText(format(float_data1[34], ".6f")) 
        self.la_bias1_h104.setText(format(float_data1[35], ".6f")) 
        self.la_bias1_h105.setText(format(float_data1[36], ".6f")) 
        self.la_bias1_h106.setText(format(float_data1[37], ".6f")) 
        self.la_bias1_h107.setText(format(float_data1[38], ".6f")) 
        self.la_bias1_h108.setText(format(float_data1[39], ".6f")) 
        self.la_bias1_h109.setText(format(float_data1[40], ".6f")) 
        self.la_bias1_h110.setText(format(float_data1[41], ".6f")) 
        self.la_bias1_h111.setText(format(float_data1[42], ".6f")) 
        self.la_bias1_h112.setText(format(float_data1[43], ".6f")) 
        self.la_bias1_h113.setText(format(float_data1[44], ".6f")) 
        self.la_bias1_h114.setText(format(float_data1[45], ".6f")) 
        self.la_bias1_h115.setText(format(float_data1[46], ".6f")) 
        self.la_bias1_h116.setText(format(float_data1[47], ".6f")) 

    # la_w_h101-116_out1, la_bias1_out1 
    # la_w_h101-116_out1 
        self.la_w_h101_out1.setText(format(float_data1[48], ".6f")) 
        self.la_w_h102_out1.setText(format(float_data1[49], ".6f")) 
        self.la_w_h103_out1.setText(format(float_data1[50], ".6f")) 
        self.la_w_h104_out1.setText(format(float_data1[51], ".6f")) 
        self.la_w_h105_out1.setText(format(float_data1[52], ".6f")) 
        self.la_w_h106_out1.setText(format(float_data1[53], ".6f")) 
        self.la_w_h107_out1.setText(format(float_data1[54], ".6f")) 
        self.la_w_h108_out1.setText(format(float_data1[55], ".6f")) 
        self.la_w_h109_out1.setText(format(float_data1[56], ".6f")) 
        self.la_w_h110_out1.setText(format(float_data1[57], ".6f")) 
        self.la_w_h111_out1.setText(format(float_data1[58], ".6f")) 
        self.la_w_h112_out1.setText(format(float_data1[59], ".6f")) 
        self.la_w_h113_out1.setText(format(float_data1[60], ".6f")) 
        self.la_w_h114_out1.setText(format(float_data1[61], ".6f")) 
        self.la_w_h115_out1.setText(format(float_data1[62], ".6f")) 
        self.la_w_h116_out1.setText(format(float_data1[63], ".6f"))        

    # la_bias1_out1 
        self.la_bias_out1.setText(format(float_data1[64], ".6f")) 
        messagebox = TimerMessageBox(self.width0, self.height0, 0.01, self)  # 화면 밖에 메세지 박스를 그리도록 설정함 
        messagebox.exec()   
    
#비정상 종료 방지
app1 = QApplication.instance()
if app1 is None:
    app1 = QApplication(sys.argv)

screen = app1.primaryScreen() 
screen_size = screen.size() 
width, height = screen_size.width(), screen_size.height() 

myWindow1 = MainWindow(width, height)

print_weights = LambdaCallback(on_epoch_end=lambda epoch,
    logs: myWindow1.save_lamda(fun_XOR.model_2.get_weights()) )  

if __name__ == "__main__":
    myWindow1.show()
    sys.exit(app1.exec())
