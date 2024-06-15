from PyQt5.QtCore import QDateTime, QTimer

from shared.imports import *
from screens.admin_screens.admin_maintenance.maintenanceEDIT import Ui_MainWindow


class adminMaintenanceEDIT(QMainWindow, Ui_MainWindow):
    add_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.active_button_style = ACTIVE_BUTTON_STYLE
        self.inactive_button_style = INACTIVE_BUTTON_STYLE

        self.saveBTN.clicked.connect(self.edit_user)
        self.adduserBTN.clicked.connect(self.add_user)
        self.backBTN.clicked.connect(self.back)
        self.searchFIELD.returnPressed.connect(self.search_user)
        self.staffBTN.clicked.connect(self.activate_staff)
        self.adminBTN.clicked.connect(self.activate_admin)
        self.cashierBTN.clicked.connect(self.activate_cashier)
        self.kitchenBTN.clicked.connect(self.activate_kitchen)
        self.userlogsBTN.clicked.connect(self.show_rightcontent)
        self.deactBTN.clicked.connect(self.deactivate_user)
        self.discardBTN.clicked.connect(self.discard)
        self.rightcontent.hide()
        self.edituserCONTENT.hide()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.dateDISPLAY.setText(formattedDateTime)

    def add_user(self):
        self.add_signal.emit()

    def back(self):
        self.back_signal.emit()

    def edit_user(self):
        email = self.emailDISPLAY.text()
        department = self.get_active_department()

        cursor = conn.cursor()

        # Check if the user is an admin
        if self.adminBTN.styleSheet() == self.active_button_style:
            try:
                cursor.execute(GET_ADMIN_DATA, (email,))
                result = cursor.fetchone()

                if result is None:
                    # If user doesn't have data in the admin table
                    cursor.execute(MOVE_TO_ADMIN, (email,))
                else:
                    cursor.execute(ENABLE_ADMIN, (email,))

                cursor.execute(DISABLE_EMPLOYEE, (email,))

                conn.commit()
                print(f"{email} moved to admin table")
            except Exception as e:
                print(f"An error occurred: {e}")

        # Check if the user is a staff
        elif self.staffBTN.styleSheet() == self.active_button_style:
            try:
                cursor.execute(GET_EMPLOYEE_DATA(email,))
                result = cursor.fetchone()

                if result is None:
                    cursor.execute(MOVE_TO_EMPLOYEE(department, email,))
                else:
                    cursor.execute(UPDATE_EMPLOYEE_DEPARTMENT, (department, email,))

                cursor.execute(DISABLE_ADMIN, (email,))

                conn.commit()
                print(f"{email} moved to employee table")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("No role selected")

    def get_active_department(self):
        if self.cashierBTN.styleSheet() == self.active_button_style:
            return 'Cashier'
        elif self.kitchenBTN.styleSheet() == self.active_button_style:
            return 'Kitchen'
        else:
            return None

    def search_user(self):
        try:
            search_text = self.searchFIELD.text()
            cursor = conn.cursor()

            cursor.execute(SEARCH_EMPLOYEE, (search_text, search_text, search_text))
            results = cursor.fetchall()

            print(f"Employee search results: {results}")  # Debug print

            # Clear the table before adding new data
            self.userRESULTS.setRowCount(len(results))
            self.userRESULTS.setColumnCount(1)

            row_position = 0

            for result in results:
                # Concatenate all fields of a result into a single string
                result_string = ', '.join(map(str, result))
                item = QtWidgets.QTableWidgetItem(result_string)
                # Make the cell not editable
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.userRESULTS.setItem(row_position, 0, item)
                row_position += 1
                self.userRESULTS.show()
                self.edituserCONTENT.hide()

            cursor.execute(SEARCH_ADMIN, (search_text, search_text, search_text))
            results = cursor.fetchall()

            print(f"Admin search results: {results}")  # Debug print

            self.userRESULTS.setRowCount(self.userRESULTS.rowCount() + len(results))

            for result in results:
                # Concatenate all fields of a result into a single string
                result_string = ', '.join(map(str, result))
                item = QtWidgets.QTableWidgetItem(result_string)
                # Make the cell not editable
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.userRESULTS.setItem(row_position, 0, item)
                row_position += 1
                self.userRESULTS.show()
                self.edituserCONTENT.hide()


            # Connect the cellClicked signal to a slot function
            self.userRESULTS.cellClicked.connect(self.cell_clicked)

        except Exception as e:
            print(f"An error occurred: {e}")

    # Slot function to handle cell click events
    def cell_clicked(self, row, column):
        item = self.userRESULTS.item(row, column)
        print(f"You clicked on cell {row}, {column}. The cell contains: {item.text()}")

        self.userRESULTS.hide()

        # Split the cell data into a list of result data
        result = item.text().split(', ')

        # Show the edituserCONTENT and update the display with the result data
        self.edituserCONTENT.show()
        self.searchFIELD.clear()
        self.nameDISPLAY.setText(f"{result[0]} {result[1]}")
        self.emailDISPLAY.setText(result[2])

        # Check the department of the result and activate the corresponding button
        if result[3] == 'Kitchen':
            self.activate_kitchen()
        elif result[3] == 'Cashier':
            self.activate_cashier()
        elif result[3] == 'Admin':
            self.is_admin()

    def activate_staff(self):
        self.staffBTN.setStyleSheet(self.active_button_style)
        self.adminBTN.setStyleSheet(self.inactive_button_style)

        self.restrictionBUTTONGRP.setEnabled(True)
        self.cashierBTN.setStyleSheet(self.active_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def is_admin(self):
        self.adminBTN.setStyleSheet(self.active_button_style)
        self.staffBTN.setStyleSheet(self.inactive_button_style)

    def activate_admin(self):
        returnValue = confirmation_dialog("Are you sure you want to make this user as an admin?")
        if returnValue == QMessageBox.Ok:
            self.adminBTN.setStyleSheet(self.active_button_style)
            self.staffBTN.setStyleSheet(self.inactive_button_style)

            self.restrictionBUTTONGRP.setEnabled(False)
            self.cashierBTN.setStyleSheet(self.inactive_button_style)
            self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_cashier(self):
        self.cashierBTN.setStyleSheet(self.active_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_kitchen(self):
        self.kitchenBTN.setStyleSheet(self.active_button_style)
        self.cashierBTN.setStyleSheet(self.inactive_button_style)

    def deactivate_user(self):
        returnValue = confirmation_dialog("Are you sure you want to deactivate this user?")
        if returnValue == QMessageBox.Ok:
            email = self.emailDISPLAY.text()
            cursor = conn.cursor()

            try:
                # Deactivate user in the admin table
                cursor.execute(DISABLE_ADMIN, (email,))
                # Commit the changes
                conn.commit()
                print(f"{email} deactivated in admin table")
            except Exception as e:
                print(f"Error deactivating user in admin table: {e}")

            try:
                # Deactivate user in the employee table
                cursor.execute(DISABLE_EMPLOYEE, (email,))
                # Commit the changes
                conn.commit()
                print(f"{email} deactivated in employee table")
            except Exception as e:
                print(f"Error deactivating user in employee table: {e}")

            # Hide content and clear search field
            self.rightcontent.hide()
            self.edituserCONTENT.hide()
            self.searchFIELD.clear()
            print(f"{email} deactivated")

            create_dialog_box(f"User {email} has been successfully deactivated.", "User Deactivated")

    def show_rightcontent(self):
        self.rightcontent.show()

    def discard(self):
        self.rightcontent.hide()
        self.edituserCONTENT.hide()
        self.searchFIELD.clear()