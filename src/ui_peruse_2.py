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
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Peruse(object):
    def setupUi(self, Peruse):
        if not Peruse.objectName():
            Peruse.setObjectName(u"Peruse")
        Peruse.resize(1252, 776)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 1221, 701))
        self.gridLayout_4 = QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scan_title_label = QLabel(self.layoutWidget)
        self.scan_title_label.setObjectName(u"scan_title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scan_title_label.sizePolicy().hasHeightForWidth())
        self.scan_title_label.setSizePolicy(sizePolicy1)
        self.scan_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.scan_title_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.current_network_label = QLabel(self.layoutWidget)
        self.current_network_label.setObjectName(u"current_network_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.current_network_label.sizePolicy().hasHeightForWidth())
        self.current_network_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.current_network_label, 0, 0, 1, 2)

        self.current_network_lineEdit = QLineEdit(self.layoutWidget)
        self.current_network_lineEdit.setObjectName(u"current_network_lineEdit")
        self.current_network_lineEdit.setReadOnly(False)

        self.gridLayout_2.addWidget(self.current_network_lineEdit, 0, 2, 1, 1)

        self.ip_range_label = QLabel(self.layoutWidget)
        self.ip_range_label.setObjectName(u"ip_range_label")

        self.gridLayout_2.addWidget(self.ip_range_label, 1, 0, 1, 1)

        self.ip_range_lineEdit = QLineEdit(self.layoutWidget)
        self.ip_range_lineEdit.setObjectName(u"ip_range_lineEdit")
        self.ip_range_lineEdit.setReadOnly(False)

        self.gridLayout_2.addWidget(self.ip_range_lineEdit, 1, 1, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.scan_button = QPushButton(self.layoutWidget)
        self.scan_button.setObjectName(u"scan_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scan_button.sizePolicy().hasHeightForWidth())
        self.scan_button.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.scan_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.network_tip_label = QLabel(self.layoutWidget)
        self.network_tip_label.setObjectName(u"network_tip_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.network_tip_label.sizePolicy().hasHeightForWidth())
        self.network_tip_label.setSizePolicy(sizePolicy4)
        self.network_tip_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.network_tip_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.network_tip_label)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.vertical_line_1 = QFrame(self.layoutWidget)
        self.vertical_line_1.setObjectName(u"vertical_line_1")
        self.vertical_line_1.setFrameShape(QFrame.VLine)
        self.vertical_line_1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.vertical_line_1, 0, 1, 3, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.search_title_label = QLabel(self.layoutWidget)
        self.search_title_label.setObjectName(u"search_title_label")
        self.search_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.search_title_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)

        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.search_button = QPushButton(self.layoutWidget)
        self.search_button.setObjectName(u"search_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.search_button, 1, 1, 1, 1)

        self.search_textEdit = QTextEdit(self.layoutWidget)
        self.search_textEdit.setObjectName(u"search_textEdit")

        self.gridLayout.addWidget(self.search_textEdit, 0, 0, 1, 2)

        self.view_all_button = QPushButton(self.layoutWidget)
        self.view_all_button.setObjectName(u"view_all_button")

        self.gridLayout.addWidget(self.view_all_button, 2, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 3, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        self.horizontal_line_1 = QFrame(self.layoutWidget)
        self.horizontal_line_1.setObjectName(u"horizontal_line_1")
        self.horizontal_line_1.setFrameShape(QFrame.HLine)
        self.horizontal_line_1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.horizontal_line_1, 1, 0, 1, 1)

        self.horizontal_line_2 = QFrame(self.layoutWidget)
        self.horizontal_line_2.setObjectName(u"horizontal_line_2")
        self.horizontal_line_2.setFrameShape(QFrame.HLine)
        self.horizontal_line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.horizontal_line_2, 1, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.is_scanning_label = QLabel(self.layoutWidget)
        self.is_scanning_label.setObjectName(u"is_scanning_label")

        self.gridLayout_3.addWidget(self.is_scanning_label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scan_details_label = QLabel(self.layoutWidget)
        self.scan_details_label.setObjectName(u"scan_details_label")
        self.scan_details_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.scan_details_label)

        self.scan_details_tableWidget = QTableWidget(self.layoutWidget)
        if (self.scan_details_tableWidget.columnCount() < 5):
            self.scan_details_tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.scan_details_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.scan_details_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.scan_details_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.scan_details_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.scan_details_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.scan_details_tableWidget.setObjectName(u"scan_details_tableWidget")
        self.scan_details_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scan_details_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scan_details_tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.scan_details_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.scan_details_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.scan_details_tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.scan_details_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.scan_details_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.scan_details_tableWidget.verticalHeader().setHighlightSections(True)
        self.scan_details_tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.scan_details_tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_2.addWidget(self.scan_details_tableWidget)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.save_button = QPushButton(self.layoutWidget)
        self.save_button.setObjectName(u"save_button")
        sizePolicy3.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.save_button)

        self.clear_button = QPushButton(self.layoutWidget)
        self.clear_button.setObjectName(u"clear_button")
        sizePolicy3.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.clear_button)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.host_details_label = QLabel(self.layoutWidget)
        self.host_details_label.setObjectName(u"host_details_label")
        self.host_details_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_3.addWidget(self.host_details_label)

        self.host_details_tableWidget = QTableWidget(self.layoutWidget)
        if (self.host_details_tableWidget.columnCount() < 15):
            self.host_details_tableWidget.setColumnCount(15)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.host_details_tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem19)
        self.host_details_tableWidget.setObjectName(u"host_details_tableWidget")
        self.host_details_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.host_details_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.host_details_tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.host_details_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout_3.addWidget(self.host_details_tableWidget)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.is_searching_label = QLabel(self.layoutWidget)
        self.is_searching_label.setObjectName(u"is_searching_label")

        self.verticalLayout_3.addWidget(self.is_searching_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scans_tableWidget = QTableWidget(self.layoutWidget)
        self.scans_tableWidget.setObjectName(u"scans_tableWidget")
        font = QFont()
        font.setBold(False)
        self.scans_tableWidget.setFont(font)
        self.scans_tableWidget.setTabletTracking(True)
        self.scans_tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.scans_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.scans_tableWidget.setRowCount(0)
        self.scans_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.scans_tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_4.addWidget(self.scans_tableWidget)

        self.delete_button = QPushButton(self.layoutWidget)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy5.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.delete_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 2, 2, 1, 1)

        Peruse.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Peruse)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1252, 22))
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
        self.scan_title_label.setText(QCoreApplication.translate("Peruse", u"Scan a network", None))
        self.current_network_label.setText(QCoreApplication.translate("Peruse", u"Current network:", None))
        self.ip_range_label.setText(QCoreApplication.translate("Peruse", u"IP range:", None))
        self.scan_button.setText(QCoreApplication.translate("Peruse", u"Scan", None))
        self.network_tip_label.setText(QCoreApplication.translate("Peruse", u"If this is not a network that you own/want to scan, please change to the desired network. Also, as dictionary attacks (multiple login attempts) are used, please take note that it could potentially lock up your devices or cause other forms of harm.", None))
        self.search_title_label.setText(QCoreApplication.translate("Peruse", u"Search a scan", None))
        self.radioButton_2.setText(QCoreApplication.translate("Peruse", u"Password not cracked", None))
        self.radioButton.setText(QCoreApplication.translate("Peruse", u"Password cracked", None))
        self.search_button.setText(QCoreApplication.translate("Peruse", u"Search", None))
        self.search_textEdit.setHtml(QCoreApplication.translate("Peruse", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.search_textEdit.setPlaceholderText(QCoreApplication.translate("Peruse", u"Enter search string here", None))
        self.view_all_button.setText(QCoreApplication.translate("Peruse", u"View All", None))
        self.radioButton_3.setText(QCoreApplication.translate("Peruse", u"NA", None))
        self.is_scanning_label.setText(QCoreApplication.translate("Peruse", u"Not scanning currently, start a scan?", None))
        self.scan_details_label.setText(QCoreApplication.translate("Peruse", u"Scan details :", None))
        ___qtablewidgetitem = self.scan_details_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Peruse", u"Nmap Command", None));
        ___qtablewidgetitem1 = self.scan_details_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Peruse", u"Scan Type", None));
        ___qtablewidgetitem2 = self.scan_details_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Peruse", u"Date Time", None));
        ___qtablewidgetitem3 = self.scan_details_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Peruse", u"Time Elapsed", None));
        ___qtablewidgetitem4 = self.scan_details_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Peruse", u"Devices Detected", None));
        self.save_button.setText(QCoreApplication.translate("Peruse", u"Save", None))
        self.clear_button.setText(QCoreApplication.translate("Peruse", u"Clear", None))
        self.host_details_label.setText(QCoreApplication.translate("Peruse", u"Host details :", None))
        ___qtablewidgetitem5 = self.host_details_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Peruse", u"Device IP", None));
        ___qtablewidgetitem6 = self.host_details_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Peruse", u"Device Type", None));
        ___qtablewidgetitem7 = self.host_details_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Peruse", u"MAC Address", None));
        ___qtablewidgetitem8 = self.host_details_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Peruse", u"Vendor", None));
        ___qtablewidgetitem9 = self.host_details_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Peruse", u"Device Status", None));
        ___qtablewidgetitem10 = self.host_details_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Peruse", u"Service Name", None));
        ___qtablewidgetitem11 = self.host_details_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Peruse", u"Service Port", None));
        ___qtablewidgetitem12 = self.host_details_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Peruse", u"State", None));
        ___qtablewidgetitem13 = self.host_details_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Peruse", u"Software Product", None));
        ___qtablewidgetitem14 = self.host_details_tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Peruse", u"Service Version", None));
        ___qtablewidgetitem15 = self.host_details_tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Peruse", u"Version Information", None));
        ___qtablewidgetitem16 = self.host_details_tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Peruse", u"CPE (Common Platform Enumeration)", None));
        ___qtablewidgetitem17 = self.host_details_tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Peruse", u"Script", None));
        ___qtablewidgetitem18 = self.host_details_tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Peruse", u"Password Cracked", None));
        ___qtablewidgetitem19 = self.host_details_tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Peruse", u"Recommendation", None));
        self.is_searching_label.setText(QCoreApplication.translate("Peruse", u"Not searching currently, start a search?", None))
        self.delete_button.setText(QCoreApplication.translate("Peruse", u"Delete", None))
        self.menuScan.setTitle(QCoreApplication.translate("Peruse", u"Scan", None))
        self.menuTools.setTitle(QCoreApplication.translate("Peruse", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Peruse", u"Help", None))
    # retranslateUi

