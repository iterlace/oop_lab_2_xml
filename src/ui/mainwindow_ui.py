# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(700, 0))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 1, 1, 1)
        self.group_box_controls = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.group_box_controls.sizePolicy().hasHeightForWidth()
        )
        self.group_box_controls.setSizePolicy(sizePolicy)
        self.group_box_controls.setAutoFillBackground(False)
        self.group_box_controls.setTitle("")
        self.group_box_controls.setFlat(False)
        self.group_box_controls.setObjectName("group_box_controls")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.group_box_controls)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.group_box_filters = QtWidgets.QGroupBox(self.group_box_controls)
        self.group_box_filters.setTitle("")
        self.group_box_filters.setObjectName("group_box_filters")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.group_box_filters)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.horizontalLayout_Name = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Name.setSpacing(6)
        self.horizontalLayout_Name.setObjectName("horizontalLayout_Name")
        self.label_entry_name = QtWidgets.QLabel(self.group_box_filters)
        self.label_entry_name.setObjectName("label_entry_name")
        self.horizontalLayout_Name.addWidget(self.label_entry_name)
        self.combo_box_entry_name = QtWidgets.QComboBox(self.group_box_filters)
        self.combo_box_entry_name.setObjectName("combo_box_entry_name")
        self.horizontalLayout_Name.addWidget(self.combo_box_entry_name)
        self.vertical_layout.addLayout(self.horizontalLayout_Name)
        self.horizontalLayout_Faculty = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Faculty.setObjectName("horizontalLayout_Faculty")
        self.label_entry_faculty = QtWidgets.QLabel(self.group_box_filters)
        self.label_entry_faculty.setObjectName("label_entry_faculty")
        self.horizontalLayout_Faculty.addWidget(self.label_entry_faculty)
        self.combo_box_entry_faculty = QtWidgets.QComboBox(self.group_box_filters)
        self.combo_box_entry_faculty.setObjectName("combo_box_entry_faculty")
        self.horizontalLayout_Faculty.addWidget(self.combo_box_entry_faculty)
        self.vertical_layout.addLayout(self.horizontalLayout_Faculty)
        self.horizontalLayout_Cathedra = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Cathedra.setObjectName("horizontalLayout_Cathedra")
        self.label_entry_cathedra = QtWidgets.QLabel(self.group_box_filters)
        self.label_entry_cathedra.setObjectName("label_entry_cathedra")
        self.horizontalLayout_Cathedra.addWidget(self.label_entry_cathedra)
        self.combo_box_entry_cathedra = QtWidgets.QComboBox(self.group_box_filters)
        self.combo_box_entry_cathedra.setObjectName("combo_box_entry_cathedra")
        self.horizontalLayout_Cathedra.addWidget(self.combo_box_entry_cathedra)
        self.vertical_layout.addLayout(self.horizontalLayout_Cathedra)
        self.horizontalLayout_Laboratory = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Laboratory.setObjectName("horizontalLayout_Laboratory")
        self.label_entry_laboratory = QtWidgets.QLabel(self.group_box_filters)
        self.label_entry_laboratory.setObjectName("label_entry_laboratory")
        self.horizontalLayout_Laboratory.addWidget(self.label_entry_laboratory)
        self.combo_box_entry_laboratory = QtWidgets.QComboBox(self.group_box_filters)
        self.combo_box_entry_laboratory.setObjectName("combo_box_entry_laboratory")
        self.horizontalLayout_Laboratory.addWidget(self.combo_box_entry_laboratory)
        self.vertical_layout.addLayout(self.horizontalLayout_Laboratory)
        self.horizontalLayout_Post = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Post.setObjectName("horizontalLayout_Post")
        self.label_entry_post = QtWidgets.QLabel(self.group_box_filters)
        self.label_entry_post.setObjectName("label_entry_post")
        self.horizontalLayout_Post.addWidget(self.label_entry_post)
        self.combo_box_entry_post = QtWidgets.QComboBox(self.group_box_filters)
        self.combo_box_entry_post.setObjectName("combo_box_entry_post")
        self.horizontalLayout_Post.addWidget(self.combo_box_entry_post)
        self.vertical_layout.addLayout(self.horizontalLayout_Post)
        self.gridLayout_3.addLayout(self.vertical_layout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.group_box_filters, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_5.addItem(spacerItem, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.group_box_controls)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 4, 0, 1, 1)
        self.group_box_buttons = QtWidgets.QGroupBox(self.group_box_controls)
        self.group_box_buttons.setTitle("")
        self.group_box_buttons.setObjectName("group_box_buttons")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.group_box_buttons)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_search = QtWidgets.QPushButton(self.group_box_buttons)
        self.button_search.setMinimumSize(QtCore.QSize(0, 50))
        self.button_search.setObjectName("button_search")
        self.verticalLayout.addWidget(self.button_search)
        self.button_convert = QtWidgets.QPushButton(self.group_box_buttons)
        self.button_convert.setMinimumSize(QtCore.QSize(0, 50))
        self.button_convert.setObjectName("button_convert")
        self.verticalLayout.addWidget(self.button_convert)
        self.button_clean = QtWidgets.QPushButton(self.group_box_buttons)
        self.button_clean.setMinimumSize(QtCore.QSize(0, 50))
        self.button_clean.setObjectName("button_clean")
        self.verticalLayout.addWidget(self.button_clean)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.group_box_buttons, 5, 0, 1, 1)
        self.group_box_strategy = QtWidgets.QGroupBox(self.group_box_controls)
        self.group_box_strategy.setEnabled(True)
        self.group_box_strategy.setMaximumSize(QtCore.QSize(16777215, 50))
        self.group_box_strategy.setTitle("")
        self.group_box_strategy.setObjectName("group_box_strategy")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.group_box_strategy)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.radio_strategy_dom = QtWidgets.QRadioButton(self.group_box_strategy)
        self.radio_strategy_dom.setChecked(True)
        self.radio_strategy_dom.setObjectName("radio_strategy_dom")
        self.horizontal_layout.addWidget(self.radio_strategy_dom)
        self.radio_strategy_sax = QtWidgets.QRadioButton(self.group_box_strategy)
        self.radio_strategy_sax.setObjectName("radio_strategy_sax")
        self.horizontal_layout.addWidget(self.radio_strategy_sax)
        self.radio_strategy_bs4 = QtWidgets.QRadioButton(self.group_box_strategy)
        self.radio_strategy_bs4.setObjectName("radio_strategy_bs4")
        self.horizontal_layout.addWidget(self.radio_strategy_bs4)
        self.gridLayout_4.addLayout(self.horizontal_layout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.group_box_strategy, 3, 0, 1, 1)
        self.gridLayout_6.addWidget(self.group_box_controls, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_help = QtGui.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_file.addAction(self.action_open)
        self.menu_help.addAction(self.action_help)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_entry_name.setText(_translate("MainWindow", "Name"))
        self.label_entry_faculty.setText(_translate("MainWindow", "Faculty"))
        self.label_entry_cathedra.setText(_translate("MainWindow", "Cathedra"))
        self.label_entry_laboratory.setText(_translate("MainWindow", "Laboratory"))
        self.label_entry_post.setText(_translate("MainWindow", "Post"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        self.button_convert.setText(_translate("MainWindow", "Convert to HTML"))
        self.button_clean.setText(_translate("MainWindow", "Clean"))
        self.radio_strategy_dom.setText(_translate("MainWindow", "DOM"))
        self.radio_strategy_sax.setText(_translate("MainWindow", "SAX"))
        self.radio_strategy_bs4.setText(_translate("MainWindow", "BS4"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_help.setText(_translate("MainWindow", "Help"))
        self.action_about.setText(_translate("MainWindow", "About"))
