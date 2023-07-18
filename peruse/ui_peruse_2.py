# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'peruse_2.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Peruse(object):
    def setupUi(self, Peruse):
        if not Peruse.objectName():
            Peruse.setObjectName(u"Peruse")
        Peruse.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Peruse.sizePolicy().hasHeightForWidth())
        Peruse.setSizePolicy(sizePolicy)
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
        self.horizontal_line_1 = QFrame(self.centralwidget)
        self.horizontal_line_1.setObjectName(u"horizontal_line_1")
        self.horizontal_line_1.setGeometry(QRect(1010, 300, 871, 20))
        self.horizontal_line_1.setFrameShape(QFrame.HLine)
        self.horizontal_line_1.setFrameShadow(QFrame.Sunken)
        self.scan_output_text_browser = QTextBrowser(self.centralwidget)
        self.scan_output_text_browser.setObjectName(u"scan_output_text_browser")
        self.scan_output_text_browser.setGeometry(QRect(100, 330, 741, 561))
        self.scan_output_label = QLabel(self.centralwidget)
        self.scan_output_label.setObjectName(u"scan_output_label")
        self.scan_output_label.setGeometry(QRect(20, 330, 81, 21))
        self.scan_output_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.vertical_line_1 = QFrame(self.centralwidget)
        self.vertical_line_1.setObjectName(u"vertical_line_1")
        self.vertical_line_1.setGeometry(QRect(960, 50, 20, 831))
        self.vertical_line_1.setFrameShape(QFrame.VLine)
        self.vertical_line_1.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(860, 330, 81, 56))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.save_button = QPushButton(self.layoutWidget)
        self.save_button.setObjectName(u"save_button")

        self.verticalLayout_2.addWidget(self.save_button)

        self.delete_button = QPushButton(self.layoutWidget)
        self.delete_button.setObjectName(u"delete_button")

        self.verticalLayout_2.addWidget(self.delete_button)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(5, 2, __qtablewidgetitem25)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(1000, 330, 891, 561))
        font = QFont()
        font.setBold(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 921, 271))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scan_title_label = QLabel(self.widget)
        self.scan_title_label.setObjectName(u"scan_title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scan_title_label.sizePolicy().hasHeightForWidth())
        self.scan_title_label.setSizePolicy(sizePolicy1)
        self.scan_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.scan_title_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.current_network_label = QLabel(self.widget)
        self.current_network_label.setObjectName(u"current_network_label")
        sizePolicy.setHeightForWidth(self.current_network_label.sizePolicy().hasHeightForWidth())
        self.current_network_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.current_network_label)

        self.current_network_lineEdit = QLineEdit(self.widget)
        self.current_network_lineEdit.setObjectName(u"current_network_lineEdit")
        self.current_network_lineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.current_network_lineEdit)

        self.scan_button = QPushButton(self.widget)
        self.scan_button.setObjectName(u"scan_button")

        self.horizontalLayout.addWidget(self.scan_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ip_range_label = QLabel(self.widget)
        self.ip_range_label.setObjectName(u"ip_range_label")

        self.horizontalLayout_2.addWidget(self.ip_range_label)

        self.ip_range_lineEdit = QLineEdit(self.widget)
        self.ip_range_lineEdit.setObjectName(u"ip_range_lineEdit")
        self.ip_range_lineEdit.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.ip_range_lineEdit)

        self.cancel_button = QPushButton(self.widget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_2.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.network_tip_label = QLabel(self.widget)
        self.network_tip_label.setObjectName(u"network_tip_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.network_tip_label.sizePolicy().hasHeightForWidth())
        self.network_tip_label.setSizePolicy(sizePolicy2)
        self.network_tip_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.network_tip_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.network_tip_label)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(1000, 20, 891, 271))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_title_label = QLabel(self.widget1)
        self.search_title_label.setObjectName(u"search_title_label")
        self.search_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.search_title_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton = QRadioButton(self.widget1)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.widget1)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 3, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)

        self.textEdit = QTextEdit(self.widget1)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)

        self.view_all_button = QPushButton(self.widget1)
        self.view_all_button.setObjectName(u"view_all_button")

        self.gridLayout.addWidget(self.view_all_button, 2, 1, 1, 1)

        self.search_button = QPushButton(self.widget1)
        self.search_button.setObjectName(u"search_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.search_button, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        Peruse.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Peruse)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
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
        self.scan_output_label.setText(QCoreApplication.translate("Peruse", u"Scan Output :", None))
        self.save_button.setText(QCoreApplication.translate("Peruse", u"Save", None))
        self.delete_button.setText(QCoreApplication.translate("Peruse", u"Delete", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Peruse", u"scan_id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Peruse", u"scan_datetime", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Peruse", u"network_name", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Peruse", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Peruse", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Peruse", u"2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Peruse", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Peruse", u"4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Peruse", u"adalkakmalknlaknvlaknvlakvnk", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Peruse", u"a", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Peruse", u"a", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Peruse", u"b", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Peruse", u"b", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Peruse", u"b", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Peruse", u"c", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Peruse", u"c", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Peruse", u"c", None));
        ___qtablewidgetitem17 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Peruse", u"d", None));
        ___qtablewidgetitem18 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Peruse", u"d", None));
        ___qtablewidgetitem19 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Peruse", u"d", None));
        ___qtablewidgetitem20 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Peruse", u"e", None));
        ___qtablewidgetitem21 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Peruse", u"e", None));
        ___qtablewidgetitem22 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Peruse", u"e", None));
        ___qtablewidgetitem23 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Peruse", u"f", None));
        ___qtablewidgetitem24 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Peruse", u"f", None));
        ___qtablewidgetitem25 = self.tableWidget.item(5, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Peruse", u"f", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.scan_title_label.setText(QCoreApplication.translate("Peruse", u"Scan a network", None))
        self.current_network_label.setText(QCoreApplication.translate("Peruse", u"Current network:", None))
        self.scan_button.setText(QCoreApplication.translate("Peruse", u"Scan", None))
        self.ip_range_label.setText(QCoreApplication.translate("Peruse", u"IP range:", None))
        self.cancel_button.setText(QCoreApplication.translate("Peruse", u"Cancel", None))
        self.network_tip_label.setText(QCoreApplication.translate("Peruse", u"If this is not a network that you own/want to scan, please change to the desired network. Also, as dictionary attacks (multiple login attempts) are used, please take note that it could potentially lock up your devices or cause other forms of harm.", None))
        self.search_title_label.setText(QCoreApplication.translate("Peruse", u"Search a scan", None))
        self.radioButton.setText(QCoreApplication.translate("Peruse", u"Password cracked", None))
        self.radioButton_3.setText(QCoreApplication.translate("Peruse", u"NA", None))
        self.radioButton_2.setText(QCoreApplication.translate("Peruse", u"Password not cracked", None))
        self.textEdit.setHtml(QCoreApplication.translate("Peruse", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Peruse", u"Enter search string here", None))
        self.view_all_button.setText(QCoreApplication.translate("Peruse", u"View All", None))
        self.search_button.setText(QCoreApplication.translate("Peruse", u"Search", None))
        self.menuScan.setTitle(QCoreApplication.translate("Peruse", u"Scan", None))
        self.menuTools.setTitle(QCoreApplication.translate("Peruse", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Peruse", u"Help", None))
    # retranslateUi

