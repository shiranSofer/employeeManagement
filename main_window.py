import json

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from employee import Employee
from input_dialog import InputDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('management.ui', self)
        self.setWindowTitle('ניהול עובדים')
        self.load()
        self.add_button.clicked.connect(self.on_add_button_clicked)

    @pyqtSlot()
    def on_add_button_clicked(self):
        row = self.list_container.currentRow()
        dialog = InputDialog()
        if dialog.exec():
            employee = Employee(dialog.get_inputs()[1], dialog.get_inputs()[0])
            if not employee.if_exist():
                self.list_container.insertItem(row, str(employee))
                employee.save_employee()
            else:
                dialog.print_label("employee exist")

    def load(self):
        self.list_container.clear()
        with open("employee.json", "r") as f:
            data = json.load(f)
        items = data['employee_details']
        for item in items:
            self.list_container.addItem(item['employee_name'] + ' ' + item['employee_id'])
