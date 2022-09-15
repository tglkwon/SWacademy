from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QMainWindow, QMenuBar, QToolBar, QMenu,
                               QPushButton)
from PySide6.QtGui import QPalette, QIcon
from PySide6.QtCore import Qt
# print(dir(Qt))

# print(Qt.Alignment)
# print(type(QApplication))
app = QApplication()    # 눈에 보이지 않는 영역을 처리해주는 instance
widget = QWidget()
# widget.show()
window = QMainWindow()  # 메뉴, 툴바들을 추가시키고 관리한다
qmenu = QMenu('File')
qmenu.show()
menubar = QMenuBar()
# menubar.addMenu()
window.show()

## label 연습
label = QLabel('Moon')
label.show()
label.setFixedSize(100, 100)
# label.alignment()
palette = QPalette()
label.setAlignment(Qt.AlignCenter)
# label.setBackgroundRole(palette.Light)

## pushbutton 연습
button = QPushButton('button')
button.clicked.connect()
button.show()

app.exec()
