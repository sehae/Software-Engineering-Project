# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/admin_ui/adminDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 952)
        self.mainwidget = QtWidgets.QWidget(MainWindow)
        self.mainwidget.setObjectName("mainwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(self.stackedWidgetPage1)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QLabel(self.widget_3)
        self.logo.setEnabled(True)
        self.logo.setMaximumSize(QtCore.QSize(250, 80))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setPixmap(QtGui.QPixmap(":/logos/Icons/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.widget_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.username = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.widget = QtWidgets.QWidget(self.header)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.date = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date.setFont(font)
        self.date.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.date.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.date.setWordWrap(False)
        self.date.setIndent(-1)
        self.date.setObjectName("date")
        self.verticalLayout_3.addWidget(self.date)
        self.time = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time.setFont(font)
        self.time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.time.setObjectName("time")
        self.verticalLayout_3.addWidget(self.time)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.header)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonGroup = QtWidgets.QWidget(self.stackedWidgetPage1)
        self.buttonGroup.setObjectName("buttonGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.buttonGroup)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setObjectName("gridLayout")
        self.maintenanceButton = QtWidgets.QPushButton(self.buttonGroup)
        self.maintenanceButton.setMinimumSize(QtCore.QSize(400, 240))
        self.maintenanceButton.setMaximumSize(QtCore.QSize(400, 280))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.maintenanceButton.setFont(font)
        self.maintenanceButton.setAutoFillBackground(False)
        self.maintenanceButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/maintenanceIcon.png) center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.maintenanceButton.setIconSize(QtCore.QSize(200, 200))
        self.maintenanceButton.setAutoRepeat(False)
        self.maintenanceButton.setAutoExclusive(False)
        self.maintenanceButton.setAutoDefault(False)
        self.maintenanceButton.setDefault(False)
        self.maintenanceButton.setFlat(False)
        self.maintenanceButton.setObjectName("maintenanceButton")
        self.gridLayout.addWidget(self.maintenanceButton, 0, 0, 1, 1)
        self.logoutButton = QtWidgets.QPushButton(self.buttonGroup)
        self.logoutButton.setMinimumSize(QtCore.QSize(400, 240))
        self.logoutButton.setMaximumSize(QtCore.QSize(400, 280))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/logoutIcon.png) center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout.addWidget(self.logoutButton, 2, 1, 1, 1)
        self.posButton = QtWidgets.QPushButton(self.buttonGroup)
        self.posButton.setMinimumSize(QtCore.QSize(400, 240))
        self.posButton.setMaximumSize(QtCore.QSize(400, 240))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.posButton.setFont(font)
        self.posButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/posIcon.png) center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.posButton.setObjectName("posButton")
        self.gridLayout.addWidget(self.posButton, 0, 1, 1, 1)
        self.aboutButton = QtWidgets.QPushButton(self.buttonGroup)
        self.aboutButton.setMinimumSize(QtCore.QSize(400, 240))
        self.aboutButton.setMaximumSize(QtCore.QSize(400, 280))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.aboutButton.setFont(font)
        self.aboutButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/aboutIcon.png) center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.aboutButton.setObjectName("aboutButton")
        self.gridLayout.addWidget(self.aboutButton, 2, 0, 1, 1)
        self.helpButton = QtWidgets.QPushButton(self.buttonGroup)
        self.helpButton.setMinimumSize(QtCore.QSize(400, 240))
        self.helpButton.setMaximumSize(QtCore.QSize(400, 280))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.helpButton.setFont(font)
        self.helpButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/helpIcon.png) center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.helpButton.setObjectName("helpButton")
        self.gridLayout.addWidget(self.helpButton, 1, 2, 1, 1)
        self.changePassButton = QtWidgets.QPushButton(self.buttonGroup)
        self.changePassButton.setMinimumSize(QtCore.QSize(400, 240))
        self.changePassButton.setMaximumSize(QtCore.QSize(400, 280))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.changePassButton.setFont(font)
        self.changePassButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/changePassIcon.png) center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.changePassButton.setObjectName("changePassButton")
        self.gridLayout.addWidget(self.changePassButton, 1, 1, 1, 1)
        self.reportsButton = QtWidgets.QPushButton(self.buttonGroup)
        self.reportsButton.setMinimumSize(QtCore.QSize(400, 240))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.reportsButton.setFont(font)
        self.reportsButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/reportsIcon.png) center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.reportsButton.setObjectName("reportsButton")
        self.gridLayout.addWidget(self.reportsButton, 1, 0, 1, 1)
        self.inventoryButton = QtWidgets.QPushButton(self.buttonGroup)
        self.inventoryButton.setMinimumSize(QtCore.QSize(400, 240))
        self.inventoryButton.setMaximumSize(QtCore.QSize(400, 280))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.inventoryButton.setFont(font)
        self.inventoryButton.setStyleSheet("QPushButton {\n"
"    background: #07BEB8 url(:/logos/Icons/inventoryIcon.png)center no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding-top: 160px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5FCAC4;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #058A84;\n"
"}\n"
"")
        self.inventoryButton.setObjectName("inventoryButton")
        self.gridLayout.addWidget(self.inventoryButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.buttonGroup)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.mainwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Admin"))
        self.username.setText(_translate("MainWindow", "John Doe"))
        self.date.setText(_translate("MainWindow", "Wednesday, November 29, 2023 "))
        self.time.setText(_translate("MainWindow", "12:00:02 am"))
        self.maintenanceButton.setText(_translate("MainWindow", "MAINTENANCE"))
        self.logoutButton.setText(_translate("MainWindow", "LOGOUT"))
        self.posButton.setText(_translate("MainWindow", "POS"))
        self.aboutButton.setText(_translate("MainWindow", "ABOUT"))
        self.helpButton.setText(_translate("MainWindow", "HELP"))
        self.changePassButton.setText(_translate("MainWindow", "CHANGE PASSWORD"))
        self.reportsButton.setText(_translate("MainWindow", "REPORTS"))
        self.inventoryButton.setText(_translate("MainWindow", "INVENTORY"))
import assets.resourceFile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
