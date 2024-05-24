from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTableView, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from src.dialogs.add_employee_dialog import AddEmployeeDialog
from src.dialogs.edit_employee_dialog import EditEmployeeDialog
from src.config import Configuration


class EmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Список сотрудников')
        self.setGeometry(100, 100, 600, 400)

        self.cfg = Configuration()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.cfg.db_path)
        self.db.open()

        self.model = QSqlTableModel(self)
        self.model.setTable('Employees')
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)

        self.newButton = QPushButton('Добавить сотрудника')
        self.newButton.clicked.connect(self.add_employee)

        self.editButton = QPushButton('Редактирование сотрудника')
        self.editButton.clicked.connect(self.edit_employee)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.newButton)
        layout.addWidget(self.editButton)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def closeEvent(self, e):
        self.db.close()

    def add_employee(self):
        self.addEmployeeDialog = AddEmployeeDialog(self.model)
        self.addEmployeeDialog.exec_()

    def edit_employee(self):
        selected_indexes = self.view.selectionModel().selectedRows()
        if selected_indexes:
            employee_id = selected_indexes[0].data()
            self.editEmployeeDialog = EditEmployeeDialog(self.model, employee_id)
            self.editEmployeeDialog.exec_()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, выберите сотрудника для редактирования.')
