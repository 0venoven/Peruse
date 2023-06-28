# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'peruse.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Peruse(object):
    def setupUi(self, Peruse):
        if not Peruse.objectName():
            Peruse.setObjectName(u"Peruse")
        Peruse.resize(1000, 700)
        Peruse.setStyleSheet(u"")
        self.actionQuit = QAction(Peruse)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionSearch = QAction(Peruse)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionFilter = QAction(Peruse)
        self.actionFilter.setObjectName(u"actionFilter")
        self.actionAbout = QAction(Peruse)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_QT = QAction(Peruse)
        self.actionAbout_QT.setObjectName(u"actionAbout_QT")
        self.centralwidget = QWidget(Peruse)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ip_range_label = QLabel(self.centralwidget)
        self.ip_range_label.setObjectName(u"ip_range_label")

        self.horizontalLayout.addWidget(self.ip_range_label)

        self.ip_range_line_edit = QLineEdit(self.centralwidget)
        self.ip_range_line_edit.setObjectName(u"ip_range_line_edit")

        self.horizontalLayout.addWidget(self.ip_range_line_edit)

        self.scan_button = QPushButton(self.centralwidget)
        self.scan_button.setObjectName(u"scan_button")

        self.horizontalLayout.addWidget(self.scan_button)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.scan_progress_bar = QProgressBar(self.centralwidget)
        self.scan_progress_bar.setObjectName(u"scan_progress_bar")
        self.scan_progress_bar.setValue(24)

        self.horizontalLayout.addWidget(self.scan_progress_bar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scan_output_label = QLabel(self.centralwidget)
        self.scan_output_label.setObjectName(u"scan_output_label")
        self.scan_output_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.scan_output_label)

        self.scan_output_text_browser = QTextBrowser(self.centralwidget)
        self.scan_output_text_browser.setObjectName(u"scan_output_text_browser")

        self.horizontalLayout_2.addWidget(self.scan_output_text_browser)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        Peruse.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Peruse)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menuScan = QMenu(self.menubar)
        self.menuScan.setObjectName(u"menuScan")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Peruse.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Peruse)
        self.statusbar.setObjectName(u"statusbar")
        Peruse.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuScan.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuScan.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionSearch)
        self.menuTools.addAction(self.actionFilter)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_QT)

        self.retranslateUi(Peruse)

        QMetaObject.connectSlotsByName(Peruse)
    # setupUi

    def retranslateUi(self, Peruse):
        Peruse.setWindowTitle(QCoreApplication.translate("Peruse", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("Peruse", u"Quit", None))
        self.actionSearch.setText(QCoreApplication.translate("Peruse", u"Search", None))
        self.actionFilter.setText(QCoreApplication.translate("Peruse", u"Filter", None))
        self.actionAbout.setText(QCoreApplication.translate("Peruse", u"About Peruse", None))
        self.actionAbout_QT.setText(QCoreApplication.translate("Peruse", u"About QT", None))
        self.ip_range_label.setText(QCoreApplication.translate("Peruse", u"IP Range :", None))
        self.scan_button.setText(QCoreApplication.translate("Peruse", u"Scan", None))
        self.scan_output_label.setText(QCoreApplication.translate("Peruse", u"Scan Output :", None))
        self.menuScan.setTitle(QCoreApplication.translate("Peruse", u"Scan", None))
        self.menuTools.setTitle(QCoreApplication.translate("Peruse", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Peruse", u"Help", None))
    # retranslateUi

