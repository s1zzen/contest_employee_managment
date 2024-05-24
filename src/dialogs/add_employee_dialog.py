from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QDialog, QComboBox, QMessageBox
from PyQt5.QtSql import QSqlQuery


class AddEmployeeDialog(QDialog):
    def __init__(self, model):
        super().__init__()

        self.model = model

        self.setWindowTitle('Добавить сотрудника')

        self.nameInput = QLineEdit()
        self.positionInput = QLineEdit()
        self.branchInput = QComboBox()

        query = QSqlQuery()
        query.exec_("SELECT branch_id, name FROM Branches")
        while query.next():
            branch_id = query.value(0)
            name = query.value(1)
            self.branchInput.addItem(name, branch_id)

        formLayout = QFormLayout()
        formLayout.addRow('Имя:', self.nameInput)
        formLayout.addRow('Должность:', self.positionInput)
        formLayout.addRow('Филиал:', self.branchInput)

        self.submitButton = QPushButton('Сохранить')
        self.submitButton.clicked.connect(self.add_employee)

        layout = QVBoxLayout()
        layout.addLayout(formLayout)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def add_employee(self):
        name = self.nameInput.text()
        position = self.positionInput.text()
        branch_id = self.branchInput.currentData()

        if name and position:
            query = QSqlQuery()
            query.prepare('INSERT INTO Employees (name, position, branch_id) VALUES (?, ?, ?)')
            query.addBindValue(name)
            query.addBindValue(position)
            query.addBindValue(branch_id)
            if query.exec_():
                self.model.select()
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Не удалось добавить сотрудника в базу данных.')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, заполните все поля.')
