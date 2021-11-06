import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QMessageBox, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets, sip


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(276, 105)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 21, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 61, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 0, 121, 21))
        self.label_3.setObjectName("label_3")
        self.color_button = QtWidgets.QPushButton(self.centralwidget)
        self.color_button.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.color_button.setObjectName("color_button")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(100, 40, 75, 23))
        self.ok_button.setObjectName("ok_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Пропорции флага:"))
        self.label_2.setText(_translate("MainWindow", "1 к "))
        self.label_3.setText(_translate("MainWindow", "Основной цвет флага:"))
        self.color_button.setText(_translate("MainWindow", "Выбрать"))
        self.ok_button.setText(_translate("MainWindow", "Принять"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.color_button.clicked.connect(self.run)
        self.ok_button.clicked.connect(self.run_1)
        self.col = ''
        self.do_paint = False

    def is_number(self, b):
        try:
            float(b)
            return True
        except ValueError:
            return False

    def run(self):
        self.col = QColorDialog.getColor()

    def run_1(self):
        if MainWindow().is_number(self.lineEdit.text()):
            if self.lineEdit.text() and self.col != '':
                if (float(self.lineEdit.text()) >= 1.0) and (float(self.lineEdit.text()) <= 2.0):
                    self.znach = float(self.lineEdit.text())
                    print(self.znach)
                    self.form = Ui_Form(self.znach, self.col, self.do_paint)
                    self.wid = MyWidget(self.znach, self.col, self.do_paint)
                    self.wid.show()
                    self.do_paint = True
                    self.hide()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText('некоректное значение')
                    msg.setWindowTitle('Ошибка')
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('не оставляйте пустые поля')
                msg.setWindowTitle('Ошибка')
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('необходимо записать число')
            msg.setWindowTitle('Ошибка')
            msg.exec_()


class Ui_Form():
    def __init__(self, a, b, c):
        self.c = c
        self.a = a
        self.b = b

    def setupUi_1(self, Form):
        Form.setObjectName("Form")
        Form.resize(400 * self.a, 350)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 140, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 260, 141, 51))
        self.pushButton_5.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "")
        self.pushButton_5.setObjectName("pushButton_5")
        #sip.delete(self.label)
        #sip.delete(self.label_2)
        #sip.delete(self.label_3)
        #sip.delete(self.ok_button)
        #sip.delete(self.color_button)
        #sip.delete(self.lineEdit)


        self.retranslateUi_1(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi_1(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Нарисовать полосу"))
        self.pushButton_2.setText(_translate("Form", "Нарисовать череду\n"
                                                     "полос"))
        self.pushButton_3.setText(_translate("Form", "Нарисовать особую\n"
                                                     "форму"))
        self.pushButton_4.setText(_translate("Form", "Вставить герб"))
        self.pushButton_5.setText(_translate("Form", "Сохранить изображение"))

    def paintEvent(self, event):
        if self.c:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setPen(QColor(255, 0, 0))
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(130, 10, 230, 110)


# noinspection PyTypeChecker
class MyWidget(QWidget, Ui_Form):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.setupUi(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
