# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_DataBase(object):
    def setupUi(self, DataBase):
        if not DataBase.objectName():
            DataBase.setObjectName(u"DataBase")
        DataBase.resize(746, 669)
        DataBase.setMinimumSize(QSize(679, 589))
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setBold(True)
        DataBase.setFont(font)
        DataBase.setCursor(QCursor(Qt.ArrowCursor))
        DataBase.setAutoFillBackground(False)
        DataBase.setStyleSheet(u"")
        self.centralwidget = QWidget(DataBase)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 50, 711, 41))
        self.gridLayoutWidget.setFont(font)
        self.add_deleteLO = QGridLayout(self.gridLayoutWidget)
        self.add_deleteLO.setObjectName(u"add_deleteLO")
        self.add_deleteLO.setContentsMargins(0, 0, 0, 0)
        self.delete_std = QPushButton(self.gridLayoutWidget)
        self.delete_std.setObjectName(u"delete_std")
        self.delete_std.setFont(font)

        self.add_deleteLO.addWidget(self.delete_std, 0, 2, 1, 1)

        self.delete_var = QPushButton(self.gridLayoutWidget)
        self.delete_var.setObjectName(u"delete_var")
        self.delete_var.setFont(font)

        self.add_deleteLO.addWidget(self.delete_var, 0, 3, 1, 1)

        self.add_var = QPushButton(self.gridLayoutWidget)
        self.add_var.setObjectName(u"add_var")
        self.add_var.setFont(font)

        self.add_deleteLO.addWidget(self.add_var, 0, 1, 1, 1)

        self.add_std = QPushButton(self.gridLayoutWidget)
        self.add_std.setObjectName(u"add_std")
        self.add_std.setFont(font)

        self.add_deleteLO.addWidget(self.add_std, 0, 0, 1, 1)

        self.dbName = QTextEdit(self.centralwidget)
        self.dbName.setObjectName(u"dbName")
        self.dbName.setGeometry(QRect(20, 10, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Dubai"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.dbName.setFont(font1)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(150, 0, 481, 51))
        self.horizontalLayoutWidget.setFont(font)
        self.createLO = QHBoxLayout(self.horizontalLayoutWidget)
        self.createLO.setObjectName(u"createLO")
        self.createLO.setContentsMargins(0, 0, 0, 0)
        self.create = QPushButton(self.horizontalLayoutWidget)
        self.create.setObjectName(u"create")
        self.create.setFont(font)

        self.createLO.addWidget(self.create)

        self.open = QPushButton(self.horizontalLayoutWidget)
        self.open.setObjectName(u"open")
        self.open.setFont(font)

        self.createLO.addWidget(self.open)

        self.fill = QPushButton(self.horizontalLayoutWidget)
        self.fill.setObjectName(u"fill")
        self.fill.setFont(font)

        self.createLO.addWidget(self.fill)

        self.textFill = QTextEdit(self.centralwidget)
        self.textFill.setObjectName(u"textFill")
        self.textFill.setGeometry(QRect(640, 10, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"Dubai"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.textFill.setFont(font2)
        self.print_all = QPushButton(self.centralwidget)
        self.print_all.setObjectName(u"print_all")
        self.print_all.setGeometry(QRect(260, 640, 281, 24))
        self.print_all.setFont(font)
        self.studentID = QTextEdit(self.centralwidget)
        self.studentID.setObjectName(u"studentID")
        self.studentID.setGeometry(QRect(480, 90, 71, 31))
        self.studentID.setFont(font)
        self.variantID = QTextEdit(self.centralwidget)
        self.variantID.setObjectName(u"variantID")
        self.variantID.setGeometry(QRect(660, 90, 71, 31))
        self.variantID.setFont(font)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(410, 120, 321, 41))
        self.horizontalLayoutWidget_2.setFont(font)
        self.editLO = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.editLO.setObjectName(u"editLO")
        self.editLO.setContentsMargins(0, 0, 0, 0)
        self.edit_std = QPushButton(self.horizontalLayoutWidget_2)
        self.edit_std.setObjectName(u"edit_std")
        self.edit_std.setFont(font)

        self.editLO.addWidget(self.edit_std)

        self.edit_var = QPushButton(self.horizontalLayoutWidget_2)
        self.edit_var.setObjectName(u"edit_var")
        self.edit_var.setFont(font)

        self.editLO.addWidget(self.edit_var)

        self.giveVar = QPushButton(self.centralwidget)
        self.giveVar.setObjectName(u"giveVar")
        self.giveVar.setGeometry(QRect(410, 160, 321, 31))
        self.giveVar.setFont(font)
        self.stdID_lbl = QLabel(self.centralwidget)
        self.stdID_lbl.setObjectName(u"stdID_lbl")
        self.stdID_lbl.setGeometry(QRect(410, 100, 71, 20))
        self.stdID_lbl.setFont(font)
        self.varI_lbl = QLabel(self.centralwidget)
        self.varI_lbl.setObjectName(u"varI_lbl")
        self.varI_lbl.setGeometry(QRect(590, 100, 71, 20))
        self.varI_lbl.setFont(font)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 248, 711, 51))
        self.gridLayoutWidget_2.setFont(font)
        self.printLO = QGridLayout(self.gridLayoutWidget_2)
        self.printLO.setObjectName(u"printLO")
        self.printLO.setContentsMargins(0, 0, 0, 0)
        self.print_IDs = QPushButton(self.gridLayoutWidget_2)
        self.print_IDs.setObjectName(u"print_IDs")
        self.print_IDs.setFont(font)

        self.printLO.addWidget(self.print_IDs, 0, 2, 1, 1)

        self.print_info = QPushButton(self.gridLayoutWidget_2)
        self.print_info.setObjectName(u"print_info")
        self.print_info.setFont(font)

        self.printLO.addWidget(self.print_info, 0, 3, 1, 1)

        self.print_vars = QPushButton(self.gridLayoutWidget_2)
        self.print_vars.setObjectName(u"print_vars")
        self.print_vars.setFont(font)

        self.printLO.addWidget(self.print_vars, 0, 1, 1, 1)

        self.print_std = QPushButton(self.gridLayoutWidget_2)
        self.print_std.setObjectName(u"print_std")
        self.print_std.setFont(font)

        self.printLO.addWidget(self.print_std, 0, 0, 1, 1)

        self.stdID = QTextEdit(self.gridLayoutWidget_2)
        self.stdID.setObjectName(u"stdID")
        self.stdID.setMinimumSize(QSize(0, 31))
        self.stdID.setMaximumSize(QSize(60, 27))
        self.stdID.setBaseSize(QSize(1, 40))
        font3 = QFont()
        font3.setFamilies([u"Dubai"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.stdID.setFont(font3)

        self.printLO.addWidget(self.stdID, 0, 4, 1, 1)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 198, 721, 51))
        self.horizontalLayoutWidget_3.setFont(font)
        self.saveLO = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.saveLO.setObjectName(u"saveLO")
        self.saveLO.setContentsMargins(0, 0, 0, 0)
        self.save = QPushButton(self.horizontalLayoutWidget_3)
        self.save.setObjectName(u"save")
        self.save.setFont(font)

        self.saveLO.addWidget(self.save)

        self.upload = QPushButton(self.horizontalLayoutWidget_3)
        self.upload.setObjectName(u"upload")
        self.upload.setFont(font)

        self.saveLO.addWidget(self.upload)

        self.createBU = QPushButton(self.horizontalLayoutWidget_3)
        self.createBU.setObjectName(u"createBU")
        self.createBU.setFont(font)

        self.saveLO.addWidget(self.createBU)

        self.uploadBU = QPushButton(self.horizontalLayoutWidget_3)
        self.uploadBU.setObjectName(u"uploadBU")
        self.uploadBU.setFont(font)

        self.saveLO.addWidget(self.uploadBU)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 300, 721, 331))
        font4 = QFont()
        font4.setFamilies([u"Dubai"])
        font4.setBold(False)
        self.tableWidget.setFont(font4)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 640, 75, 24))
        self.pushButton.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 130, 301, 41))
        self.label.setFont(font)
        self.textAdd = QPlainTextEdit(self.centralwidget)
        self.textAdd.setObjectName(u"textAdd")
        self.textAdd.setGeometry(QRect(20, 90, 351, 32))
        self.textAdd.setMinimumSize(QSize(0, 31))
        self.textAdd.setFont(font2)
        DataBase.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataBase)

        QMetaObject.connectSlotsByName(DataBase)
    # setupUi

    def retranslateUi(self, DataBase):
        DataBase.setWindowTitle(QCoreApplication.translate("DataBase", u"DataBase", None))
        self.delete_std.setText(QCoreApplication.translate("DataBase", u"delete student", None))
        self.delete_var.setText(QCoreApplication.translate("DataBase", u"delete variant", None))
        self.add_var.setText(QCoreApplication.translate("DataBase", u"add variant", None))
        self.add_std.setText(QCoreApplication.translate("DataBase", u"add student", None))
        self.dbName.setHtml(QCoreApplication.translate("DataBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Dubai'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.create.setText(QCoreApplication.translate("DataBase", u"CREATE", None))
        self.open.setText(QCoreApplication.translate("DataBase", u"OPEN", None))
        self.fill.setText(QCoreApplication.translate("DataBase", u"FILL", None))
        self.textFill.setHtml(QCoreApplication.translate("DataBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Dubai'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.print_all.setText(QCoreApplication.translate("DataBase", u"PRINT TABLE FOR TEACHER", None))
        self.edit_std.setText(QCoreApplication.translate("DataBase", u"edit student", None))
        self.edit_var.setText(QCoreApplication.translate("DataBase", u"edit variant", None))
        self.giveVar.setText(QCoreApplication.translate("DataBase", u"change variant", None))
        self.stdID_lbl.setText(QCoreApplication.translate("DataBase", u"STUDENT ID:", None))
        self.varI_lbl.setText(QCoreApplication.translate("DataBase", u"VARIANT ID:", None))
        self.print_IDs.setText(QCoreApplication.translate("DataBase", u"print IDs table", None))
        self.print_info.setText(QCoreApplication.translate("DataBase", u"print info", None))
        self.print_vars.setText(QCoreApplication.translate("DataBase", u"print variants", None))
        self.print_std.setText(QCoreApplication.translate("DataBase", u"print students", None))
        self.save.setText(QCoreApplication.translate("DataBase", u"save", None))
        self.upload.setText(QCoreApplication.translate("DataBase", u"upload", None))
        self.createBU.setText(QCoreApplication.translate("DataBase", u"create backup", None))
        self.uploadBU.setText(QCoreApplication.translate("DataBase", u"upload backup", None))
        self.pushButton.setText(QCoreApplication.translate("DataBase", u"DELETE", None))
        self.label.setText(QCoreApplication.translate("DataBase", u"TextLabel", None))
#if QT_CONFIG(whatsthis)
        self.textAdd.setWhatsThis(QCoreApplication.translate("DataBase", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

