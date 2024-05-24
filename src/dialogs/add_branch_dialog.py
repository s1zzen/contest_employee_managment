from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QDialog, QComboBox, QMessageBox
from PyQt5.QtSql import QSqlQuery


class AddBranchDialog(QDialog):
    def __init__(self, model):
        super().__init__()

        self.model = model

        self.setWindowTitle('Добавить филиал')

        self.nameInput = QLineEdit()
        self.directorInput = QComboBox()
        self.directorInput.addItem("Нет директора", None)

        query = QSqlQuery()
        query.exec_("SELECT employee_id, name FROM Employees")
        while query.next():
            employee_id = query.value(0)
            name = query.value(1)
            self.directorInput.addItem(name, employee_id)

        formLayout = QFormLayout()
        formLayout.addRow('Название филиала:', self.nameInput)
        formLayout.addRow('Директор филиала:', self.directorInput)

        self.submitButton = QPushButton('Сохранить')
        self.submitButton.clicked.connect(self.add_branch)

        layout = QVBoxLayout()
        layout.addLayout(formLayout)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def add_branch(self):
        name = self.nameInput.text()
        director_id = self.directorInput.currentData()

        if name:
            query = QSqlQuery()
            query.prepare('INSERT INTO Branches (name, director_id) VALUES (?, ?)')
            query.addBindValue(name)
            query.addBindValue(director_id)
            if query.exec_():
                self.model.select()
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Не удалось добавить филиал в базу данных.')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, заполните все поля.')
