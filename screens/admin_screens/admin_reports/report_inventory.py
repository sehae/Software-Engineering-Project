# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/admin_ui/admin_reports/report_inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.navbar = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        self.navbar.setSizePolicy(sizePolicy)
        self.navbar.setStyleSheet("QWidget {\n"
"    border-right: 3px solid #D8DBD9;\n"
"}\n"
"")
        self.navbar.setObjectName("navbar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.navbar)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.salesReportBTN = QtWidgets.QPushButton(self.navbar)
        self.salesReportBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.salesReportBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.salesReportBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.salesReportBTN.setObjectName("salesReportBTN")
        self.verticalLayout_2.addWidget(self.salesReportBTN)
        self.inventoryReportBTN = QtWidgets.QPushButton(self.navbar)
        self.inventoryReportBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.inventoryReportBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.inventoryReportBTN.setAutoFillBackground(False)
        self.inventoryReportBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.inventoryReportBTN.setObjectName("inventoryReportBTN")
        self.verticalLayout_2.addWidget(self.inventoryReportBTN)
        self.trendAnalysisBTN = QtWidgets.QPushButton(self.navbar)
        self.trendAnalysisBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.trendAnalysisBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.trendAnalysisBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.trendAnalysisBTN.setObjectName("trendAnalysisBTN")
        self.verticalLayout_2.addWidget(self.trendAnalysisBTN)
        self.backBTN = QtWidgets.QPushButton(self.navbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBTN.sizePolicy().hasHeightForWidth())
        self.backBTN.setSizePolicy(sizePolicy)
        self.backBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.backBTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backBTN.setFont(font)
        self.backBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.backBTN.setAutoRepeat(False)
        self.backBTN.setObjectName("backBTN")
        self.verticalLayout_2.addWidget(self.backBTN)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.navbar, 1, 0, 1, 1)
        self.header = QtWidgets.QWidget(self.frame)
        self.header.setStyleSheet("QWidget {\n"
"    border-bottom: 3px solid #D8DBD9; \n"
"}\n"
"")
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel {\n"
"    color: #67B99A;\n"
"    font-size: 45px;\n"
"}")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.sysTimeDate = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sysTimeDate.setFont(font)
        self.sysTimeDate.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.sysTimeDate.setObjectName("sysTimeDate")
        self.horizontalLayout_2.addWidget(self.sysTimeDate)
        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)
        self.Content = QtWidgets.QFrame(self.frame)
        self.Content.setObjectName("Content")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.Content)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.automaticbackupLBL = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.automaticbackupLBL.setFont(font)
        self.automaticbackupLBL.setObjectName("automaticbackupLBL")
        self.verticalLayout_5.addWidget(self.automaticbackupLBL)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem3)
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.frequencyLBL = QtWidgets.QLabel(self.widget)
        self.frequencyLBL.setObjectName("frequencyLBL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLBL)
        self.frequencyBOX = QtWidgets.QComboBox(self.widget)
        self.frequencyBOX.setMinimumSize(QtCore.QSize(270, 0))
        self.frequencyBOX.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frequencyBOX.setStyleSheet("QComboBox {\n"
"    padding: 5px;\n"
"    border: 2px solid #07BEB8;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 20px;\n"
"    border-left: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/logos/Icons/gridicons_dropdown.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}")
        self.frequencyBOX.setObjectName("frequencyBOX")
        self.frequencyBOX.addItem("")
        self.frequencyBOX.addItem("")
        self.frequencyBOX.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frequencyBOX)
        self.filelocLBL = QtWidgets.QLabel(self.widget)
        self.filelocLBL.setObjectName("filelocLBL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.filelocLBL)
        self.filelocDISPLAY = QtWidgets.QLabel(self.widget)
        self.filelocDISPLAY.setObjectName("filelocDISPLAY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.filelocDISPLAY)
        self.verticalLayout_5.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.viewBTN = QtWidgets.QPushButton(self.widget_2)
        self.viewBTN.setMinimumSize(QtCore.QSize(400, 0))
        self.viewBTN.setMaximumSize(QtCore.QSize(400, 16777215))
        self.viewBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.viewBTN.setObjectName("viewBTN")
        self.verticalLayout.addWidget(self.viewBTN)
        self.selectfolderBTN = QtWidgets.QPushButton(self.widget_2)
        self.selectfolderBTN.setMinimumSize(QtCore.QSize(400, 0))
        self.selectfolderBTN.setMaximumSize(QtCore.QSize(400, 16777215))
        self.selectfolderBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.selectfolderBTN.setObjectName("selectfolderBTN")
        self.verticalLayout.addWidget(self.selectfolderBTN)
        self.generateBTN = QtWidgets.QPushButton(self.widget_2)
        self.generateBTN.setMinimumSize(QtCore.QSize(400, 50))
        self.generateBTN.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setBold(False)
        self.generateBTN.setFont(font)
        self.generateBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.generateBTN.setObjectName("generateBTN")
        self.verticalLayout.addWidget(self.generateBTN)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5.addWidget(self.widget_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.scrollArea = QtWidgets.QScrollArea(self.Content)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1090, 656, 1977))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.levelView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.levelView.setMinimumSize(QtCore.QSize(0, 600))
        self.levelView.setMaximumSize(QtCore.QSize(16777215, 600))
        self.levelView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.levelView.setObjectName("levelView")
        self.verticalLayout_3.addWidget(self.levelView)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.statusView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.statusView.setMinimumSize(QtCore.QSize(0, 600))
        self.statusView.setMaximumSize(QtCore.QSize(16777215, 600))
        self.statusView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.statusView.setObjectName("statusView")
        self.verticalLayout_3.addWidget(self.statusView)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.expiryView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.expiryView.setMinimumSize(QtCore.QSize(0, 600))
        self.expiryView.setMaximumSize(QtCore.QSize(16777215, 600))
        self.expiryView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.expiryView.setObjectName("expiryView")
        self.verticalLayout_3.addWidget(self.expiryView)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.Content, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.salesReportBTN.setText(_translate("MainWindow", "Sales\n"
"Report"))
        self.inventoryReportBTN.setText(_translate("MainWindow", "Inventory\n"
"Report"))
        self.trendAnalysisBTN.setText(_translate("MainWindow", "Trend\n"
"Analysis"))
        self.backBTN.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "REPORTS"))
        self.sysTimeDate.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.automaticbackupLBL.setText(_translate("MainWindow", "Inventory Report"))
        self.frequencyLBL.setText(_translate("MainWindow", "Report Frequency"))
        self.frequencyBOX.setItemText(0, _translate("MainWindow", "Daily"))
        self.frequencyBOX.setItemText(1, _translate("MainWindow", "Weekly"))
        self.frequencyBOX.setItemText(2, _translate("MainWindow", "Monthly"))
        self.filelocLBL.setText(_translate("MainWindow", "Excel Location"))
        self.filelocDISPLAY.setText(_translate("MainWindow", "You don\'t have current excel location..."))
        self.viewBTN.setText(_translate("MainWindow", "View Excel Location"))
        self.selectfolderBTN.setText(_translate("MainWindow", "Select Excel Location"))
        self.generateBTN.setText(_translate("MainWindow", "Generate Report"))
        self.label_2.setText(_translate("MainWindow", "Inventory Levels by Products"))
        self.label_3.setText(_translate("MainWindow", "Inventory Status Overview"))
        self.label_4.setText(_translate("MainWindow", "Expiry Date Analysis"))
import assets.resourceFile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
