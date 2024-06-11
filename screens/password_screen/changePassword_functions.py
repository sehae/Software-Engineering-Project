from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from screens.password_screen.changePassword import Ui_MainWindow
from server.local_server import conn
from security.hash import hash_password
from shared.dialog import show_error_message
from validator.password_validator import isValidPassword
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.password_screen.changePassword import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager


class changePassword(QMainWindow, Ui_MainWindow):
    back_signal = pyqtSignal()
    back_employee_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backBTN.clicked.connect(self.back)

        # Create an instance of userManager
        self.user_manager = userManager()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        self.check_action = None
        self.saveBTN.clicked.connect(self.change_password)
        self.cp_visibility.clicked.connect(lambda: self.toggle_visibility(self.currentPassFIELD, self.cp_visibility))
        self.np_visibility.clicked.connect(lambda: self.toggle_visibility(self.newPassFIELD, self.np_visibility))
        self.rp_visibility.clicked.connect(lambda: self.toggle_visibility(self.retypeFIELD, self.rp_visibility))

        self.UiComponents()

    def back(self):
        updated_user_type = self.user_manager.updated_userType
        print(f"Updated user type: {updated_user_type}")
        if updated_user_type == "admin":
            print("You clicked back as an admin")
            self.back_signal.emit()
        elif updated_user_type == "employee":
            print("You clicked back as an employee")
            self.back_employee_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)

    def UiComponents(self):
        self.currentPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retypeFIELD.setEchoMode(QtWidgets.QLineEdit.Password)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QIcon.Normal, QIcon.On)
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
        username = self.userName.text()
        current_password = self.currentPassFIELD.text()
        new_password = self.newPassFIELD.text()
        retype_password = self.retypeFIELD.text()

        if not username or not current_password or not new_password or not retype_password:
            show_error_message("Error", "All fields must be filled. Please fill in the fields before changing your "
                                        "password.")
            return

        if new_password != retype_password:
            show_error_message("Error", "Passwords do not match. Please retype your new password.")

            return

        if new_password == current_password:
            show_error_message("Error", "New password must be different from your current password.")
            return

        if new_password == retype_password:
            if not isValidPassword(new_password):
                return

            hashed_password = hash_password(new_password)
            cursor = conn.cursor()