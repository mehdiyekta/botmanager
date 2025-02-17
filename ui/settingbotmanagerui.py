# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingbotmanagerui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(941, 607)
        MainWindow.setStyleSheet("/* General Styles */\n"
"QWidget {\n"
"    color: #FFFFFF;\n"
"    background-color: #2C2C2C;\n"
"    font-family: \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* QPushButton Styles */\n"
"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41;\n"
"}\n"
"\n"
"/* QLineEdit Styles */\n"
"QLineEdit {\n"
"    background-color: #3C3C3C;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    padding: 8px 12px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4CAF50;\n"
"}\n"
"\n"
"/* QComboBox Styles */\n"
"QComboBox {\n"
"    background-color: #3C3C3C;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    padding: 8px 12px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #454545;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3C3C3C;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #4CAF50;\n"
"}\n"
"\n"
"/* QCheckBox Styles */\n"
"QCheckBox {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    background-color: #3C3C3C;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"/* QProgressBar Styles */\n"
"QProgressBar {\n"
"    background-color: #3C3C3C;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"   background-color: #3C3C3C;;\n"
"}\n"
"QTabWidget::pane {\n"
"border: 2px solid #909090;\n"
"border-radius:2px;\n"
"}\n"
"            QTabBar::tab {\n"
"                background-color: #f1f1f1;\n"
"                color: #333;\n"
"                padding: 10px 20px;\n"
"                font-size: 14px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background-color: #333;\n"
"                color: #fff;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setMinimumSize(QtCore.QSize(111, 0))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 4, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 5, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 1, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_10.addWidget(self.lineEdit_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 7, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 6, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_4.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "تنظیمات"))
        self.groupBox_3.setTitle(_translate("MainWindow", "تنظیمات اتصال"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "بدون پروکسی"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "http"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "https"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "socks4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "socks5"))
        self.label_2.setText(_translate("MainWindow", "پروکسی"))
        self.label_7.setText(_translate("MainWindow", "یوزر سرور FTP"))
        self.label_4.setText(_translate("MainWindow", "چنل آیدی"))
        self.pushButton_5.setText(_translate("MainWindow", "بازنشانی فایل دیتابیس"))
        self.label_9.setText(_translate("MainWindow", "سرور FTP"))
        self.label_3.setText(_translate("MainWindow", "توکن API"))
        self.label_8.setText(_translate("MainWindow", "پسورد سرور FTP"))
        self.groupBox.setTitle(_translate("MainWindow", "ظاهر برنامه"))
        self.comboBox.setItemText(0, _translate("MainWindow", "تاریک"))
        self.comboBox.setItemText(1, _translate("MainWindow", "روشن"))
        self.comboBox.setItemText(2, _translate("MainWindow", "مطابق با سیستم"))
        self.label.setText(_translate("MainWindow", "تم:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "آدرس ها"))
        self.pushButton_4.setText(_translate("MainWindow", "تعیین"))
        self.label_5.setText(_translate("MainWindow", "محل ذخیره محصول"))
        self.pushButton_3.setText(_translate("MainWindow", "تعیین"))
        self.label_6.setText(_translate("MainWindow", "محل دیتابیس items"))
        self.pushButton.setText(_translate("MainWindow", "ذخیره"))
        self.pushButton_2.setText(_translate("MainWindow", "لغو"))
