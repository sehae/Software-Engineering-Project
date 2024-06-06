from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from screens.password_screen.changePassword import Ui_MainWindow
from server.local_server import conn
from security.hash import hash_password
from shared.dialog import show_error_message
from validator.password_validator import isValidPassword


class ChangePassword(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.check_action = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.saveBTN.clicked.connect(self.change_password)

    def UiComponents(self):
        self.currentPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retypeFIELD.setEchoMode(QtWidgets.QLineEdit.Password)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QIcon.Normal, QIcon.On)
        self.un_visibility.setIcon(icon)
        self.cp_visibility.setIcon(icon)
        self.np_visibility.setIcon(icon)
        self.rp_visibility.setIcon(icon)


    def toggle_visibility(self, field, button):
        if field.echoMode() == QtWidgets.QLineEdit.Password:
            field.setEchoMode(QtWidgets.QLineEdit.Normal)
            button.setIcon(QtGui.QIcon("assets/Icons/visibilityOn.png"))
        else:
            field.setEchoMode(QtWidgets.QLineEdit.Password)
            button.setIcon(QtGui.QIcon("assets/Icons/visibilityOff.png"))


    def check_password_match(self):
        if self.newPassFIELD.text() == self.retypeFIELD.text():
            check_icon = QIcon("assets/Icons/check.png")
            self.check_action = QAction(check_icon, "Passwords Match", self.newPassFIELD)

            self.newPassFIELD.addAction(self.check_action, QtWidgets.QLineEdit.TrailingPosition)
            self.retypeFIELD.addAction(self.check_action, QtWidgets.QLineEdit.TrailingPosition)
        else:
            if self.check_action:
                self.newPassFIELD.removeAction(self.check_action)
                self.retypeFIELD.removeAction(self.check_action)

    def change_password(self):

