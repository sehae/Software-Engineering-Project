# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory_Barcode.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import assets.resourceFile_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.pushButton_3 = QtWidgets.QPushButton(self.navbar)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.navbar)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_10 = QtWidgets.QPushButton(self.navbar)
        self.pushButton_10.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_10.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
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
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton = QtWidgets.QPushButton(self.navbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/Icons/entypo_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
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
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)
        self.Content = QtWidgets.QFrame(self.frame)
        self.Content.setObjectName("Content")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Content)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.Content)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(75, 75, 75, 75)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 25px;\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_3.addWidget(self.widget_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout_4.addWidget(self.widget)
        self.gridLayout.addWidget(self.Content, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Inventory"))
        self.pushButton_2.setText(_translate("MainWindow", "Modify"))
        self.pushButton_10.setText(_translate("MainWindow", "Barcode"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "INVENTORY"))
        self.label_2.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.label_3.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.label_4.setText(_translate("MainWindow", "Available: Bar Code Scanner"))
        self.pushButton_4.setText(_translate("MainWindow", "Scan"))
        self.pushButton_5.setText(_translate("MainWindow", "Stop"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())