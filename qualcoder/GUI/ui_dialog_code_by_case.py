# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_code_by_case.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_code_by_case(object):
    def setupUi(self, Dialog_code_by_case):
        Dialog_code_by_case.setObjectName("Dialog_code_by_case")
        Dialog_code_by_case.resize(1024, 695)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_code_by_case)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_code_by_case)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_coder = QtWidgets.QLabel(self.groupBox)
        self.label_coder.setGeometry(QtCore.QRect(10, 0, 281, 28))
        self.label_coder.setObjectName("label_coder")
        self.lineEdit_search = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_search.setGeometry(QtCore.QRect(477, 1, 171, 30))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.checkBox_search_case = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_search_case.setGeometry(QtCore.QRect(667, 1, 21, 36))
        self.checkBox_search_case.setText("")
        self.checkBox_search_case.setObjectName("checkBox_search_case")
        self.checkBox_search_all_files = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_search_all_files.setGeometry(QtCore.QRect(727, 1, 21, 36))
        self.checkBox_search_all_files.setText("")
        self.checkBox_search_all_files.setObjectName("checkBox_search_all_files")
        self.label_search_totals = QtWidgets.QLabel(self.groupBox)
        self.label_search_totals.setGeometry(QtCore.QRect(880, 7, 81, 22))
        self.label_search_totals.setAlignment(QtCore.Qt.AlignCenter)
        self.label_search_totals.setObjectName("label_search_totals")
        self.label_codes_count = QtWidgets.QLabel(self.groupBox)
        self.label_codes_count.setGeometry(QtCore.QRect(570, 46, 41, 22))
        self.label_codes_count.setText("")
        self.label_codes_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_codes_count.setObjectName("label_codes_count")
        self.pushButton_previous = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_previous.setGeometry(QtCore.QRect(797, 1, 28, 28))
        self.pushButton_previous.setText("")
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setGeometry(QtCore.QRect(837, 1, 28, 28))
        self.pushButton_next.setText("")
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_search_all_files = QtWidgets.QLabel(self.groupBox)
        self.label_search_all_files.setGeometry(QtCore.QRect(753, 4, 24, 24))
        self.label_search_all_files.setAutoFillBackground(False)
        self.label_search_all_files.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search_all_files.setText("")
        self.label_search_all_files.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_search_all_files.setWordWrap(True)
        self.label_search_all_files.setObjectName("label_search_all_files")
        self.label_search_case_sensitive = QtWidgets.QLabel(self.groupBox)
        self.label_search_case_sensitive.setGeometry(QtCore.QRect(687, 4, 24, 24))
        self.label_search_case_sensitive.setAutoFillBackground(False)
        self.label_search_case_sensitive.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search_case_sensitive.setText("")
        self.label_search_case_sensitive.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_search_case_sensitive.setWordWrap(True)
        self.label_search_case_sensitive.setObjectName("label_search_case_sensitive")
        self.pushButton_annotate = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_annotate.setGeometry(QtCore.QRect(360, 0, 28, 28))
        self.pushButton_annotate.setText("")
        self.pushButton_annotate.setObjectName("pushButton_annotate")
        self.pushButton_coding_memo = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_coding_memo.setGeometry(QtCore.QRect(400, 0, 28, 28))
        self.pushButton_coding_memo.setText("")
        self.pushButton_coding_memo.setObjectName("pushButton_coding_memo")
        self.label_search_regex = QtWidgets.QLabel(self.groupBox)
        self.label_search_regex.setGeometry(QtCore.QRect(447, 4, 24, 24))
        self.label_search_regex.setAutoFillBackground(False)
        self.label_search_regex.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search_regex.setText("")
        self.label_search_regex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_search_regex.setWordWrap(True)
        self.label_search_regex.setObjectName("label_search_regex")
        self.pushButton_help = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_help.setGeometry(QtCore.QRect(970, 0, 28, 28))
        self.pushButton_help.setText("")
        self.pushButton_help.setObjectName("pushButton_help")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Dialog_code_by_case)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leftsplitter = QtWidgets.QSplitter(self.splitter)
        self.leftsplitter.setOrientation(QtCore.Qt.Vertical)
        self.leftsplitter.setObjectName("leftsplitter")
        self.listWidget = QtWidgets.QListWidget(self.leftsplitter)
        self.listWidget.setObjectName("listWidget")
        self.groupBox_file_buttons = QtWidgets.QGroupBox(self.leftsplitter)
        self.groupBox_file_buttons.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_file_buttons.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_file_buttons.setTitle("")
        self.groupBox_file_buttons.setObjectName("groupBox_file_buttons")
        self.pushButton_latest = QtWidgets.QPushButton(self.groupBox_file_buttons)
        self.pushButton_latest.setGeometry(QtCore.QRect(40, 0, 28, 28))
        self.pushButton_latest.setText("")
        self.pushButton_latest.setObjectName("pushButton_latest")
        self.pushButton_next_2 = QtWidgets.QPushButton(self.groupBox_file_buttons)
        self.pushButton_next_2.setGeometry(QtCore.QRect(0, 0, 28, 28))
        self.pushButton_next_2.setText("")
        self.pushButton_next_2.setObjectName("pushButton_next_2")
        self.label_case = QtWidgets.QLabel(self.groupBox_file_buttons)
        self.label_case.setGeometry(QtCore.QRect(140, 5, 221, 17))
        self.label_case.setObjectName("label_case")
        self.pushButton_goto_id = QtWidgets.QPushButton(self.groupBox_file_buttons)
        self.pushButton_goto_id.setGeometry(QtCore.QRect(80, 0, 28, 28))
        self.pushButton_goto_id.setText("")
        self.pushButton_goto_id.setObjectName("pushButton_goto_id")
        self.treeWidget = QtWidgets.QTreeWidget(self.leftsplitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.groupBox_coding_buttons = QtWidgets.QGroupBox(self.leftsplitter)
        self.groupBox_coding_buttons.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_coding_buttons.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_coding_buttons.setTitle("")
        self.groupBox_coding_buttons.setObjectName("groupBox_coding_buttons")
        self.pushButton_show_all_codings = QtWidgets.QPushButton(self.groupBox_coding_buttons)
        self.pushButton_show_all_codings.setGeometry(QtCore.QRect(90, 0, 28, 28))
        self.pushButton_show_all_codings.setText("")
        self.pushButton_show_all_codings.setObjectName("pushButton_show_all_codings")
        self.pushButton_show_codings_prev = QtWidgets.QPushButton(self.groupBox_coding_buttons)
        self.pushButton_show_codings_prev.setGeometry(QtCore.QRect(10, 0, 28, 28))
        self.pushButton_show_codings_prev.setText("")
        self.pushButton_show_codings_prev.setObjectName("pushButton_show_codings_prev")
        self.pushButton_show_codings_next = QtWidgets.QPushButton(self.groupBox_coding_buttons)
        self.pushButton_show_codings_next.setGeometry(QtCore.QRect(50, 0, 28, 28))
        self.pushButton_show_codings_next.setText("")
        self.pushButton_show_codings_next.setObjectName("pushButton_show_codings_next")
        self.pushButton_important = QtWidgets.QPushButton(self.groupBox_coding_buttons)
        self.pushButton_important.setGeometry(QtCore.QRect(130, 0, 28, 28))
        self.pushButton_important.setText("")
        self.pushButton_important.setObjectName("pushButton_important")
        self.label_code = QtWidgets.QLabel(self.groupBox_coding_buttons)
        self.label_code.setGeometry(QtCore.QRect(180, 0, 28, 28))
        self.label_code.setText("")
        self.label_code.setWordWrap(True)
        self.label_code.setObjectName("label_code")
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.retranslateUi(Dialog_code_by_case)
        QtCore.QMetaObject.connectSlotsByName(Dialog_code_by_case)
        Dialog_code_by_case.setTabOrder(self.lineEdit_search, self.pushButton_previous)
        Dialog_code_by_case.setTabOrder(self.pushButton_previous, self.pushButton_next)
        Dialog_code_by_case.setTabOrder(self.pushButton_next, self.checkBox_search_case)
        Dialog_code_by_case.setTabOrder(self.checkBox_search_case, self.checkBox_search_all_files)
        Dialog_code_by_case.setTabOrder(self.checkBox_search_all_files, self.textEdit)

    def retranslateUi(self, Dialog_code_by_case):
        _translate = QtCore.QCoreApplication.translate
        Dialog_code_by_case.setWindowTitle(_translate("Dialog_code_by_case", "Code by case"))
        self.label_coder.setText(_translate("Dialog_code_by_case", "Coder:"))
        self.lineEdit_search.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Search for text.</p><p>check <span style=\" font-weight:600;\">Case sensitive</span> for case sensitive search</p><p>check <span style=\" font-weight:600;\">All files</span> for searching all files search</p>\n"
"<p>Right-click to change automatic searching options</p></body></html>"))
        self.checkBox_search_case.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>search case sensitive</p></body></html>"))
        self.checkBox_search_all_files.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>search all files</p></body></html>"))
        self.label_search_totals.setText(_translate("Dialog_code_by_case", "0 / 0"))
        self.pushButton_previous.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Previous</p></body></html>"))
        self.pushButton_next.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Next</p></body></html>"))
        self.label_search_all_files.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Search text. All text files.</p></body></html>"))
        self.label_search_case_sensitive.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Search text. Case sensitive</p></body></html>"))
        self.pushButton_annotate.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Annotate selection</p></body></html>"))
        self.pushButton_coding_memo.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Memo for this coded section</p></body></html>"))
        self.label_search_regex.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Search uses Regex functions. </p><p>A dot ‘.’ is used as a wild card, e.g. ‘.ears’ will match ‘bears’ and ‘years’. </p><p>A ‘?’ after a character will match one or none times that character, e.g. ‘bears?’ will match ‘bear’ and ‘bears’ </p><p><span style=\" background-color:transparent;\">A ‘*’ after a character will match zero or more times. </span></p><p><span style=\" background-color:transparent;\">‘</span>\\. will match the dot symbol, ‘\\?’ will match the question mark. ‘\\n’ will match the line ending symbol. </p><p>Regex cheatsheet: www.rexegg.com/regex-quickstart.html</p></body></html>"))
        self.pushButton_help.setToolTip(_translate("Dialog_code_by_case", "Help"))
        self.pushButton_latest.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>File with latest coding</p></body></html>"))
        self.pushButton_next_2.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Next file</p></body></html>"))
        self.label_case.setText(_translate("Dialog_code_by_case", "."))
        self.pushButton_goto_id.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>File with latest coding</p></body></html>"))
        self.pushButton_show_all_codings.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Show all codings</p></body></html>"))
        self.pushButton_show_codings_prev.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Show previous coding of selected code</p></body></html>"))
        self.pushButton_show_codings_next.setToolTip(_translate("Dialog_code_by_case", "<html><head/><body><p>Show next coding of selected code.</p></body></html>"))
        self.pushButton_important.setToolTip(_translate("Dialog_code_by_case", "Show codings flagged important"))
        self.label_code.setToolTip(_translate("Dialog_code_by_case", "Right click below to create new codes and categories"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_code_by_case = QtWidgets.QDialog()
    ui = Ui_Dialog_code_by_case()
    ui.setupUi(Dialog_code_by_case)
    Dialog_code_by_case.show()
    sys.exit(app.exec_())
