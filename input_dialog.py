from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QFormLayout, QLabel


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        self.third = QLabel(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Employee's Name", self.first)
        layout.addRow("Employee's ID", self.second)
        layout.addRow('', self.third)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_inputs(self):
        return [self.first.text(), self.second.text()]

    def accept(self):
        if '' in {self.first.text(), self.second.text()}:
            self.print_label('Name/ID cannot be empty')
        else:
            super().accept()

    def print_label(self, msg):
        self.third.setText(msg)
