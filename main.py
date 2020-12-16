import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = 0
        self.pushButton.clicked.connect(self.Flag)

    def paintEvent(self, e):
        if self.flag == 1:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()
            self.show()

    def drawCircle(self, qp):
        qp.setBrush(Qt.yellow)
        for i in range(random.randint(1, 100)):
            size = random.randint(5, 100)
            qp.drawEllipse(
                random.randint(10, 790),
                random.randint(10, 590),
                size, size
            )

    def Flag(self):
        self.flag = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Example()
    gui.show()
    sys.exit(app.exec_())
