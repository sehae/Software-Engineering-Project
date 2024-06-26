from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer, pyqtSignal
from screens.help_screen.help_FAQ import Ui_MainWindow
from shared.navigation_signal import auth_back
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager


class helpFAQ(QMainWindow, Ui_MainWindow):
    support_signal = pyqtSignal()
    back_signal = pyqtSignal()
    manual_signal = pyqtSignal()
    back_kitchen_signal = pyqtSignal()
    back_cashier_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.support_signal.emit)
        self.backButton_3.clicked.connect(lambda: auth_back(self.user_manager, self.back_signal,
                                                            self.back_kitchen_signal, self.back_cashier_signal))
        self.editUserButton_3.clicked.connect(self.manual_signal.emit)

        # Create an instance of userManager
        self.user_manager = userManager()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def update_user_type(self, user_type):
        self.user_type = user_type

    def navigate_support(self):
        self.support_signal.emit()

    def navigate_manual(self):
        self.manual_signal.emit()

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")
        self.sysTimeDate_3.setText(formattedDateTime)