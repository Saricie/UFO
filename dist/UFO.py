import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class UFO(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setFixedSize(500, 500)
        self.setWindowTitle('НЛО')
        self.pixmap = QPixmap('UFO.jpg').scaled(50, 50)
        self.ufo = QLabel(self)
        self.ufo.resize(50, 50)
        self.ufo.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W or event.key() == Qt.Key_Up:
            if self.ufo.y() - 10 >= 0:
                self.ufo.move(self.ufo.x(), self.ufo.y() - 10)
            else:
                self.ufo.move(self.ufo.x(), 450)
        if event.key() == Qt.Key_S or event.key() == Qt.Key_Down:
            if self.ufo.y() + 10 <= 500:
                self.ufo.move(self.ufo.x(), self.ufo.y() + 10)
            else:
                self.ufo.move(self.ufo.x(), 0)
        if event.key() == Qt.Key_D or event.key() == Qt.Key_Right:
            if self.ufo.x() + 10 <= 500:
                self.ufo.move(self.ufo.x() + 10, self.ufo.y())
            else:
                self.ufo.move(0, self.ufo.y())
        if event.key() == Qt.Key_A or event.key() == Qt.Key_Left:
            if self.ufo.x() - 10 >= 0:
                self.ufo.move(self.ufo.x() - 10, self.ufo.y())
            else:
                self.ufo.move(450, self.ufo.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ufo = UFO()
    ufo.show()
    sys.exit(app.exec())
