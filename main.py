import sys
import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from threading import Timer, Thread, Event

from perpetualTimer import perpetualTimer


class MyApp(QWidget):
    global count
    count = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global t
        t = perpetualTimer(self.changeLabel)

        btn1 = QPushButton(self)
        btn1.setText("Start")
        btn1.clicked.connect(self.start)

        # btn2 = QPushButton(self)
        # btn2.setText("pause")
        # btn2.clicked.connect(self.pause)
        # btn2.setDisabled(True)

        btn3 = QPushButton(self)
        btn3.setText("stop")
        btn3.clicked.connect(self.stop)

        # btn4 = QPushButton(self)
        # btn4.setText("Hold")
        # btn4.clicked.connect(self.Hold)
        # btn4.setDisabled(True)

        btn5 = QPushButton(self)
        btn5.setText("exit")
        btn5.clicked.connect(QCoreApplication.instance().quit)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        # hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        # hbox.addWidget(btn4)
        hbox.addWidget(btn5)
        hbox.addStretch(1)

        self.label1 = QLabel("00:00:00", self)
        self.label1.setAlignment(Qt.AlignCenter)
        font1 = self.label1.font()
        font1.setPointSize(50)
        font1.setFamily("D2 Coding")
        font1.setBold(True)
        self.label1.setFont(font1)
        self.label1.setStyleSheet("color: white;" "background-color: green")

        vbox = QVBoxLayout()

        vbox.addWidget(self.label1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("Time Counter")
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.adjustSize()
        # self.resize(450, 200)
        self.center()
        self.setStyleSheet("color: #7FFFD4;" "background-color: green")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Hold(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowFlag(Qt.WindowStaysOnBottomHint)
        self.show()

    def start(self):
        # self.changeLabel()
        t.start()

    def pause(self):
        t.pause()

    def stop(self):
        t.cancel()

    def changeLabel(self):
        temp = self.label1.text()
        temp2 = datetime.datetime.strptime(temp, "%H:%M:%S")
        temp3 = temp2 + datetime.timedelta(seconds=1)
        self.label1.setText(temp3.strftime("%H:%M:%S"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
