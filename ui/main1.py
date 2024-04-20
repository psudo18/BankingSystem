# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main1.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

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
        self.label.setGeometry(QRect(150, 10, 211, 61))
        self.label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.bgwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 90, 161, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_2 = QPushButton(self.bgwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 90, 161, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_3 = QPushButton(self.bgwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 160, 161, 41))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_4 = QPushButton(self.bgwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 160, 161, 41))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_5 = QPushButton(self.bgwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 230, 161, 41))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_6 = QPushButton(self.bgwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(320, 230, 161, 41))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_7 = QPushButton(self.bgwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(30, 300, 161, 41))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_8 = QPushButton(self.bgwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(320, 300, 161, 41))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"border-radius : 20px;\n"
"background-color:rgb(40, 170, 138);\n"
"color:rgb(255, 255, 255);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select an option", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Deposite", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Withdraw", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Check Balance", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Fixed Deposite", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Loan", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Pay EMI", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Transaction", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Close Account", None))
    # retranslateUi

