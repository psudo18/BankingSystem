# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transactionm.ui'
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
        Dialog.resize(367, 303)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 521, 411))
        self.bgwidget.setStyleSheet(u"QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.124955, y1:0.199, x2:0.909091, y2:0.903, stop:0 rgba(170, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(48, 29, 261, 31))
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_2 = QPushButton(self.bgwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 220, 161, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2 = QLabel(self.bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 100, 201, 31))
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(self.bgwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 161, 161, 31))
        self.lineEdit.setStyleSheet(u"background-color:transparent;")
        self.lineEdit.setClearButtonEnabled(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Proceed", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Enter the Account No.", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Account No.", None))
    # retranslateUi

