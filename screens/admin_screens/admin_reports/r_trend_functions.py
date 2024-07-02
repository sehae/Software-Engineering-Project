import os

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QGraphicsPixmapItem

from modules.reports_and_analysis.generate_trends import (
    load_config, save_config, save_trend_report_to_excel,
    save_trend_report_to_word,
)
from screens.admin_screens.admin_reports.report_trend import Ui_MainWindow
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW


class trendReport(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    sales_report_signal = QtCore.pyqtSignal()
    inventory_report_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.back_signal.emit)
        self.salesReportBTN.clicked.connect(self.sales_report_signal.emit)
        self.inventoryReportBTN.clicked.connect(self.inventory_report_signal.emit)
        self.generateBTN.clicked.connect(self.generate_report)
        self.viewBTN.clicked.connect(self.view_report_location)
        self.selectfolderBTN.clicked.connect(self.selectReportDirectory)

        config = load_config()
        self.directory = config.get('DEFAULT', 'trend_path', fallback=None)
        if self.directory:
            self.filelocDISPLAY.setText(self.directory)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        self.UiComponents()

    def UiComponents(self):
        self.frequencyBOX.setStyleSheet(COMBOBOX_STYLE)
        self.frequencyBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")
        self.sysTimeDate.setText(formattedDateTime)

    def selectReportDirectory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')

        if directory:
            save_config(directory)
            self.directory = directory
            self.filelocDISPLAY.setText(directory)

    def view_report_location(self):
        try:
            config = load_config()
            trend_path = config.get('DEFAULT', 'trend_path', fallback=None)
            if trend_path:
                print(f"The report location is: {trend_path}")
                os.startfile(trend_path)  # Open the report directory in the file explorer
            else:
                print("No report location has been set.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def generate_report(self):
        if not self.directory:
            # If no directory is selected, show a warning message or handle the case accordingly
            print("Please select a directory to save the reports.")
            return

        frequency = self.frequencyBOX.currentText()
        success = False
        if frequency == "Daily":
            save_trend_report_to_word(frequency, self.directory)
            success = True
        elif frequency == "Weekly":
            save_trend_report_to_word(frequency, self.directory)
            success = True
        elif frequency == "Monthly":
            save_trend_report_to_word(frequency, self.directory)
            success = True

        if success:
            QMessageBox.information(self, "Success", f"{frequency.capitalize()} report has been generated and saved to '{self.directory}'")

        self.displayReport(frequency)

    def displayReport(self, frequency):
        viewer1scene = QGraphicsScene()
        viewer2scene = QGraphicsScene()
        # viewer3scene = QGraphicsScene()

        viewer1Pixmap = QPixmap(f'{self.directory}/product_performance_{frequency.lower()}.png')
        viewer2Pixmap = QPixmap(f'{self.directory}/sales_trend_{frequency.lower()}.png')
        # viewer3Pixmap = QPixmap(f'{self.directory}/sales_category_{frequency.lower()}.png')

        viewer1scene.addItem(QGraphicsPixmapItem(viewer1Pixmap))
        viewer2scene.addItem(QGraphicsPixmapItem(viewer2Pixmap))
        # viewer3scene.addItem(QGraphicsPixmapItem(viewer3Pixmap))

        self.viewer1.setScene(viewer1scene)
        self.viewer2.setScene(viewer2scene)
        # self.viewer3.setScene(viewer3scene)
