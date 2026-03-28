# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(408, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setEnabled(True)
        self.input_text.setGeometry(QRect(60, 20, 331, 31))
        font = QFont()
        font.setFamilies([u"Courier New"])
        self.input_text.setFont(font)
        self.input_text.setAutoFillBackground(False)
        self.input_text.setStyleSheet(u"background-color: #1c1c1c;")
        self.input_text.setFrame(False)
        self.button_t = QPushButton(self.centralwidget)
        self.button_t.setObjectName(u"button_t")
        self.button_t.setGeometry(QRect(160, 60, 141, 41))
        self.button_f = QPushButton(self.centralwidget)
        self.button_f.setObjectName(u"button_f")
        self.button_f.setGeometry(QRect(10, 60, 141, 41))
        self.button_and = QPushButton(self.centralwidget)
        self.button_and.setObjectName(u"button_and")
        self.button_and.setGeometry(QRect(159, 100, 141, 41))
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setGeometry(QRect(10, 20, 71, 16))
        self.output_eval = QLabel(self.centralwidget)
        self.output_eval.setObjectName(u"output_eval")
        self.output_eval.setGeometry(QRect(10, 160, 57, 14))
        self.button_equal = QPushButton(self.centralwidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setGeometry(QRect(310, 60, 80, 81))
        self.button_or = QPushButton(self.centralwidget)
        self.button_or.setObjectName(u"button_or")
        self.button_or.setGeometry(QRect(10, 100, 141, 41))
        self.output_trans = QLabel(self.centralwidget)
        self.output_trans.setObjectName(u"output_trans")
        self.output_trans.setGeometry(QRect(100, 160, 57, 14))
        self.output_tree = QLabel(self.centralwidget)
        self.output_tree.setObjectName(u"output_tree")
        self.output_tree.setGeometry(QRect(10, 210, 57, 14))
        self.label_eval = QLabel(self.centralwidget)
        self.label_eval.setObjectName(u"label_eval")
        self.label_eval.setEnabled(True)
        self.label_eval.setGeometry(QRect(50, 160, 31, 31))
        self.label_eval.setFont(font)
        self.label_eval.setAutoFillBackground(False)
        self.label_eval.setStyleSheet(u"background-color: #1c1c1c;")
        self.label_eval.setFrameShape(QFrame.Shape.NoFrame)
        self.label_trans = QLabel(self.centralwidget)
        self.label_trans.setObjectName(u"label_trans")
        self.label_trans.setEnabled(True)
        self.label_trans.setGeometry(QRect(150, 160, 241, 31))
        self.label_trans.setFont(font)
        self.label_trans.setAutoFillBackground(False)
        self.label_trans.setStyleSheet(u"background-color: #1c1c1c;")
        self.label_trans.setFrameShape(QFrame.Shape.NoFrame)
        self.label_tree = QLabel(self.centralwidget)
        self.label_tree.setObjectName(u"label_tree")
        self.label_tree.setEnabled(True)
        self.label_tree.setGeometry(QRect(10, 240, 381, 281))
        self.label_tree.setFont(font)
        self.label_tree.setAutoFillBackground(False)
        self.label_tree.setStyleSheet(u"background-color: #1c1c1c;")
        self.label_tree.setFrameShape(QFrame.Shape.NoFrame)
        self.label_tree.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 408, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_t.setText(QCoreApplication.translate("MainWindow", u"t", None))
        self.button_f.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.button_and.setText(QCoreApplication.translate("MainWindow", u"\u2227", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.output_eval.setText(QCoreApplication.translate("MainWindow", u"Eval:", None))
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.button_or.setText(QCoreApplication.translate("MainWindow", u"\u2228", None))
        self.output_trans.setText(QCoreApplication.translate("MainWindow", u"Trans:", None))
        self.output_tree.setText(QCoreApplication.translate("MainWindow", u"Tree:", None))
        self.label_eval.setText("")
        self.label_trans.setText("")
        self.label_tree.setText("")
    # retranslateUi

