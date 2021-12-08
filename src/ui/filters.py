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


class Filters:

    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.query_mapping = {
            self.ui.combo_box_entry_name: "full_name",
            self.ui.combo_box_entry_faculty: "faculty",
            self.ui.combo_box_entry_cathedra: "cathedra",
            self.ui.combo_box_entry_laboratory: "laboratory",
            self.ui.combo_box_entry_post: "post",
        }

    def fill(self, scientists: List[Scientist]) -> None:
        for widget, query_field in self.query_mapping.items():
            widget.clear()
            widget.addItem("---", None)
            values = sorted(set(str(getattr(obj, query_field)) for obj in scientists))
            for val in values:
                widget.addItem(val, val)

    def deselect(self):
        for widget, _ in self.query_mapping.items():
            widget.setCurrentIndex(0)

    def get_query(self) -> ScientistQuery:
        fields = {}
        for widget, query_field in self.query_mapping.items():
            data = widget.itemData(widget.currentIndex())
            if not data:
                fields[query_field] = ""
            else:
                fields[query_field] = data

        query = ScientistQuery(**fields)
        return query

