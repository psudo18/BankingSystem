# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fdc.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(521, 411)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 521, 411))
        self.bgwidget.setStyleSheet(u"QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.124955, y1:0.199, x2:0.909091, y2:0.903, stop:0 rgba(170, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 351, 61))
        self.label.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.bgwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 320, 161, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2 = QLabel(self.bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 110, 311, 21))
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(self.bgwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 200, 161, 31))
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2 = QLineEdit(self.bgwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 260, 161, 31))
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.label_3 = QLabel(self.bgwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 180, 61, 16))
        self.label_4 = QLabel(self.bgwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 240, 61, 16))
        self.label_5 = QLabel(self.bgwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 119, 261, 31))
        self.label_5.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Proceed", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Amount (1k to 1cr.)", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"years (1 to 10)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Years", None))
        self.label_5.setText("")
    # retranslateUi

