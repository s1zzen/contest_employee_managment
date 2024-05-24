from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QDialog, QComboBox, QMessageBox
from PyQt5.QtSql import QSqlQuery


class EditBranchDialog(QDialog):
    def __init__(self, model, branch_id):
        super().__init__()

        self.model = model
        self.branch_id = branch_id

        self.setWindowTitle('Редактировать филиал')

        self.nameInput = QLineEdit()
        self.directorInput = QComboBox()
        self.directorInput.addItem("Нет директора", None)

        query = QSqlQuery()
        query.exec_("SELECT employee_id, name FROM Employees")
        while query.next():
            employee_id = query.value(0)
            name = query.value(1)
            self.directorInput.addItem(name, employee_id)

        query = QSqlQuery()
        query.prepare("SELECT name, director_id FROM Branches WHERE branch_id = ?")
        query.addBindValue(branch_id)
        query.exec_()
        if query.next():
            name = query.value(0)
            director_id = query.value(1)
            self.nameInput.setText(name)
            if director_id:
                index = self.directorInput.findData(director_id)
                if index >= 0:
                    self.directorInput.setCurrentIndex(index)

        formLayout = QFormLayout()
        formLayout.addRow('Название филиала:', self.nameInput)
        formLayout.addRow('Директор филиала:', self.directorInput)

        self.submitButton = QPushButton('Сохранить')
        self.submitButton.clicked.connect(self.edit_branch)

        layout = QVBoxLayout()
        layout.addLayout(formLayout)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def edit_branch(self):
        name = self.nameInput.text()
        director_id = self.directorInput.currentData()

        if name:
            query = QSqlQuery()
            query.prepare('UPDATE Branches SET name = ?, director_id = ? WHERE branch_id = ?')
            query.addBindValue(name)
            query.addBindValue(director_id)
            query.addBindValue(self.branch_id)
            if query.exec_():
                self.model.select()
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Не удалось обновить данные филиала.')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, заполните все поля.')
