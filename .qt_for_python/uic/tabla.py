# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabla.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(454, 464)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(50, 130))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 421, 111))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.formLayoutWidget)
        self.label_nombre.setObjectName(u"label_nombre")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_nombre)

        self.nombre = QLineEdit(self.formLayoutWidget)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nombre)

        self.label_empleo = QLabel(self.formLayoutWidget)
        self.label_empleo.setObjectName(u"label_empleo")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_empleo)

        self.empleo = QLineEdit(self.formLayoutWidget)
        self.empleo.setObjectName(u"empleo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.empleo)

        self.label_email = QLabel(self.formLayoutWidget)
        self.label_email.setObjectName(u"label_email")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_email)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.boton_nuevo = QPushButton(self.formLayoutWidget)
        self.boton_nuevo.setObjectName(u"boton_nuevo")

        self.horizontalLayout.addWidget(self.boton_nuevo)

        self.boton_borrar = QPushButton(self.formLayoutWidget)
        self.boton_borrar.setObjectName(u"boton_borrar")

        self.horizontalLayout.addWidget(self.boton_borrar)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.tabla = QTableView(self.centralwidget)
        self.tabla.setObjectName(u"tabla")

        self.verticalLayout.addWidget(self.tabla)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos del contacto", None))
        self.label_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.nombre.setText("")
        self.label_empleo.setText(QCoreApplication.translate("MainWindow", u"Empleo", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.boton_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.boton_borrar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
    # retranslateUi

