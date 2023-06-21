## Ex 10-5. 간단한 그림판 프로그램.

import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

ui_path = r'src/project30/그림판.ui'
form_class = uic.loadUiType(ui_path)[0]

class MyApp(QMainWindow,form_class):

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 5
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.initUI()
        
    # self.image : 그림이 그려지는 이미지
    # 프로그램이 실행될 때 흰색 (Qt.white)으로 초기화됨
    # self.drawing : 그림이 그려지는 중이라면 True, 그렇지 않다면 False가 되는 변수
    # self.brush_size, self.brush_color : 펜의 크기 & 색을 나타냄
    # self.last_point : 마우스를 누른 상태로 이동하는 과정의 마지막 지점을 나타냄 

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)
        
        # 메뉴바를 하나 만들고 ‘File’ 메뉴를 만든다.
        # QAction()를 이용해서 ‘Save’, ‘Clear’ 액션을 추가
        # setShortcut()을 이용해서 각각의 단축키를 설정
        # 각각의 액션은 self.save와 self.clear 메서드에 연결된다.

        self.setWindowTitle('Simple Painter')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())
        
        # paintEvent() 메서드는 위젯이 화면에 처음 나타날 때, 또는 숨겨졌다가 다시 표시될 때 자동으로 호출됨
        # PyQt5의 그림 그리기는 QPainter()를 통해 이뤄지는데, QPainter()의 drawImage() 메서드는 이미지를 표시하는 기능을 한다.
        # (이미지를 나타낼 영역, 표시할 원본 이미지, 원본 이미지의 영역을 지정)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())
            self.last_point = e.pos()
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False
            
        # 마우스 왼쪽 버튼을 눌렀을 때, e.pos()를 이용해서 누른 지점을 self.last_point 변수에 저장한다.
        # 마우스 왼쪽 버튼을 누른채로 움질일 때, self.last_point와 e.pos() 지점을 잇는 선을 그린다.

    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.save(fpath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        
        # 파일 메뉴에서 ‘Save’ 버튼 또는 ‘Ctrl+S’ 단축키를 누르면 이미지가 저장됨
        # QFileDialog.getSaveFileName()은 파일을 저장할 때 사용자로부터 파일명을 입력받아서 반환한다.
        # 마지막 파라미터에는 저장할 이미지의 확장자로 지정할 옵션을 입력한다.
        # 파일 메뉴에서 ‘Clear’ 버튼 또는 ‘Ctrl+C’ 단축키를 누르면 그림판이 지워진다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())