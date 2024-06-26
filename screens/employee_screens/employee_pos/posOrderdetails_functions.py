from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from screens.employee_screens.employee_pos.posOrderdetails import Ui_MainWindow
from shared.navigation_signal import auth_back, pos_back
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.receipt.receipt_dialog import ReceiptDialog
from PyQt5.QtCore import QTime

from validator.user_manager import userManager


class posOrderdetails(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    transaction_generated_signal = QtCore.pyqtSignal()
    update_combobox_signal = QtCore.pyqtSignal()
    history_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.checkoutBTN.clicked.connect(self.goCheckout)
        self.modifyBTN.clicked.connect(self.goModify)
        self.menuBTN.clicked.connect(self.goMenu)
        self.historyBTN.clicked.connect(self.goHistory)
        self.pushButton_6.clicked.connect(self.saveOrder)
        self.pushButton.clicked.connect(self.cancel_order)
        self.pushButton_2.clicked.connect(self.start_timer)
        self.pushButton_3.clicked.connect(self.print_receipt)
        self.pushButton_7.clicked.connect(self.discard)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.updateDateTimeAndTable)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Populate comboBox_2 with package names
        self.populate_comboBox_2()

        # Populate comboBox_2 with soup names
        self.populate_comboBox_3()

        # Populate comboBox_4 with order types
        self.populate_comboBox_4()

        # Populate comboBox_5 with priority
        self.populate_comboBox_5()

        # Populate order id for cancel
        self.populate_comboBox_7()

        # Populate order id for timer
        self.populate_comboBox_8()

        # Populate order id for receipt
        self.populate_comboBox_9()

        # Populate order id for guide
        self.populate_table()

        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)

    def updateDateTimeAndTable(self):
        self.updateDateTime()
        self.populate_table()

    def discard(self):
        self.lineEdit_9.clear()
        self.lineEdit_7.clear()
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    SELECT 
                        Order_ID,
                        Customer_Name,
                        Order_Type,
                        Guest_Pax,
                        Payment_Status,
                        Priority_Order
                    FROM `order`
                    WHERE Payment_Status = 'Waiting for Receipt' or Payment_Status = 'Waiting for Timer'
                    OR (Order_Type = 'Add-ons only' AND Payment_Status = 'Pending')
                    ORDER BY Priority_Order DESC, Order_ID ASC
                """
                cursor.execute(query)
                records = cursor.fetchall()
                self.display_records(records)

                self.tableWidget.setColumnWidth(3, 60)

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()

    def display_records(self, records):
        column_names = [
            "Order ID",
            "Customer Name",
            "Order Type",
            "Guest Pax",
            "Payment Status",
            "Priority Order"
        ]

        if records:
            self.tableWidget.setRowCount(len(records))
            self.tableWidget.setColumnCount(len(column_names))

            for j, name in enumerate(column_names):
                item = QTableWidgetItem(name)
                self.tableWidget.setHorizontalHeaderItem(j, item)

            for i, row in enumerate(records):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))  # Always convert to string
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cell non-clickable
                    self.tableWidget.setItem(i, j, item)

                    # Apply conditional formatting for the "Priority Order" column
                    if column_names[j] == "Priority Order" and col == "Priority":
                        item.setBackground(QtGui.QColor(255, 215, 0))  # Gold color for priority

        else:
            print("No records found.")

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.date.setText(formattedDateTime)

    def goHistory(self):
        self.history_signal.emit()

    def goBack(self):
        self.back_signal.emit()

    def goCheckout(self):
        self.checkout_signal.emit()

    def goModify(self):
        self.modify_signal.emit()

    def goMenu(self):
        self.menu_signal.emit()

    def populate_comboBox_2(self):
        try:
            # Clear existing items
            self.comboBox_2.clear()

            # Add blank/null option
            self.comboBox_2.addItem("")  # Add a blank item

            # Add specific values
            self.comboBox_2.addItems(["Hotpot", "Grill", "Hotpot and Grill"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_2: {e}")

    def populate_comboBox_3(self):
        try:
            # Clear existing items
            self.comboBox_3.clear()

            # Add blank/null option
            self.comboBox_3.addItem("")  # Add a blank item

            # Add specific values
            self.comboBox_3.addItems(["Mala soup", "Plain soup", "Suan la soup", "Tomato soup"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_3: {e}")

    def populate_comboBox_4(self):
        try:
            # Clear existing items
            self.comboBox_4.clear()

            # Add specific values
            self.comboBox_4.addItems(["Package", "Add-ons only"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_4: {e}")

    def populate_comboBox_5(self):
        items = ['Non-priority', 'Priority']
        self.comboBox_5.addItems(items)

    def populate_comboBox_7(self):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Order_ID FROM `order` 
                WHERE Payment_Status = 'Waiting for Receipt' or (Order_Type = 'Add-ons only' AND Payment_Status = 'Pending') 
                ORDER BY Priority_Order DESC, Order_ID ASC
            """)
            order_ids = cursor.fetchall()

            self.comboBox_7.clear()
            for order_id in order_ids:
                self.comboBox_7.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating comboBox_7: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_comboBox_8(self):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Order_ID FROM `order` 
                WHERE Payment_Status = 'Waiting for Timer' 
                ORDER BY Priority_Order DESC, Order_ID ASC
            """)
            order_ids = cursor.fetchall()

            self.comboBox_8.clear()
            for order_id in order_ids:
                self.comboBox_8.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating comboBox_8: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_comboBox_9(self):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Order_ID FROM `order` 
                WHERE Payment_Status = 'Waiting for Receipt'
                ORDER BY Priority_Order DESC, Order_ID ASC
            """)
            order_ids = cursor.fetchall()

            self.comboBox_9.clear()
            for order_id in order_ids:
                self.comboBox_9.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating comboBox_9: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def saveOrder(self):
        # Get input values
        customer_name = self.lineEdit_9.text().strip()
        order_type = self.comboBox_4.currentText()
        priority_order = self.comboBox_5.currentText()
        package_name = self.comboBox_2.currentText()
        guest_capacity = self.lineEdit_7.text().strip()
        soup_variation = self.comboBox_3.currentText()

        if order_type == "Package":
            payment_status = "Waiting for Receipt"

            if not self.validate_package_inputs(customer_name, package_name, guest_capacity, soup_variation):
                return

        elif order_type == "Add-ons only":
            payment_status = "Pending"
            guest_capacity = None

            if not self.validate_addon_inputs(customer_name, package_name, guest_capacity, soup_variation):
                return

        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Get current date in yyyy-MM-dd format
                current_date = QDateTime.currentDateTime().toString("yyyy-MM-dd")

                # Fetch the latest Order_ID for the current date
                cursor.execute(f"SELECT MAX(Order_ID) FROM `order` WHERE Date = '{current_date}'")
                latest_order_id = cursor.fetchone()[0]

                if latest_order_id:
                    # Extract numeric part and increment
                    numeric_part = latest_order_id[11:]  # Assuming Order_ID format is POSyyyyMMddNNN
                    order_number = int(numeric_part)
                    new_order_number = order_number + 1
                    next_order_number = f"{new_order_number:03d}"
                else:
                    # If no previous orders for the day, start from 001
                    next_order_number = "001"

                # Construct new Order_ID
                new_order_id = f"POS{current_date.replace('-', '')}{next_order_number}"



                # Construct the insert query with proper handling of NULL for Guest_Pax
                insert_query = f"""
                                INSERT INTO `order` (Order_ID, Date, Time, Package_ID, Payment_Status, 
                                                     Guest_Pax, Customer_Name, Soup_Variation, Order_Type, Payment_Method, Priority_Order)
                                VALUES (%s, %s, TIME_FORMAT(NOW(), '%H:%i'), 
                                        (SELECT Package_ID FROM package WHERE Package_Name = %s), 
                                        %s, %s, %s, %s, %s, %s, %s)
                            """
                cursor.execute(insert_query, (
                    new_order_id, current_date, package_name, payment_status, guest_capacity, customer_name,
                    soup_variation, order_type, 'Pending', priority_order))
                conn.commit()

                QMessageBox.information(self, "Success", "Order saved successfully.")

                self.update_combobox_signal.emit()
                self.populate_comboBox_7()
                self.populate_comboBox_9()
                self.populate_comboBox_8()

                # Clear input fields after successful save
                self.lineEdit_9.clear()
                self.lineEdit_7.clear()
                self.comboBox_2.setCurrentIndex(-1)
                self.comboBox_3.setCurrentIndex(-1)

                self.populate_table()
                self.reset_styles()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while saving order: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def reset_styles(self):
        self.lineEdit_9.setStyleSheet("")
        self.comboBox_2.setStyleSheet("")
        self.lineEdit_7.setStyleSheet("")
        self.comboBox_5.setStyleSheet("")
        self.comboBox_3.setStyleSheet("")

    def validate_package_inputs(self, customer_name, package_name, guest_capacity, soup_variation):
        valid = True

        if not customer_name:
            self.lineEdit_9.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_9.setStyleSheet("border: 1px solid green;")

        if not package_name:
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if not guest_capacity:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if package_name == "Grill" and soup_variation != "":
            self.comboBox_3.setStyleSheet("border: 1px solid red;")
            valid = False
        elif package_name != "Grill" and not soup_variation:
            self.comboBox_3.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_3.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly for Package type order.")

        return valid

    def validate_addon_inputs(self, customer_name, package_name, guest_capacity, soup_variation):
        valid = True

        if not customer_name:
            self.lineEdit_9.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_9.setStyleSheet("border: 1px solid green;")

        if package_name != "":
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if guest_capacity:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if soup_variation != "":
            self.comboBox_3.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_3.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Provide customer name and empty the other fields for Add-ons only order.")

        return valid

    def print_receipt(self):
        order_id = self.comboBox_9.currentText()

        try:
            cursor = conn.cursor()


            # Fetch order details based on order_id
            cursor.execute("""
                                        UPDATE `order`
                                        SET Payment_Status = 'Waiting for Timer'
                                        WHERE Order_ID = %s
                                    """, (order_id,))
            conn.commit()

            self.populate_table()
            self.populate_comboBox_8()
            self.populate_comboBox_7()
            self.populate_comboBox_9()

            cursor.execute("""
                SELECT Date, Customer_Name, Package_ID, Guest_Pax, Order_Type, 
                       Soup_Variation, Priority_Order
                FROM `order`
                WHERE Order_ID = %s
            """, (order_id,))
            order_details = cursor.fetchone()

            if order_details:
                # Unpack fetched values
                current_date = order_details[0]
                customer_name = order_details[1]
                package_id = order_details[2]
                guest_capacity = order_details[3]
                order_type = order_details[4]
                soup_variation = order_details[5]
                priority_order = order_details[6]

                # Get current time in HH:mm:ss format
                current_time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)

                # Get package name from package table
                package_name = self.get_package_name(cursor, package_id)

                # Construct the order details string including time
                order_details_text = f"""
                Moon Hey Hotpot and Grill

                Order ID: {order_id}
                Date: {current_date}
                Time: {current_time}
                Customer Name: {customer_name}

                -- Order Details --
                Package Name: {package_name if package_name else "N/A"}
                Guest Capacity: {guest_capacity if guest_capacity else "N/A"}
                Order Type: {order_type}
                Soup Variation: {soup_variation if soup_variation else "N/A"}
                Priority Order: {priority_order}


                -- Kitchen Note --
                [Leave space for kitchen staff to add any necessary notes or special instructions.]









                """

                # Create and show the receipt dialog
                receipt_dialog = ReceiptDialog(order_details_text)
                receipt_dialog.exec_()

            else:
                QMessageBox.warning(self, "Error", f"No order found for Order ID: {order_id}")

            # Update the payment status to 'Waiting for Timer'
            cursor.execute("""
                UPDATE `order`
                SET Payment_Status = 'Waiting for Timer'
                WHERE Order_ID = %s
            """, (order_id,))
            conn.commit()


        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while fetching order details: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def get_package_name(self, cursor, package_id):
        try:
            cursor.execute("SELECT Package_Name FROM package WHERE Package_ID = %s", (package_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "N/A"
        except Exception as e:
            print(f"Error occurred while fetching package name: {e}")
            return "N/A"

    def cancel_order(self):
        order_id = self.comboBox_7.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        # Confirm cancellation with the user
        reply = QMessageBox.question(self, 'Confirm Cancel', f"Are you sure you want to cancel order ID {order_id}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE `order` SET Payment_Status = 'Cancelled' WHERE Order_ID = %s", (order_id,))
                conn.commit()

                QMessageBox.information(self, "Order Cancelled", "The order has been successfully cancelled.")
                self.populate_comboBox_7()  # Refresh the combo box
                self.populate_comboBox_8()
                self.populate_comboBox_9()
                self.populate_table()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Error occurred while cancelling the order: {e}")

            finally:
                if conn.is_connected():
                    cursor.close()
        else:
            QMessageBox.information(self, "Cancelled", "Cancellation operation cancelled by user.")

    def start_timer(self):
        order_id = self.comboBox_8.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        reply = QMessageBox.question(self, 'Confirm Timer', f"Are you sure you want to start the timer of {order_id}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE `order` SET Payment_Status = 'Pending' WHERE Order_ID = %s", (order_id,))
                conn.commit()

                QMessageBox.information(self, "Timer Started", "The order has been successfully started with the timer.")
                self.populate_comboBox_7()
                self.populate_comboBox_8()
                self.populate_comboBox_9()


                self.transaction_generated_signal.emit()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Error occurred: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
        else:
            QMessageBox.information(self, "Cancelled", "Timer operation cancelled by user.")



