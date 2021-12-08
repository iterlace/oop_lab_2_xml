import webbrowser
from typing import Optional

from PyQt6.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from exporter import TableExporter
from strategies import BaseStrategy, BS4Strategy, DOMStrategy, SAXStrategy

from .filters import Filters
from .mainwindow_ui import Ui_MainWindow
from .table import TableWrapper


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget = TableWrapper(self.ui.tableWidget)
        self.filters = Filters(self.ui)

        self.ui.action_open.triggered.connect(self.on_open)
        self.ui.action_help.triggered.connect(self.on_help)
        self.ui.action_about.triggered.connect(self.on_about)
        self.ui.button_search.clicked.connect(self.on_search)
        self.ui.button_convert.clicked.connect(self.on_convert)
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

    def on_convert(self):
        if not self.filepath:
            return

        filepath, _ = QFileDialog().getSaveFileName(
            parent=self,
            caption="Select an export path",
            filter="HTML (*.html)",
        )
        if not filepath:
            return
        TableExporter.export(self.ui.tableWidget.scientists, filepath)

        webbrowser.open(f"file://{filepath}", new=2)
        QMessageBox.information(
            self,
            "Exported",
            f"The table was successfully exported!\n",
        )

    def on_about(self):
        QMessageBox.information(
            self,
            "About",
            f"Version: undefined\n"
            f"Developed by: Evgeniy Goncharenko\n"
            f"Source code: https://github.com/iterlace/oop_lab_2_xml",
        )

    def on_help(self):
        QMessageBox.information(
            self,
            "Help",
            f"1. First, open an .xml file with a valid schema\n"
            f'2. You can apply filters by each field and click "Select" to apply them\n'
            f"3. To convert selected table to the .HTML format, click the corresponding button.\n",
        )
