from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QDialog, QComboBox, QMessageBox
from PyQt5.QtSql import QSqlQuery


class EditEmployeeDialog(QDialog):
    def __init__(self, model, employee_id):
        super().__init__()

        self.model = model
        self.employee_id = employee_id

        self.setWindowTitle('Редактировать сотрудника')

        self.nameInput = QLineEdit()
        self.positionInput = QLineEdit()
        self.branchInput = QComboBox()

        query = QSqlQuery()
        query.exec_("SELECT branch_id, name FROM Branches")
        while query.next():
            branch_id = query.value(0)
            name = query.value(1)
            self.branchInput.addItem(name, branch_id)

        query = QSqlQuery()
        query.prepare("SELECT name, position, branch_id FROM Employees WHERE employee_id = ?")
        query.addBindValue(employee_id)
        query.exec_()
        if query.next():
            name = query.value(0)
            position = query.value(1)
            branch_id = query.value(2)
            self.nameInput.setText(name)
            self.positionInput.setText(position)
            index = self.branchInput.findData(branch_id)
            if index >= 0:
                self.branchInput.setCurrentIndex(index)

        formLayout = QFormLayout()
        formLayout.addRow('Имя:', self.nameInput)
        formLayout.addRow('Должность:', self.positionInput)
        formLayout.addRow('Филиал:', self.branchInput)

        self.submitButton = QPushButton('Сохранить')
        self.submitButton.clicked.connect(self.edit_employee)

        layout = QVBoxLayout()
        layout.addLayout(formLayout)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def edit_employee(self):
        name = self.nameInput.text()
        position = self.positionInput.text()
        branch_id = self.branchInput.currentData()

        if name and position:
            query = QSqlQuery()
            query.prepare('UPDATE Employees SET name = ?, position = ?, branch_id = ? WHERE employee_id = ?')
            query.addBindValue(name)
            query.addBindValue(position)
            query.addBindValue(branch_id)
            query.addBindValue(self.employee_id)
            if query.exec_():
                self.model.select()
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Не удалось обновить данные сотрудника.')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, заполните все поля.')
