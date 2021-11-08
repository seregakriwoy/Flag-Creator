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
        self.color_button.clicked.connect(self.color_button_push)
        self.ok_button.clicked.connect(self.run_1)
        self.col = ''

    def is_number(self, b):
        try:
            float(b)
            return True
        except ValueError:
            return False

    def error_1(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle('Ошибка')
        msg.exec_()

    def color_button_push(self):
        self.col = QColorDialog.getColor()

    def run_1(self):
        if MainWindow().is_number(self.lineEdit.text()):
            if self.lineEdit.text() and self.col != '':
                if (float(self.lineEdit.text()) >= 1.0) and (float(self.lineEdit.text()) <= 2.0):
                    self.znach = float(self.lineEdit.text())
                    self.wid = FlagWidget(self.znach, self.col)
                    self.wid.show()
                    self.hide()
                else:
                    MainWindow().error_1('Некоректное значение')
            else:
                MainWindow().error_1('Не оставляйте пустые поля')
        else:
            MainWindow().error_1('Необходимо записать число')


class Flag_Form():

    def setupUi_flg(self, Form, prop, col):
        self.prop = prop
        self.col = col
        Form.setObjectName("Form")
        Form.resize(round(350 * prop), 350)
        self.string_btn = QtWidgets.QPushButton(Form)
        self.string_btn.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.string_btn.setObjectName("pushButton")
        self.strings_btn = QtWidgets.QPushButton(Form)
        self.strings_btn.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.strings_btn.setObjectName("pushButton_2")
        self.forms_btn = QtWidgets.QPushButton(Form)
        self.forms_btn.setGeometry(QtCore.QRect(10, 90, 111, 41))
        self.forms_btn.setObjectName("pushButton_3")
        self.arms_btn = QtWidgets.QPushButton(Form)
        self.arms_btn.setGeometry(QtCore.QRect(10, 140, 111, 31))
        self.arms_btn.setObjectName("pushButton_4")
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setGeometry(QtCore.QRect(10, 260, 141, 51))
        self.save_btn.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                    "")
        self.save_btn.setObjectName("pushButton_5")

        self.retranslateUi_flg(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi_flg(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.string_btn.setText(_translate("Form", "Нарисовать полосу"))
        self.strings_btn.setText(_translate("Form", "Нарисовать череду\n"
                                                    "полос"))
        self.forms_btn.setText(_translate("Form", "Нарисовать особую\n"
                                                  "форму"))
        self.arms_btn.setText(_translate("Form", "Вставить герб"))
        self.save_btn.setText(_translate("Form", "Сохранить изображение"))

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        qp.setPen(self.col)
        qp.setBrush(self.col)
        qp.drawRect(130, 10, round(200 * self.prop), 200)


class FlagWidget(Flag_Form, QWidget):
    def __init__(self, prop, col):
        super().__init__()
        self.setupUi_flg(self, prop, col)
        self.string_btn.clicked.connect(self.string_btn_push)

    def string_btn_push(self):
        self.str = StringWidget()
        self.str.show()


class String_Form(object):
    def setupUi_str(self, Form):
        Form.setObjectName("Form")
        Form.resize(318, 151)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 0, 81, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 20, 71, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(230, 0, 91, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(230, 20, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.ok_btn = QtWidgets.QPushButton(Form)
        self.ok_btn.setGeometry(QtCore.QRect(200, 100, 111, 41))
        self.ok_btn.setObjectName("ok_btn")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_4.setObjectName("label_4")
        self.col_btn = QtWidgets.QPushButton(Form)
        self.col_btn.setGeometry(QtCore.QRect(14, 70, 81, 23))
        self.col_btn.setObjectName("col_btn")
        self.drow_btn = QtWidgets.QPushButton(Form)
        self.drow_btn.setGeometry(QtCore.QRect(100, 100, 91, 31))
        self.drow_btn.setObjectName("drow_btn")

        self.retranslateUi_str(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi_str(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(1, _translate("Form", "Горизонтальная"))
        self.comboBox.setItemText(2, _translate("Form", "Вертикальная"))
        self.label.setText(_translate("Form", "Ориентация полосы"))
        self.label_2.setText(_translate("Form", "Размер полосы"))
        self.comboBox_2.setItemText(1, _translate("Form", "2"))
        self.comboBox_2.setItemText(2, _translate("Form", "3"))
        self.comboBox_2.setItemText(3, _translate("Form", "4"))
        self.comboBox_2.setItemText(4, _translate("Form", "5"))
        self.comboBox_2.setItemText(5, _translate("Form", "6"))
        self.label_3.setText(_translate("Form", "Позиция полосы"))
        self.comboBox_3.setItemText(1, _translate("Form", "1"))
        self.comboBox_3.setItemText(2, _translate("Form", "2"))
        self.comboBox_3.setItemText(3, _translate("Form", "3"))
        self.comboBox_3.setItemText(4, _translate("Form", "4"))
        self.comboBox_3.setItemText(5, _translate("Form", "5"))
        self.comboBox_3.setItemText(6, _translate("Form", "6"))
        self.ok_btn.setText(_translate("Form", "Принять"))
        self.label_4.setText(_translate("Form", "Цвет полосы"))
        self.col_btn.setText(_translate("Form", "Выбрать"))
        self.drow_btn.setText(_translate("Form", "Нарисовать"))


class StringWidget(String_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi_str(self)
        # if (self.comboBox_2.currentText() != '') and (self.comboBox_3.currentText() != ''):
        #     if int(self.comboBox_2.currentText()) < int(self.comboBox_3.currentText()):
        # MainWindow().error_1('Номер позиции не должен превышать размера полосы')
        self.col_btn.clicked.connect(self.col_btn_push)
        self.drow_btn.clicked.connect(self.drow_btn_push)
        self.col_str = ''

    def col_btn_push(self):
        self.col_str = QColorDialog.getColor()

    def drow_btn_push(self):
        if (self.comboBox.currentText() != '') and (self.comboBox_2.currentText() != '') and (
                self.comboBox_3.currentText() != '') and self.col_str != '':
            if int(self.comboBox_2.currentText()) >= int(self.comboBox_3.currentText()):
                if self.comboBox.currentText() == 'Горизонтальная':
                    pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
