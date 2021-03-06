import sys

from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QMessageBox, QWidget, \
     QLabel
from PyQt5 import QtCore, QtGui, QtWidgets


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


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
        self.label.setText(_translate("MainWindow", "?????????????????? ??????????:"))
        self.label_2.setText(_translate("MainWindow", "1 ?? "))
        self.label_3.setText(_translate("MainWindow", "???????????????? ???????? ??????????:"))
        self.color_button.setText(_translate("MainWindow", "??????????????"))
        self.ok_button.setText(_translate("MainWindow", "??????????????"))


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
        msg.setWindowTitle('????????????')
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
                    MainWindow().error_1('?????????????????????? ????????????????!')
            else:
                MainWindow().error_1('???? ???????????????????? ???????????? ????????!')
        else:
            MainWindow().error_1('???????????????????? ???????????????? ??????????!')


class Flag_Form(QWidget):

    def setupUi_flg(self, Flag, prop, col):
        self.prop = prop
        self.col = col
        self.dlin = round(200 * self.prop)
        Flag.setObjectName("Form")
        Flag.resize(round(350 * prop), 350)
        # self.save_btn = QtWidgets.QPushButton(Flag)
        # self.save_btn.setGeometry(QtCore.QRect(190, 250, 141, 51))
        # self.save_btn.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
        #                             "")
        # self.save_btn.setObjectName("save_btn")
        self.orientation_comboBox = QtWidgets.QComboBox(Flag)
        self.orientation_comboBox.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.orientation_comboBox.setObjectName("orientation_comboBox")
        self.orientation_comboBox.addItem("")
        self.orientation_comboBox.setItemText(0, "")
        self.orientation_comboBox.addItem("")
        self.orientation_comboBox.addItem("")
        self.label = QtWidgets.QLabel(Flag)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Flag)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.size_comboBox = QtWidgets.QComboBox(Flag)
        self.size_comboBox.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.size_comboBox.setObjectName("size_comboBox")
        self.size_comboBox.addItem("")
        self.size_comboBox.setItemText(0, "")
        self.size_comboBox.addItem("")
        self.size_comboBox.addItem("")
        self.size_comboBox.addItem("")
        self.size_comboBox.addItem("")
        self.size_comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Flag)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_3.setObjectName("label_3")
        self.poz_comboBox = QtWidgets.QComboBox(Flag)
        self.poz_comboBox.setGeometry(QtCore.QRect(10, 130, 69, 22))
        self.poz_comboBox.setObjectName("poz_comboBox")
        self.poz_comboBox.addItem("")
        self.poz_comboBox.setItemText(0, "")
        self.poz_comboBox.addItem("")
        self.poz_comboBox.addItem("")
        self.poz_comboBox.addItem("")
        self.poz_comboBox.addItem("")
        self.poz_comboBox.addItem("")
        self.poz_comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(Flag)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_4.setObjectName("label_4")
        self.col_btn = QtWidgets.QPushButton(Flag)
        self.col_btn.setGeometry(QtCore.QRect(10, 180, 81, 23))
        self.col_btn.setObjectName("col_btn")
        self.drow_btn = QtWidgets.QPushButton(Flag)
        self.drow_btn.setGeometry(QtCore.QRect(10, 250, 111, 41))
        self.drow_btn.setObjectName("ok_btn")
        self.label_5 = QtWidgets.QLabel(Flag)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 271, 41))
        self.label_5.setObjectName("label_5")
        # self.label_6.setGeometry(QtCore.QRect(310, 270, 61, 61))
        # self.label_6.setText("")
        # self.label_6.setObjectName("label_6")
        self.image = QLabel(self)
        self.image.move(280, 270)
        self.image.resize(61, 61)
        self.pixmap = QPixmap('image.png')
        self.image.setPixmap(self.pixmap)

        self.retranslateUi_flg(Flag)
        QtCore.QMetaObject.connectSlotsByName(Flag)

    def retranslateUi_flg(self, Flag):
        _translate = QtCore.QCoreApplication.translate
        Flag.setWindowTitle(_translate("Flag", "Form"))
        # self.save_btn.setText(_translate("Flag", "?????????????????? ??????????????????????"))
        self.orientation_comboBox.setItemText(1, _translate("Flag", "????????????????????????????"))
        self.orientation_comboBox.setItemText(2, _translate("Flag", "????????????????????????"))
        self.label.setText(_translate("Flag", "???????????????????? ????????????"))
        self.label_2.setText(_translate("Flag", "???????????? ????????????"))
        self.size_comboBox.setItemText(1, _translate("Flag", "2"))
        self.size_comboBox.setItemText(2, _translate("Flag", "3"))
        self.size_comboBox.setItemText(3, _translate("Flag", "4"))
        self.size_comboBox.setItemText(4, _translate("Flag", "5"))
        self.size_comboBox.setItemText(5, _translate("Flag", "6"))
        self.label_3.setText(_translate("Flag", "?????????????? ????????????"))
        self.poz_comboBox.setItemText(1, _translate("Flag", "1"))
        self.poz_comboBox.setItemText(2, _translate("Flag", "2"))
        self.poz_comboBox.setItemText(3, _translate("Flag", "3"))
        self.poz_comboBox.setItemText(4, _translate("Flag", "4"))
        self.poz_comboBox.setItemText(5, _translate("Flag", "5"))
        self.poz_comboBox.setItemText(6, _translate("Flag", "6"))
        self.label_4.setText(_translate("Flag", "???????? ????????????"))
        self.col_btn.setText(_translate("Flag", "??????????????"))
        self.drow_btn.setText(_translate("Flag", "????????????????????"))
        self.label_5.setText(_translate("Flag",
                                        "<html><head/><body><p>?????? ???????????????????? ???????????? ?? ?????????? ?????????? "
                                        "?????????????????? </p><p>?????????????? ???? ???? ???????????? ????????????, "
                                        "?? ?????????? ?????? ????????????????</p></body></html>"))


