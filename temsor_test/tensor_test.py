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
#gre: 영어 성적
#gpa: 학점
#rank: 대학 순위(낮을 수록 좋음)
#admit: 합격 여부(0: 불합격, 1: 합격)

#신경망 구축
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='elu'),
    tf.keras.layers.Dense(64, activation='leaky_relu'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])
#학습
model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
model.fit(np.array(xdata), np.array(ydata), epochs=250)

#추론
inference = model.predict(np.array([[750, 3.70, 3], [800, 4.0, 1], [100, 2.0, 1], [600, 2.0, 4], [800, 3.0, 2]]))
print(inference)
