import qrcode

file_path = r'./test/qr코드모음.txt'
# r : 파이썬 문자열 리터럴 = raw string
# \를 escape 하지 않고 그대로 문자열에 포함시킴
with open(file_path, 'rt', encoding='UTF8') as f : 
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)
# with - 피이썬의 컨텍스트 관리자를 사용할 때 사용되는 문법
# 파이썬의 컨텍스트 관리자 : 파일 입출력, 네트워크 연결, 데이터베이스 연결 등과 같이 자원을 사용하는 일련의 작업을 수행할 때, 
# 자원을 올바르게 할당하고 해제하는 등의 작업을 자동으로 처리해주는 기능을 제공함

# with [컨텍스트 관리자 객체] as [변수명]:
#     [코드 블록]

# with 문법을 사용하면, 
#  1. 자원 할당 및 해제를 별도로 처리하지 않아도 되므로, 코드를 간결하게 작성할 수 있고
#  2. 예외 처리도 보다 쉽게 구현할 수 있음

# with를 사용해 파일을 열고 파일 객체 f 를 생성함
# with 블록을 벗어나면 f 객체가 자동으로 닫히므로, 별도로 f.close()를 호출할 필요가 없다.