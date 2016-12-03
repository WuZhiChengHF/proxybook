# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proxybook.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ProxyBook(object):
    def setupUi(self, ProxyBook):
        ProxyBook.setObjectName(_fromUtf8("ProxyBook"))
        ProxyBook.resize(700, 450)
        font = QtGui.QFont()
        font.setPointSize(12)
        ProxyBook.setFont(font)
        self.centralwidget = QtGui.QWidget(ProxyBook)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 271, 91))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_name = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.horizontalLayout.addWidget(self.label_name)
        self.edit_name = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit_name.setFont(font)
        self.edit_name.setText(_fromUtf8(""))
        self.edit_name.setObjectName(_fromUtf8("edit_name"))
        self.horizontalLayout.addWidget(self.edit_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_id = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_id.setFont(font)
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.horizontalLayout_2.addWidget(self.label_id)
        self.edit_id = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit_id.setFont(font)
        self.edit_id.setText(_fromUtf8(""))
        self.edit_id.setObjectName(_fromUtf8("edit_id"))
        self.horizontalLayout_2.addWidget(self.edit_id)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.view_id = QtGui.QGraphicsView(self.centralwidget)
        self.view_id.setGeometry(QtCore.QRect(40, 180, 300, 200))
        self.view_id.setObjectName(_fromUtf8("view_id"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(410, 50, 248, 169))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.bt_print = QtGui.QPushButton(self.centralwidget)
        self.bt_print.setGeometry(QtCore.QRect(520, 260, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_print.setFont(font)
        self.bt_print.setObjectName(_fromUtf8("bt_print"))
        self.bt_add = QtGui.QPushButton(self.centralwidget)
        self.bt_add.setGeometry(QtCore.QRect(430, 260, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_add.setFont(font)
        self.bt_add.setObjectName(_fromUtf8("bt_add"))
        self.bt_get = QtGui.QPushButton(self.centralwidget)
        self.bt_get.setGeometry(QtCore.QRect(430, 310, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_get.setFont(font)
        self.bt_get.setObjectName(_fromUtf8("bt_get"))
        self.bt_clear = QtGui.QPushButton(self.centralwidget)
        self.bt_clear.setGeometry(QtCore.QRect(520, 310, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_clear.setFont(font)
        self.bt_clear.setObjectName(_fromUtf8("bt_clear"))
        ProxyBook.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ProxyBook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ProxyBook.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ProxyBook)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ProxyBook.setStatusBar(self.statusbar)

        self.retranslateUi(ProxyBook)
        QtCore.QObject.connect(self.bt_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.edit_name.clear)
        QtCore.QObject.connect(self.bt_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.edit_id.clear)
        QtCore.QMetaObject.connectSlotsByName(ProxyBook)

    def retranslateUi(self, ProxyBook):
        ProxyBook.setWindowTitle(_translate("ProxyBook", "ProxyBook", None))
        self.label_name.setText(_translate("ProxyBook", "姓名：", None))
        self.label_id.setText(_translate("ProxyBook", "  ID：", None))
        self.bt_print.setText(_translate("ProxyBook", "打印", None))
        self.bt_add.setText(_translate("ProxyBook", "添加", None))
        self.bt_get.setText(_translate("ProxyBook", "获取", None))
        self.bt_clear.setText(_translate("ProxyBook", "清空", None))

