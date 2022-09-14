from PySide6.QtCore import Qt
# print(dir(Qt))
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPalette

# print(Qt.Alignment)
# print(type(QApplication))
app = QApplication()    # 눈에 보이지 않는 영역을 처리해주는 instance
# widget = QWidget()
# widget.show()
label = QLabel('Moon')
label.show()
label.setFixedSize(100, 100)
# label.alignment()
palette = QPalette()
label.setAlignment(Qt.AlignCenter)
# label.setBackgroundRole(palette.Light)
app.exec()
