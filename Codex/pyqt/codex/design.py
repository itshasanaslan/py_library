# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from codex import CodeX

class Ui_Codex(object):
    def setupUi(self, Codex):
        Codex.setObjectName("Codex")
        Codex.resize(552, 594)
        Codex.setTabletTracking(False)
        self.txtHashKey = QtWidgets.QTextEdit(Codex)
        self.txtHashKey.setGeometry(QtCore.QRect(20, 60, 521, 61))
        self.txtHashKey.setObjectName("txtHashKey")
        self.txtHashKey.setText(CodeX.generate_hashkey())
        self.label = QtWidgets.QLabel(Codex)
        self.label.setGeometry(QtCore.QRect(20, 40, 151, 16))
        self.label.setObjectName("label")
        self.btnGenerate = QtWidgets.QPushButton(Codex)
        self.btnGenerate.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnGenerate.clicked.connect(lambda:self.txtHashKey.setText(CodeX.generate_hashkey()))
        self.btnSave = QtWidgets.QPushButton(Codex)
        self.btnSave.setGeometry(QtCore.QRect(130, 130, 93, 28))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(lambda: self.save_key())
        self.btnConvert = QtWidgets.QPushButton(Codex)
        self.btnConvert.setGeometry(QtCore.QRect(210, 500, 93, 28))
        self.btnConvert.setObjectName("btnConvert")
        self.btnConvert.clicked.connect(lambda: self.check_hash_key())
        self.lblWarning = QtWidgets.QLabel(Codex)
        self.lblWarning.setGeometry(QtCore.QRect(30, 20, 491, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblWarning.setFont(font)
        self.lblWarning.setAutoFillBackground(False)
        self.lblWarning.setObjectName("lblWarning")
        self.txtText = QtWidgets.QTextEdit(Codex)
        self.txtText.setGeometry(QtCore.QRect(20, 180, 511, 311))
        self.txtText.setObjectName("txtText")

        self.retranslateUi(Codex)
        QtCore.QMetaObject.connectSlotsByName(Codex)

    def retranslateUi(self, Codex):
        _translate = QtCore.QCoreApplication.translate
        Codex.setWindowTitle(_translate("Codex", "r/hasanaslan"))
        self.label.setText(_translate("Codex", "Encryption Key"))
        self.btnGenerate.setText(_translate("Codex", "Generate Key"))
        self.btnSave.setText(_translate("Codex", "Save Key"))
        self.btnConvert.setText(_translate("Codex", "Convert Text"))
        self.lblWarning.setText(_translate("Codex", "<html><head/><body><p><br/></p></body></html>"))
    def check_hash_key(self):
        text = self.txtHashKey.toPlainText()
        if len(text)!=107:
            self.lblWarning.setText("Key length must be 107 and must consist of non-repetitive characters!")
        else:
            self.lblWarning.setText("")
            self.txtText.setText(CodeX.convert_text(self.txtHashKey.toPlainText(),self.txtText.toPlainText()))
    def save_key(self):
        CodeX.save_hashkey(self.txtHashKey.toPlainText(),"HashKeys.txt")
        self.lblWarning.setText("Key saved to HashKeys.txt!")
