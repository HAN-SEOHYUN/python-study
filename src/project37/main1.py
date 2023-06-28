# TensorFlow
# 구글에서 개발한 머신러닝 프레임워크

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

model_path = r'src/project37/converted_keras/keras_model.h5'
labels_path = r'src/project37/converted_keras/labels.txt'
image_path = r'src/project37/검증용사진/오렌지.jpeg'

model = tensorflow.keras.models.load_model(model_path)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# 입력 데이터의 형태를 정의 : 1개의 이미지를 처리하며, 크기 : 224x224 / 채널 : RGB 색상

image = Image.open(image_path)
# Image.open() : 이미지 파일 열기

size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
# ImageOps.fit() : 이미지를 지정된 크기로 조정 
# Image.ANTIALIAS : 고해상도로 리샘플링

image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array
# np.asarray() : 이미지를 배열로 변환하고 배열을 정규화한다. 이후 정규화된 이미지 배열을 data에 할당함

prediction = model.predict(data)
print(prediction)
# model.predict() : 입력 데이터에 대한 예측값을 얻는다. 

with open(labels_path, 'rt', encoding='utf8') as f:
  readlines = f.readlines()

if prediction[0, 0] > prediction[0, 1]:
  print(readlines[0])
else: 
  print(readlines[1])
  
# labels_path블 파일을 열고, 각 클래스에 해당하는 labels_path을 readlines 리스트에 저장