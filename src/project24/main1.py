import numpy as np
import cv2
# numpy(Numerical Python) : 수치계산을 위한 라이브러리
# 다차원 배열을 사용하여 벡터 및 행렬 연산, 선형 대수, 푸리에 변환 등과 같은 과학적, 수치적 계산을 수행한다.

# OpenCV(Open Source Computer Vision)
# 이미지 & 비디오 로드, 저장, 조작, 분석 등에 사용됨

ff = np.fromfile(r'src/project24/사진을 그림으로 변환하기 (OpenCV)/여행사진.jpg', np.uint8)
# 이미지 파일을 바이트 배열로 읽어옴
# np.fromfile() 함수는 지정된 경로의 파일에서 데이터를 읽어와서 np.uint8 데이터유형의 NumPy 배열로 변환함
# np.uint8 : 8비트의 부호 없는 정수 데이터 유형을 의미함 (0 ~ 255)

img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# 바이트 배열을 이미지로 디코딩
# IMREAD_UNCHANGED : 이미지를 이미지 채널 수(이미지에서 사용되는 색상 채널의 수)와 함께 디코딩
# 디코딩된 이미지를 img 변수에 저장

img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)
# 이미지 크기 조정
# dsize 함수나, , fx와 fy 매개변수를 사용해 이미지의 가로 및 세로 크기를 조정할 수 있다.
# INTER_LINEAR : 선형보간법
# 보간법 : 이미지 크기를 변경할 때 새로운 픽셀 값을 계산하기 위해 주변 픽셀의 값을 활용하는 방법

cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)
# 카툰 이미지 생성
# cv2.stylization() 함수를 사용해 입력 이미지를 카툰 스타일로 변경
# sigma_s : 공간 필터링에 사용되는 시그마 값
# sigma_r : 색상 필터링에 사용되는 시그마 값

cv2.imshow('cartoon view', cartoon_img)
# 변경된이미지 출력
# imshow(출력되는 창의 이름, 이미지가 저장된 변수)

cv2.waitKey(0)
# 사용자가 키를 누를때까지 대기한다. 0을 전달하면 키 입력이 있을 때까지 무한대기
# 이미지 창이 닫히지 않도록 하는 역할

cv2.destroyAllWindows()
# 모든 이미지 창 닫기