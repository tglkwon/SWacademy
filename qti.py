from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QMainWindow, QMenuBar, QToolBar, QMenu,
                               QPushButton, QVBoxLayout, Qc)
from PySide6.QtGui import QPalette, QIcon, QIconEngine
from PySide6.QtCore import Qt, QSize, Slot
import pprint
# print(dir(Qt))
app = QApplication()    # 눈에 보이지 않는 영역을 처리해주는 instance
window = QMainWindow()  # 메뉴, 툴바들을 추가시키고 관리한다

# 나만의 프로그램 창 만들기
class KwonMainWindow(QMainWindow):
    def __init__(self, title):
        super(KwonMainWindow, self).__init__()
        self.setWindowTitle(title)
        icon = QIcon('jsonWeb.jfif')
        label = QLabel('Moon')
        button = QPushButton(icon, 'json')
        widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


window = KwonMainWindow('Kwon')


## label 연습
# label.setFixedSize(100, 100)
# size = QSize(300,400)
# label.setMinimumSize(size)
# # label.alignment()
# palette = QPalette()
# label.setAlignment(Qt.AlignCenter)
# label.setBackgroundRole(palette.Light)

@Slot()
def xx():
    print('xxxxx')


## pushbutton 연습
# 설명이 더 필요한 경우 찾는법
# print(button.clicked.connect.__doc__)
# button.clicked.connect(xx())


# print(Qt.Alignment)
# print(type(QApplication))
# window.setWindowTitle('MOon')
# window.setCentralWidget(label)
# window.setWindowIcon(icon)
# qmenu = QMenu('File')
# qmenu.show()
# menubar = QMenuBar()
# menubar.addMenu()

# button.show()
# widget.show()
window.show()
# label.show()

app.exec()