class FlagWidget(Flag_Form, QWidget):
    def __init__(self, prop, col):
        super().__init__()
        self.setupUi_flg(self, prop, col)
        self.col_btn.clicked.connect(self.col_btn_push)
        self.drow_btn.clicked.connect(self.drow_btn_push)
        # self.save_btn.clicked.connect(self.save_image)
        self.col_str = ''
        self.size = 0
        self.pozition = 0
        self.orientation = ''
        self.do_gor = False
        self.do_ver = False
        self.lst = []
        self.col_lst = []

    def paintEvent(self, event):
        s = 0
        self.qp = QPainter()
        self.qp.begin(self)
        if s == 0:
            self.draw_flag(self.qp)
            s += 1
        if self.do_gor:
            self.draw_string_gor(self.size, self.pozition, self.col_str, self.dlin, self.qp)
            self.update()
        elif self.do_ver:
            self.draw_string_ver(self.size, self.pozition, self.col_str, self.dlin, self.qp)
            self.update()
        self.qp.end()

    def draw_flag(self, qp):
        qp.setPen(self.col)
        qp.setBrush(self.col)
        qp.drawRect(130, 10, round(200 * self.prop), 200)
        self.dlin = round(200 * self.prop)

    def draw_string_gor(self, si, poz, clr, dl, qp):
        qp.setPen(clr)
        qp.setBrush(clr)
        qp.drawRect(130, round(10 + 200 / si * (poz - 1)), dl, round(200 / si))
        self.lst.append([clr, 130, round(10 + 200 / si * (poz - 1)), dl, round(200 / si)])
        for i in self.lst:
            qp.setPen(i[0])
            qp.setBrush(i[0])
            qp.drawRect(i[1], i[2], i[3], i[4])
            self.col_lst.append([qp.setPen(i[0]), qp.setBrush(i[0])])
        # print(1)

    def draw_string_ver(self, si, poz, clr, dl, qp):
        qp.setPen(clr)
        qp.setBrush(clr)
        qp.drawRect(round(130 + dl / si * (poz - 1)), 10, round(dl / si), 200)
        self.lst.append([clr, round(130 + dl / si * (poz - 1)), 10, round(dl / si), 200])
        for i in self.lst:
            qp.setPen(i[0])
            qp.setBrush(i[0])
            qp.drawRect(i[1], i[2], i[3], i[4])
            self.col_lst.append([qp.setPen(i[0]), qp.setBrush(i[0])])

    def col_btn_push(self):
        self.col_str = QColorDialog.getColor()

    def drow_btn_push(self):
        if (self.orientation_comboBox.currentText() != '') and (
                self.size_comboBox.currentText() != '') and (
                self.poz_comboBox.currentText() != '') and self.col_str != '':
            if int(self.size_comboBox.currentText()) >= int(self.poz_comboBox.currentText()):
                self.size = int(self.size_comboBox.currentText())
                self.pozition = int(self.poz_comboBox.currentText())
                self.orientation = self.orientation_comboBox.currentText()
                if self.orientation == '????????????????????????????':
                    self.do_ver = False
                    self.do_gor = True
                elif self.orientation == '????????????????????????':
                    self.do_gor = False
                    self.do_ver = True
            else:
                MainWindow.error_1(self, '?????????? ?????????????? ???? ?????????? ?????????????????? ????????????!')
        else:
            MainWindow.error_1(self, '???? ???????????????????? ???????????? ????????!')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
