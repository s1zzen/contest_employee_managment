from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTableView, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from src.dialogs.add_branch_dialog import AddBranchDialog
from src.dialogs.edit_branch_dialog import EditBranchDialog
from src.config import Configuration


class BranchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Список филиалов')
        self.setGeometry(100, 100, 600, 400)

        self.cfg = Configuration()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.cfg.db_path)
        self.db.open()

        self.model = QSqlTableModel(self)
        self.model.setTable('Branches')
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionBehavior(QTableView.SelectRows)

        self.newButton = QPushButton('Добавить филиал')
        self.newButton.clicked.connect(self.add_branch)

        self.editButton = QPushButton('Редактировать филиал')
        self.editButton.clicked.connect(self.edit_branch)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.newButton)
        layout.addWidget(self.editButton)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def closeEvent(self, e):
        self.db.close()

    def add_branch(self):
        self.addBranchDialog = AddBranchDialog(self.model)
        self.addBranchDialog.exec_()

    def edit_branch(self):
        selected_indexes = self.view.selectionModel().selectedRows()
        if selected_indexes:
            branch_id = selected_indexes[0].data()
            self.editBranchDialog = EditBranchDialog(self.model, branch_id)
            self.editBranchDialog.exec_()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, выберите филиал для редактирования.')
