# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createacc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(520, 406)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 521, 411))
        self.bgwidget.setStyleSheet(u"QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.124955, y1:0.199, x2:0.909091, y2:0.903, stop:0 rgba(170, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.pushButton_2 = QPushButton(self.bgwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 350, 161, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setCheckable(True)
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(58, 20, 401, 20))
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.bgwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 100, 131, 22))
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.label_2 = QLabel(self.bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 80, 61, 16))
        self.lineEdit_2 = QLineEdit(self.bgwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(380, 150, 131, 22))
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_3 = QLineEdit(self.bgwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(380, 210, 131, 22))
        self.lineEdit_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.label_3 = QLabel(self.bgwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 130, 61, 16))
        self.label_4 = QLabel(self.bgwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(380, 190, 111, 16))
        self.lineEdit_4 = QLineEdit(self.bgwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 100, 131, 22))
        self.lineEdit_4.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.label_5 = QLabel(self.bgwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 80, 51, 16))
        self.lineEdit_5 = QLineEdit(self.bgwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 150, 131, 22))
        self.lineEdit_5.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.label_6 = QLabel(self.bgwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 130, 71, 16))
        self.lineEdit_6 = QLineEdit(self.bgwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 210, 131, 22))
        self.lineEdit_6.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.label_7 = QLabel(self.bgwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 190, 49, 16))
        self.lineEdit_7 = QLineEdit(self.bgwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(200, 100, 131, 22))
        self.lineEdit_7.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.label_8 = QLabel(self.bgwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 80, 91, 16))
        self.lineEdit_8 = QLineEdit(self.bgwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(200, 150, 131, 22))
        self.lineEdit_8.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.label_9 = QLabel(self.bgwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 130, 71, 16))
        self.lineEdit_9 = QLineEdit(self.bgwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(200, 210, 131, 22))
        self.lineEdit_9.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"")
        self.label_10 = QLabel(self.bgwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 190, 81, 16))
        self.checkBox = QCheckBox(self.bgwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(50, 300, 441, 20))
        self.checkBox.setTabletTracking(False)
        self.checkBox.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Create an account", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome ! Please fill the details to create a new account", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"email", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Confirm password", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"YYYY-MM-DD", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Date of birth", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Dialog", u"M/F", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Gender", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Dialog", u"phone number", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Phone number", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Dialog", u"Pan card number", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"PAN ", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Dialog", u" Aadhar No.", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Aadhar No.", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u" I completly agree to the all terms and the conditions of the bank.", None))
    # retranslateUi

