# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(411, 234)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        Dialog.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 51))
        self.groupBox.setObjectName("groupBox")
        self.btnSelectFile = QtWidgets.QPushButton(self.groupBox)
        self.btnSelectFile.setGeometry(QtCore.QRect(290, 20, 91, 23))
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.lineFileName = QtWidgets.QLineEdit(self.groupBox)
        self.lineFileName.setGeometry(QtCore.QRect(10, 21, 271, 21))
        self.lineFileName.setAutoFillBackground(False)
        self.lineFileName.setReadOnly(True)
        self.lineFileName.setObjectName("lineFileName")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 391, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cbModel = QtWidgets.QComboBox(self.groupBox_2)
        self.cbModel.setGeometry(QtCore.QRect(10, 30, 161, 22))
        self.cbModel.setObjectName("cbModel")
        self.cbStatusVariant = QtWidgets.QComboBox(self.groupBox_2)
        self.cbStatusVariant.setGeometry(QtCore.QRect(10, 70, 161, 22))
        self.cbStatusVariant.setObjectName("cbStatusVariant")
        self.leModel = QtWidgets.QLineEdit(self.groupBox_2)
        self.leModel.setGeometry(QtCore.QRect(200, 30, 181, 21))
        self.leModel.setReadOnly(True)
        self.leModel.setObjectName("leModel")
        self.leStatusVariant = QtWidgets.QLineEdit(self.groupBox_2)
        self.leStatusVariant.setGeometry(QtCore.QRect(200, 70, 181, 21))
        self.leStatusVariant.setReadOnly(True)
        self.leStatusVariant.setObjectName("leStatusVariant")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(180, 30, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(15, 195, 131, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btnConvert = QtWidgets.QPushButton(Dialog)
        self.btnConvert.setGeometry(QtCore.QRect(267, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnConvert.setFont(font)
        self.btnConvert.setObjectName("btnConvert")
        self.label_complit = QtWidgets.QLabel(Dialog)
        self.label_complit.setGeometry(QtCore.QRect(115, 200, 61, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_complit.setFont(font)
        self.label_complit.setObjectName("label_complit")
        self.cb_encoding = QtWidgets.QComboBox(Dialog)
        self.cb_encoding.setGeometry(QtCore.QRect(191, 191, 70, 29))
        self.cb_encoding.setObjectName("cb_encoding")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Конвертировать xlsx в csv (v1.0.1)"))
        self.groupBox.setTitle(_translate("Dialog", "Выберите файл: (xlsx)"))
        self.btnSelectFile.setText(_translate("Dialog", "Выбор файла"))
        self.groupBox_2.setTitle(_translate("Dialog", "Отметьте нужные поля:"))
        self.leModel.setText(_translate("Dialog", "_MODEL_"))
        self.leStatusVariant.setText(_translate("Dialog", "_STATUS_VARIANT_"))
        self.label.setText(_translate("Dialog", "="))
        self.label_2.setText(_translate("Dialog", "="))
        self.btnConvert.setText(_translate("Dialog", "Конвертировать"))
        self.label_complit.setText(_translate("Dialog", "TextLabel"))