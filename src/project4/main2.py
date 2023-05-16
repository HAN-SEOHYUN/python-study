import qrcode

file_path = r'./test/qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f : #open(파일경로, 파일모드, 인코딩방식)
    # 파일모드 rt : 파일을 읽기 모드(r)로 열되, 텍스트 파일(t)로 열리도록 지정
    read_lines = f.readlines() #파일 f 에서 라인을 읽어 list 로 반환

    for line in read_lines:
        line = line.strip() #양쪽 공백제거
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = './test/' + qr_data + '.png'
        qr_img.save(save_path) #인자로 받은 경로에 이미지 파일 저장