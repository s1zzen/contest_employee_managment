import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox
from src.windows.branch_window import BranchWindow
from src.windows.employee_window import EmployeeWindow
from src.utils import export

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Employee Management')
        self.setGeometry(100, 100, 800, 600)

        # Создание кнопок
        self.employeeButton = QPushButton('Сотрудники')
        self.branchButton = QPushButton('Филиалы')
        self.exportButton = QPushButton('Выгрузить данные')

        # Привязка кнопок к функциям
        self.employeeButton.clicked.connect(self.show_employee_list)
        self.branchButton.clicked.connect(self.show_branch_list)
        self.exportButton.clicked.connect(self.export_data)

        # Основной макет
        layout = QVBoxLayout()
        layout.addWidget(self.employeeButton)
        layout.addWidget(self.branchButton)
        layout.addWidget(self.exportButton)

        # Центральный виджет
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def show_employee_list(self):
        self.employeeWindow = EmployeeWindow()
        self.employeeWindow.show()

    def show_branch_list(self):
        self.branchWindow = BranchWindow()
        self.branchWindow.show()

    def export_data(self):
        export.export_data(self)
        QMessageBox.information(self, 'Успех', 'Данные успешно выгружены в файлы employees.xlsx и employees.docx.')

