import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
import main_window

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())