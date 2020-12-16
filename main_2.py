import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.flag = False

        self.pushButton = QPushButton('Нажми меня', self)
        self.pushButton.resize(100, 60)
        self.pushButton.move(350, 500)
        self.pushButton.clicked.connect(self.pressEvent)

    def pressEvent(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawCicrle(self.qp)
            self.qp.end()

    def drawCicrle(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for i in range(random.randint(1, 100)):
            size = random.randint(5, 100)
            qp.drawEllipse(
                random.randint(10, 790),
                random.randint(10, 590),
                size, size
            )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = Window()
    main_form.show()
    sys.exit(app.exec())
