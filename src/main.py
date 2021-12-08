# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox

from ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        Ui_MainWindow().setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


