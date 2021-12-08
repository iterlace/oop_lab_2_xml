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


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget = TableWrapper(self.ui.tableWidget)

        self.ui.action_open.triggered.connect(self.on_open)

        self.filepath: Optional[str] = None
        self._strategy = None

        self.query_mapping = {
            self.ui.combo_box_entry_name: "full_name",
            self.ui.combo_box_entry_faculty: "faculty",
            self.ui.combo_box_entry_cathedra: "cathedra",
            self.ui.combo_box_entry_laboratory: "laboratory",
            self.ui.combo_box_entry_post: "post",
        }

        self._set_debug_callbacks()

    def _set_debug_callbacks(self):
        actions = [
            i for i in dir(self.ui) if "signal" in type(getattr(self.ui, i)).__name__.lower()
        ]
        for action in actions:

            def l(__action):
                @functools.wraps(l)
                def inner(*args, **kwargs):
                    print(__action, args, kwargs)

                return inner

            getattr(self.ui, action).connect(l(action))

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
        self.fill_filters(scientists)

    def fill_filters(self, scientists: List[Scientist]):
        for widget, query_field in self.query_mapping.items():
            widget.clear()
            widget.addItem("---", None)
            values = sorted(set(str(getattr(obj, query_field)) for obj in scientists))
            for val in values:
                widget.addItem(val, val)
