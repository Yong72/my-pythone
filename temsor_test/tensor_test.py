import pandas as pd
import numpy as np
import tensorflow as tf
#데이터 입력 및 전처리
data = pd.read_csv('gpascore.csv')
data = data.dropna()
#데이터 분할 및 정규화
ydata = data['admit'].values
xdata = []
for i, rows in data.iterrows():
    xdata.append([rows['gre'], rows['gpa'], rows['rank']])
#신경망 구축
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])
#학습
model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
model.fit(np.array(xdata), np.array(ydata), epochs=500)

#추론
예측값 = model.predict(np.array([[750, 3.70, 3], [800, 4.0, 1]]))
print(예측값)