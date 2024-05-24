import sys
from PyQt5.QtWidgets import QApplication
from models.db_init import init_db
from src.windows.main_window import MainWindow
if __name__ == '__main__':
    init_db()
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
