# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/employee_ui/employee_pos/posCheckout.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1801, 872)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.navbar_2 = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbar_2.sizePolicy().hasHeightForWidth())
        self.navbar_2.setSizePolicy(sizePolicy)
        self.navbar_2.setStyleSheet("QWidget {\n"
"    border-right: 3px solid #D8DBD9;\n"
"}\n"
"")
        self.navbar_2.setObjectName("navbar_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.navbar_2)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.orderBTN = QtWidgets.QPushButton(self.navbar_2)
        self.orderBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.orderBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.orderBTN.setStyleSheet("QPushButton {\n"
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
        self.orderBTN.setObjectName("orderBTN")
        self.verticalLayout_6.addWidget(self.orderBTN)
        self.menuBTN = QtWidgets.QPushButton(self.navbar_2)
        self.menuBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.menuBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.menuBTN.setStyleSheet("QPushButton {\n"
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
        self.menuBTN.setObjectName("menuBTN")
        self.verticalLayout_6.addWidget(self.menuBTN)
        self.modifyBTN = QtWidgets.QPushButton(self.navbar_2)
        self.modifyBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.modifyBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.modifyBTN.setStyleSheet("QPushButton {\n"
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
        self.modifyBTN.setObjectName("modifyBTN")
        self.verticalLayout_6.addWidget(self.modifyBTN)
        self.checkoutBTN = QtWidgets.QPushButton(self.navbar_2)
        self.checkoutBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.checkoutBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.checkoutBTN.setStyleSheet("QPushButton {\n"
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
        self.checkoutBTN.setObjectName("checkoutBTN")
        self.verticalLayout_6.addWidget(self.checkoutBTN)
        self.historyBTN_2 = QtWidgets.QPushButton(self.navbar_2)
        self.historyBTN_2.setMinimumSize(QtCore.QSize(100, 100))
        self.historyBTN_2.setMaximumSize(QtCore.QSize(100, 100))
        self.historyBTN_2.setStyleSheet("QPushButton {\n"
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
        self.historyBTN_2.setObjectName("historyBTN_2")
        self.verticalLayout_6.addWidget(self.historyBTN_2)
        self.backBTN = QtWidgets.QPushButton(self.navbar_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBTN.sizePolicy().hasHeightForWidth())
        self.backBTN.setSizePolicy(sizePolicy)
        self.backBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.backBTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
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
        self.verticalLayout_6.addWidget(self.backBTN)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.navbar_2, 1, 0, 1, 1)
        self.header_2 = QtWidgets.QWidget(self.frame)
        self.header_2.setStyleSheet("QWidget {\n"
"    border-bottom: 3px solid #D8DBD9; \n"
"}\n"
"")
        self.header_2.setObjectName("header_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.header_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.header_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("QLabel {\n"
"    color: #67B99A;\n"
"    font-size: 45px;\n"
"}")
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_11 = QtWidgets.QLabel(self.header_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.gridLayout_2.addWidget(self.header_2, 0, 0, 1, 2)
        self.contentContainer_2 = QtWidgets.QFrame(self.frame)
        self.contentContainer_2.setObjectName("contentContainer_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.contentContainer_2)
        self.verticalLayout_8.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mainContent_2 = QtWidgets.QWidget(self.contentContainer_2)
        self.mainContent_2.setObjectName("mainContent_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainContent_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Checkout = QtWidgets.QWidget(self.mainContent_2)
        self.Checkout.setMinimumSize(QtCore.QSize(500, 0))
        self.Checkout.setMaximumSize(QtCore.QSize(500, 16777215))
        self.Checkout.setObjectName("Checkout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Checkout)
        self.verticalLayout_4.setContentsMargins(0, 0, 15, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.Checkout)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.widget_3 = QtWidgets.QWidget(self.Checkout)
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setContentsMargins(0, 15, 0, 15)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.packageDISPLAY = QtWidgets.QLabel(self.widget_3)
        self.packageDISPLAY.setText("")
        self.packageDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.packageDISPLAY.setObjectName("packageDISPLAY")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.packageDISPLAY)
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cashierDISPLAY = QtWidgets.QLabel(self.widget_3)
        self.cashierDISPLAY.setText("")
        self.cashierDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cashierDISPLAY.setObjectName("cashierDISPLAY")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cashierDISPLAY)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.customerFIELD = QtWidgets.QLabel(self.widget_3)
        self.customerFIELD.setText("")
        self.customerFIELD.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.customerFIELD.setObjectName("customerFIELD")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.customerFIELD)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.orderList = QtWidgets.QTableWidget(self.Checkout)
        self.orderList.setObjectName("orderList")
        self.orderList.setColumnCount(0)
        self.orderList.setRowCount(0)
        self.verticalLayout_4.addWidget(self.orderList)
        self.widget_4 = QtWidgets.QWidget(self.Checkout)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_4)
        self.formLayout_2.setContentsMargins(0, 15, 0, 15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.subtotalDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.subtotalDISPLAY.setText("")
        self.subtotalDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subtotalDISPLAY.setObjectName("subtotalDISPLAY")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.subtotalDISPLAY)
        self.vatDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.vatDISPLAY.setText("")
        self.vatDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vatDISPLAY.setObjectName("vatDISPLAY")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.vatDISPLAY)
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.leftoverDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.leftoverDISPLAY.setText("")
        self.leftoverDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leftoverDISPLAY.setObjectName("leftoverDISPLAY")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.leftoverDISPLAY)
        self.discountDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.discountDISPLAY.setText("")
        self.discountDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.discountDISPLAY.setObjectName("discountDISPLAY")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.discountDISPLAY)
        self.addonsAmountDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.addonsAmountDISPLAY.setText("")
        self.addonsAmountDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.addonsAmountDISPLAY.setObjectName("addonsAmountDISPLAY")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.addonsAmountDISPLAY)
        self.packageAmountDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.packageAmountDISPLAY.setText("")
        self.packageAmountDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.packageAmountDISPLAY.setObjectName("packageAmountDISPLAY")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.packageAmountDISPLAY)
        self.label_29 = QtWidgets.QLabel(self.widget_4)
        self.label_29.setObjectName("label_29")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.changeDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.changeDISPLAY.setText("")
        self.changeDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.changeDISPLAY.setObjectName("changeDISPLAY")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.changeDISPLAY)
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.paymentmethodDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.paymentmethodDISPLAY.setText("")
        self.paymentmethodDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paymentmethodDISPLAY.setObjectName("paymentmethodDISPLAY")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.paymentmethodDISPLAY)
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.referenceidDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.referenceidDISPLAY.setText("")
        self.referenceidDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.referenceidDISPLAY.setObjectName("referenceidDISPLAY")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.referenceidDISPLAY)
        self.label_17 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.totalamountDISPLAY = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.totalamountDISPLAY.setFont(font)
        self.totalamountDISPLAY.setText("")
        self.totalamountDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalamountDISPLAY.setObjectName("totalamountDISPLAY")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.totalamountDISPLAY)
        self.label_22 = QtWidgets.QLabel(self.widget_4)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.cashamountDISPLAY = QtWidgets.QLabel(self.widget_4)
        self.cashamountDISPLAY.setText("")
        self.cashamountDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cashamountDISPLAY.setObjectName("cashamountDISPLAY")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.cashamountDISPLAY)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.frame_2 = QtWidgets.QFrame(self.Checkout)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.orderidBOX = QtWidgets.QComboBox(self.frame_2)
        self.orderidBOX.setStyleSheet("QComboBox {\n"
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
        self.orderidBOX.setObjectName("orderidBOX")
        self.verticalLayout.addWidget(self.orderidBOX)
        self.checkoutBTN_3 = QtWidgets.QPushButton(self.frame_2)
        self.checkoutBTN_3.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.checkoutBTN_3.setObjectName("checkoutBTN_3")
        self.verticalLayout.addWidget(self.checkoutBTN_3)
        self.checkoutBTN_2 = QtWidgets.QPushButton(self.frame_2)
        self.checkoutBTN_2.setMinimumSize(QtCore.QSize(0, 50))
        self.checkoutBTN_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.checkoutBTN_2.setStyleSheet("QPushButton {\n"
"    background-color: #F1A40E;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E1920C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C77908;\n"
"}\n"
"")
        self.checkoutBTN_2.setObjectName("checkoutBTN_2")
        self.verticalLayout.addWidget(self.checkoutBTN_2)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.Checkout)
        self.PaymentMethod = QtWidgets.QWidget(self.mainContent_2)
        self.PaymentMethod.setMinimumSize(QtCore.QSize(500, 0))
        self.PaymentMethod.setMaximumSize(QtCore.QSize(500, 16777215))
        self.PaymentMethod.setObjectName("PaymentMethod")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.PaymentMethod)
        self.verticalLayout_3.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.PaymentMethod)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, 15, -1, 15)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_23 = QtWidgets.QLabel(self.PaymentMethod)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.amountFIELD = QtWidgets.QLineEdit(self.PaymentMethod)
        self.amountFIELD.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"")
        self.amountFIELD.setObjectName("amountFIELD")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.amountFIELD)
        self.label_24 = QtWidgets.QLabel(self.PaymentMethod)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_25 = QtWidgets.QLabel(self.PaymentMethod)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.referenceFIELD = QtWidgets.QLineEdit(self.PaymentMethod)
        self.referenceFIELD.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"")
        self.referenceFIELD.setObjectName("referenceFIELD")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.referenceFIELD)
        self.label_30 = QtWidgets.QLabel(self.PaymentMethod)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.setBTN = QtWidgets.QPushButton(self.PaymentMethod)
        self.setBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.setBTN.setObjectName("setBTN")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.setBTN)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.label_21 = QtWidgets.QLabel(self.PaymentMethod)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(-1, 15, -1, -1)
        self.formLayout_4.setHorizontalSpacing(20)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_31 = QtWidgets.QLabel(self.PaymentMethod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setObjectName("label_31")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.discountBOX = QtWidgets.QComboBox(self.PaymentMethod)
        self.discountBOX.setStyleSheet("QComboBox {\n"
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
        self.discountBOX.setObjectName("discountBOX")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.discountBOX)
        self.label_18 = QtWidgets.QLabel(self.PaymentMethod)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.leftoverBOX = QtWidgets.QComboBox(self.PaymentMethod)
        self.leftoverBOX.setStyleSheet("QComboBox {\n"
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
        self.leftoverBOX.setObjectName("leftoverBOX")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leftoverBOX)
        self.saveBTN = QtWidgets.QPushButton(self.PaymentMethod)
        self.saveBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.saveBTN.setObjectName("saveBTN")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.saveBTN)
        self.verticalLayout_3.addLayout(self.formLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.PaymentMethod)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_8.addWidget(self.mainContent_2)
        self.gridLayout_2.addWidget(self.contentContainer_2, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orderBTN.setText(_translate("MainWindow", "Order"))
        self.menuBTN.setText(_translate("MainWindow", "Menu"))
        self.modifyBTN.setText(_translate("MainWindow", "Modify"))
        self.checkoutBTN.setText(_translate("MainWindow", "Checkout"))
        self.historyBTN_2.setText(_translate("MainWindow", "History"))
        self.backBTN.setText(_translate("MainWindow", "Back"))
        self.label_10.setText(_translate("MainWindow", "POS"))
        self.label_11.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.label_2.setText(_translate("MainWindow", "Checkout"))
        self.label_8.setText(_translate("MainWindow", "Order ID"))
        self.label_12.setText(_translate("MainWindow", "Package Name"))
        self.label.setText(_translate("MainWindow", "Cashier"))
        self.label_6.setText(_translate("MainWindow", "Customer Name"))
        self.label_3.setText(_translate("MainWindow", "Subtotal"))
        self.label_5.setText(_translate("MainWindow", "Vat (12%)"))
        self.label_13.setText(_translate("MainWindow", "Total Package Amount"))
        self.label_14.setText(_translate("MainWindow", "Total Add-ons Amount"))
        self.label_16.setText(_translate("MainWindow", "Leftover Cost"))
        self.label_15.setText(_translate("MainWindow", "Discount (Senior/PWD)"))
        self.label_29.setText(_translate("MainWindow", "Change Amount"))
        self.label_19.setText(_translate("MainWindow", "Payment Method"))
        self.label_20.setText(_translate("MainWindow", "Reference ID (GCash)"))
        self.label_17.setText(_translate("MainWindow", "Payment"))
        self.label_22.setText(_translate("MainWindow", "Cash Amount"))
        self.checkoutBTN_3.setText(_translate("MainWindow", "Check Order ID"))
        self.checkoutBTN_2.setText(_translate("MainWindow", "Checkout"))
        self.label_9.setText(_translate("MainWindow", "Payment Method"))
        self.label_23.setText(_translate("MainWindow", "Amount Tendered"))
        self.amountFIELD.setPlaceholderText(_translate("MainWindow", "Enter Amount"))
        self.label_24.setText(_translate("MainWindow", "Gcash"))
        self.label_25.setText(_translate("MainWindow", "Reference Number"))
        self.referenceFIELD.setPlaceholderText(_translate("MainWindow", "Enter Gcash Reference Number"))
        self.label_30.setText(_translate("MainWindow", "Cash"))
        self.setBTN.setText(_translate("MainWindow", "Enter"))
        self.label_21.setText(_translate("MainWindow", "Apply Discount/Leftover"))
        self.label_31.setText(_translate("MainWindow", "Discount               "))
        self.label_18.setText(_translate("MainWindow", "Leftover         "))
        self.saveBTN.setText(_translate("MainWindow", "Save changes"))
import assets.resourceFile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
