import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.pressEvent)

    def paintEvent(self, e):
        if self.flag:
            self.flag = False
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawCircle(self.qp)
            self.qp.end()

    def pressEvent(self):
        self.flag = True
        self.update()

    def drawCircle(self, qp):
        qp.setBrush(Qt.yellow)
        for i in range(random.randint(1, 100)):
            size = random.randint(5, 100)
            qp.drawEllipse(
                random.randint(10, 790),
                random.randint(10, 590),
                size, size
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Example()
    gui.show()
    sys.exit(app.exec_())
