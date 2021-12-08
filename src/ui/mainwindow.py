import sys
import functools
from typing import Optional, Any, Tuple, List, Dict, Type

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox, QHeaderView
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem

from models import Scientist, ScientistQuery
from common import str2date
from strategies import BaseStrategy, DOMStrategy, BS4Strategy, SAXStrategy

from .mainwindow_ui import Ui_MainWindow
from .table import TableWrapper
from .filters import Filters


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget = TableWrapper(self.ui.tableWidget)
        self.filters = Filters(self.ui)

        self.ui.action_open.triggered.connect(self.on_open)
        self.ui.button_search.clicked.connect(self.on_search)
        self.ui.button_clean.clicked.connect(self.on_clean)

        self.filepath: Optional[str] = None
        self._strategy = None

    @property
    def strategy(self) -> BaseStrategy:
        if self.ui.radio_strategy_bs4.isChecked():
            cls = BS4Strategy
        elif self.ui.radio_strategy_dom.isChecked():
            cls = DOMStrategy
        elif self.ui.radio_strategy_sax.isChecked():
            cls = SAXStrategy

        if not self._strategy or self._strategy.__class__ is not cls:
            self._strategy = cls()
        return self._strategy

    def on_open(self):
        filepath, _ = QFileDialog().getOpenFileName(
            parent=self,
            caption="Select an .xml file",
            filter="XML (*.xml)",
        )
        if not filepath:
            return
        self.filepath = filepath
        scientists = self.strategy.all(self.filepath)
        self.ui.tableWidget.fill_scientists(scientists)
        self.filters.fill(scientists)

    def on_search(self):
        if not self.filepath:
            return
        query = self.filters.get_query()
        scientists = self.strategy.find(self.filepath, query)
        self.ui.tableWidget.fill_scientists(scientists)

    def on_clean(self):
        if not self.filepath:
            return
        self.filters.deselect()
        scientists = self.strategy.all(self.filepath)
        self.ui.tableWidget.fill_scientists(scientists)
