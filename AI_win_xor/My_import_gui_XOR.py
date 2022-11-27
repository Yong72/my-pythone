import numpy as np                          # 1. Numpy 가져오기 
import keras                                # 3. Keras 패키지 가져오기 
from keras.models import Sequential 
from keras.layers import Dense 
# from keras.callbacks import LambdaCallback 
from keras import backend as K   # https://faroit.com/keras-docs/2.0.8/activations/ 

import My_xor # import    

# 2. 입력/출력 데이터 만들기 + model 생성 
X2 = np.array([[0,0],[1,0],[0,1],[1,1]]) 
Y2 = np.array([[0],[1],[1],[0]]) 

model_2 = Sequential() 
# gui_xor파일 안의 XOR01 클래스 기능의 함수화 

def print_np_ver() :  
    print(np.__version__) 

def print_keras_ver() : 
    print(keras.__version__) 

def bulid_model() : # 4. Perceptron 모델 생성 
    # model_2 = Sequential() 
    model_2.add(Dense(units=16,input_dim=2, activation='relu')) 
    # model_2.add(Dense(units=32,activation='softmax')) 
    model_2.add(Dense(units=1, activation='sigmoid')) 

def compile_model() :   # 5. Compile - Optimizer, Loss function 설정 
    model_2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 

 
 

def fit_model(EPOCHS) :       # 6. 학습시키기 
    # model_2.fit(X2,Y2, batch_size=1, epochs=1500, shuffle=True, verbose=0, callbacks=[gui_XOR_220722.batch_print_callback, gui_XOR_220722.print_weights]) 
    # model_2.fit(X2,Y2, batch_size=1, epochs=1500, shuffle=True, verbose=0, callbacks=[gui_XOR_220722.print_weights]) 
    # model_2.fit(X2,Y2, batch_size=1, epochs=EPOCHS, shuffle=True, verbose=0, callbacks=[gui_XOR_220722.print_weights]) 
    model_2.fit(X2,Y2, batch_size=1, epochs=EPOCHS, shuffle=True, verbose=0, callbacks=[My_xor.print_weights]) 

def test_model() :      # 7. 모델 테스트하기1 
    test = np.array([[0,0],[1,0],[0,1],[1,1]])  # test data 입력 
    pred = model_2.predict(test) 
    print(pred) 

def model_predict(np) :      # 7. 모델 테스트하기2 
    pred = model_2.predict(np) 
    print(pred) 
    return pred 

def print_weight_test_model() : 
    print(model_2.get_weights()) 

# =========================================================================================================================== 
# https://www.codementor.io/@nitinsurya/how-to-re-initialize-keras-model-weights-et41zre2g 
# Keras 모델 가중치를 다시 초기화하는 방법 
# from keras import backend as K   # https://faroit.com/keras-docs/2.0.8/activations/ # this code has an error. # import tensorflow.python.keras.backend as K 

def reset_weights(model): 
    session1 = K.get_session() 
    for layer in model_2.layers :  
        if hasattr(layer, 'kernel_initializer'): 
            layer._initial_weights 

 # =========================================================================================================================== 

def test_print(my_get_weights): 
    print(my_get_weights) 

# batch_print_callback = LambdaCallback(on_batch_begin=lambda batch,logs: print(batch)) 
# print_weights = LambdaCallback(on_epoch_end=lambda epoch, logs: test_print(model_2.get_weights())) 