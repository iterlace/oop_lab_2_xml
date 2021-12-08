import sys
import functools
from typing import Union
from typing import Optional, Any, Tuple, List, Dict, Type

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QTableWidget, QApplication, QMainWindow, QMenu, QMessageBox, QHeaderView
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem

from models import Scientist, ScientistQuery
from common import str2date
from strategies import BaseStrategy, DOMStrategy, BS4Strategy, SAXStrategy


class TableWrapper:
    columns = ["Name", "Faculty", "Cathedra", "Laboratory", "Post"]

    def __init__(self, wrapped: Union[QTableWidget, Type[QTableWidget]]):
        if isinstance(wrapped, QTableWidget):
            self.wrapped_class = wrapped
        elif isinstance(wrapped, type):
            self.wrapped_class = wrapped()
        else:
            raise ValueError("Only QTableWidget class/object allowed!")

        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def __getattr__(self, attr):
        orig_attr = self.wrapped_class.__getattribute__(attr)
        if callable(orig_attr):
            def hooked(*args, **kwargs):
                result = orig_attr(*args, **kwargs)
                if result == self.wrapped_class:
                    return self
                return result
            return hooked
        else:
            return orig_attr

    def fill_scientists(self, scientists: List[Scientist]):
        self.setRowCount(0)
        self.setRowCount(len(scientists))
        for row, scientist in enumerate(scientists):
            self.setItem(row, 0, self._build_item(scientist.full_name))
            self.setItem(row, 1, self._build_item(scientist.faculty))
            self.setItem(row, 2, self._build_item(scientist.cathedra))
            self.setItem(row, 3, self._build_item(str(scientist.laboratory)))

            if scientist.post_end:
                post = "{} ({} - {})".format(
                    scientist.post,
                    scientist.post_start.strftime("%d.%m.%Y"),
                    scientist.post_end.strftime("%d.%m.%Y"),
                )
            else:
                post = "{} ({})".format(scientist.post, scientist.post_start.strftime("%d.%m.%Y"))
            self.setItem(row, 4, self._build_item(post))
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

    def _build_item(self, text: str):
        item = QTableWidgetItem()
        item.setText(text)
        item.setToolTip(text)
        return item