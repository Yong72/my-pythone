
#This code are standalone code

# 1. Numpy 가져오기 
import numpy as np 
print(np.__version__) 

import keras 
print(keras.__version__) 

# 3. Keras 패키지 가져오기 
from keras.models import Sequential 
from keras.layers import Dense #, Activation 
# from keras.optimizers import SGD 

# 2. 입력/출력 데이터 만들기 
X2 = np.array([[0,0],[1,0],[0,1],[1,1]]) 
Y2 = np.array([[0],[1],[1],[0]]) 

# 4. Perceptron 모델 생성 
model_2 = Sequential() 
model_2.add(Dense(units=16,input_dim=2, activation='relu')) 
model_2.add(Dense(units=1, activation='sigmoid')) 
# 5. Compile - Optimizer, Loss function 설정 

# sgd = SGD(lr=0.1) 
model_2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 

# 6. 학습시키기 
model_2.fit(X2,Y2, batch_size=1, epochs=1500, shuffle=True, verbose=0) 

# 7. 모델 테스트하기 
test = np.array([[0,0],[1,0],[0,1],[1,1]]) 
pred = model_2.predict(test) 

print(pred) 
print(model_2.get_weights()) 