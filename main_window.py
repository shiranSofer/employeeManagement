from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from input_dialog import InputDialog
from employee import Employee


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('management.ui', self)
        self.setWindowTitle('ניהול עובדים')
        self.add_button.clicked.connect(self.on_add_button_clicked)

    @pyqtSlot()
    def on_add_button_clicked(self):
        row = self.list_container.currentRow()
        dialog = InputDialog()
        if dialog.exec():
            employee = Employee(dialog.get_inputs()[0], dialog.get_inputs()[1])
            self.list_container.insertItem(row, str(employee))
            employee.save_employee()
            print(dialog.get_inputs()[0])

