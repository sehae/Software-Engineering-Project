from screens.admin_screens.admin_dashboard.adminDashboard_functions import myAdminDashboard
from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow
from shared.imports import *


from validator.user_manager import userManager

user_manager_instance = userManager()


class myLoginScreen(QMainWindow, Ui_MainWindow):
    login_successful = QtCore.pyqtSignal()
    login_successful_employee = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Pass the userManager instance
        self.user_manager = user_manager_instance
        self.user_type = None
        self.user_manager.user_type_updated.connect(self.print_user_type)  # Connect signal to slot

        self.loginButton.clicked.connect(self.logs)
        self.loginButton.clicked.connect(self.logs)
        self.visibilityButton.clicked.connect(self.toggle_password_visibility)
        self.UiComponents()


    def UiComponents(self):
        icon = QtGui.QIcon()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QIcon.Normal, QIcon.On)
        self.visibilityButton.setIcon(icon)

    def print_user_type(self, user_type):
        print(f"MYLOGINSCREEN: User type set to: {user_type}")


    def toggle_password_visibility(self):
        if self.password.echoMode() == QtWidgets.QLineEdit.Password:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOn.png"))
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOff.png"))

    def logs(self):
        username = self.userName.text()
        provided_password = self.password.text()

        try:
            cursor = conn.cursor()

            # Query the adminlogin table
            cursor.execute(GET_ADMIN_LOGIN, (username,))
            result = cursor.fetchone()

            if result:
                admin_id, stored_password, is_active = result

                # Verify the provided password against the stored password
                if verify_password(stored_password, provided_password):
                    if is_active:
                        cursor.execute(GET_ADMIN_FIRST_NAME, (admin_id,))
                        admin_first_name = cursor.fetchone()[0]
                        print(f"Login successful as admin: Welcome {admin_first_name}!")
                        self.user_type = "admin"
                        print(self.user_type)
                        self.user_manager.set_user_type(self.user_type)  # Update user type in userManager
                        self.login_successful.emit()
                        return
                    else:
                        print("Account is disabled.")
                        return
                else:
                    print("Incorrect password.")

            # Query the employeelogin table
            cursor.execute(GET_EMPLOYEE_LOGIN, (username,))
            result = cursor.fetchone()

            if result:
                employee_id, stored_password, is_active = result

                # Verify the provided password against the stored password
                if verify_password(stored_password, provided_password):
                    if is_active:
                        cursor.execute(GET_EMPLOYEE_FIRST_NAME, (employee_id,))
                        employee_first_name = cursor.fetchone()[0]
                        print(f"Login successful as Employee: Welcome {employee_first_name}!")
                        self.user_type = "employee"
                        print(self.user_type)
                        self.user_manager.set_user_type(self.user_type)  # Update user type in userManager
                        self.login_successful_employee.emit()
                        return
                    else:
                        print("Account is disabled.")
                        return
                else:
                    print("Incorrect password.")

            print("Invalid Credentials")
            show_error_message("Invalid Credentials.", "Please check your username and password.")

        except Exception as e:
            print(f"An error occurred during login: {e}")
            show_error_message("Error", f"An error occurred during login: {e}")
        finally:
            cursor.close()
