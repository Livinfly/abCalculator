# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'abCalcUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QWidget)
from .. import resource_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(425, 579)
        font = QFont()
        font.setFamilies([u"Consolas"])
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(False)
        mainWindow.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Image/Image/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAnimated(True)
        mainWindow.setDocumentMode(False)
        mainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_8 = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 3, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Button8 = QPushButton(self.centralwidget)
        self.Button8.setObjectName(u"Button8")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button8.sizePolicy().hasHeightForWidth())
        self.Button8.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(20)
        self.Button8.setFont(font1)
        self.Button8.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button8, 1, 1, 1, 1)

        self.ButtonPlus = QPushButton(self.centralwidget)
        self.ButtonPlus.setObjectName(u"ButtonPlus")
        sizePolicy.setHeightForWidth(self.ButtonPlus.sizePolicy().hasHeightForWidth())
        self.ButtonPlus.setSizePolicy(sizePolicy)
        self.ButtonPlus.setFont(font1)
        self.ButtonPlus.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonPlus, 3, 3, 1, 1)

        self.ButtonMul = QPushButton(self.centralwidget)
        self.ButtonMul.setObjectName(u"ButtonMul")
        sizePolicy.setHeightForWidth(self.ButtonMul.sizePolicy().hasHeightForWidth())
        self.ButtonMul.setSizePolicy(sizePolicy)
        self.ButtonMul.setFont(font1)
        self.ButtonMul.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonMul, 1, 3, 1, 1)

        self.Button0 = QPushButton(self.centralwidget)
        self.Button0.setObjectName(u"Button0")
        sizePolicy.setHeightForWidth(self.Button0.sizePolicy().hasHeightForWidth())
        self.Button0.setSizePolicy(sizePolicy)
        self.Button0.setFont(font1)
        self.Button0.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button0, 4, 0, 1, 1)

        self.Button6 = QPushButton(self.centralwidget)
        self.Button6.setObjectName(u"Button6")
        sizePolicy.setHeightForWidth(self.Button6.sizePolicy().hasHeightForWidth())
        self.Button6.setSizePolicy(sizePolicy)
        self.Button6.setFont(font1)
        self.Button6.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button6, 2, 2, 1, 1)

        self.Button4 = QPushButton(self.centralwidget)
        self.Button4.setObjectName(u"Button4")
        sizePolicy.setHeightForWidth(self.Button4.sizePolicy().hasHeightForWidth())
        self.Button4.setSizePolicy(sizePolicy)
        self.Button4.setFont(font1)
        self.Button4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button4, 2, 0, 1, 1)

        self.ButtonPoint = QPushButton(self.centralwidget)
        self.ButtonPoint.setObjectName(u"ButtonPoint")
        sizePolicy.setHeightForWidth(self.ButtonPoint.sizePolicy().hasHeightForWidth())
        self.ButtonPoint.setSizePolicy(sizePolicy)
        self.ButtonPoint.setFont(font1)
        self.ButtonPoint.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonPoint, 4, 1, 1, 1)

        self.Button9 = QPushButton(self.centralwidget)
        self.Button9.setObjectName(u"Button9")
        sizePolicy.setHeightForWidth(self.Button9.sizePolicy().hasHeightForWidth())
        self.Button9.setSizePolicy(sizePolicy)
        self.Button9.setFont(font1)
        self.Button9.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button9, 1, 2, 1, 1)

        self.ButtonBackspace = QPushButton(self.centralwidget)
        self.ButtonBackspace.setObjectName(u"ButtonBackspace")
        sizePolicy.setHeightForWidth(self.ButtonBackspace.sizePolicy().hasHeightForWidth())
        self.ButtonBackspace.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.ButtonBackspace.setFont(font2)
        self.ButtonBackspace.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonBackspace, 0, 2, 1, 1)

        self.ButtonDiv = QPushButton(self.centralwidget)
        self.ButtonDiv.setObjectName(u"ButtonDiv")
        sizePolicy.setHeightForWidth(self.ButtonDiv.sizePolicy().hasHeightForWidth())
        self.ButtonDiv.setSizePolicy(sizePolicy)
        self.ButtonDiv.setFont(font1)
        self.ButtonDiv.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonDiv, 0, 3, 1, 1)

        self.Button7 = QPushButton(self.centralwidget)
        self.Button7.setObjectName(u"Button7")
        sizePolicy.setHeightForWidth(self.Button7.sizePolicy().hasHeightForWidth())
        self.Button7.setSizePolicy(sizePolicy)
        self.Button7.setFont(font1)
        self.Button7.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button7, 1, 0, 1, 1)

        self.ButtonSub = QPushButton(self.centralwidget)
        self.ButtonSub.setObjectName(u"ButtonSub")
        sizePolicy.setHeightForWidth(self.ButtonSub.sizePolicy().hasHeightForWidth())
        self.ButtonSub.setSizePolicy(sizePolicy)
        self.ButtonSub.setFont(font1)
        self.ButtonSub.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonSub, 2, 3, 1, 1)

        self.Button3 = QPushButton(self.centralwidget)
        self.Button3.setObjectName(u"Button3")
        sizePolicy.setHeightForWidth(self.Button3.sizePolicy().hasHeightForWidth())
        self.Button3.setSizePolicy(sizePolicy)
        self.Button3.setFont(font1)
        self.Button3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button3, 3, 2, 1, 1)

        self.ButtonClear = QPushButton(self.centralwidget)
        self.ButtonClear.setObjectName(u"ButtonClear")
        sizePolicy.setHeightForWidth(self.ButtonClear.sizePolicy().hasHeightForWidth())
        self.ButtonClear.setSizePolicy(sizePolicy)
        self.ButtonClear.setFont(font1)
        self.ButtonClear.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonClear, 0, 0, 1, 2)

        self.Button2 = QPushButton(self.centralwidget)
        self.Button2.setObjectName(u"Button2")
        sizePolicy.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy)
        self.Button2.setFont(font1)
        self.Button2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button2, 3, 1, 1, 1)

        self.ButtonEqual = QPushButton(self.centralwidget)
        self.ButtonEqual.setObjectName(u"ButtonEqual")
        sizePolicy.setHeightForWidth(self.ButtonEqual.sizePolicy().hasHeightForWidth())
        self.ButtonEqual.setSizePolicy(sizePolicy)
        self.ButtonEqual.setFont(font1)
        self.ButtonEqual.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ButtonEqual, 4, 2, 1, 2)

        self.Button5 = QPushButton(self.centralwidget)
        self.Button5.setObjectName(u"Button5")
        sizePolicy.setHeightForWidth(self.Button5.sizePolicy().hasHeightForWidth())
        self.Button5.setSizePolicy(sizePolicy)
        self.Button5.setFont(font1)
        self.Button5.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button5, 2, 1, 1, 1)

        self.Button1 = QPushButton(self.centralwidget)
        self.Button1.setObjectName(u"Button1")
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)
        self.Button1.setFont(font1)
        self.Button1.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Button1, 3, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.Result = QLineEdit(self.centralwidget)
        self.Result.setObjectName(u"Result")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Result.sizePolicy().hasHeightForWidth())
        self.Result.setSizePolicy(sizePolicy1)
        self.Result.setFont(font1)
        self.Result.setFocusPolicy(Qt.NoFocus)
        self.Result.setLayoutDirection(Qt.LeftToRight)
        self.Result.setStyleSheet(u"#Result {\n"
"	background:transparent;\n"
"	border-width:0;\n"
"	border-style:outset;\n"
"}")
        self.Result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Result.setReadOnly(True)

        self.horizontalLayout.addWidget(self.Result)

        self.horizontalSpacer_6 = QSpacerItem(40, 58, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.Course = QLineEdit(self.centralwidget)
        self.Course.setObjectName(u"Course")
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(15)
        self.Course.setFont(font3)
        self.Course.setFocusPolicy(Qt.NoFocus)
        self.Course.setStyleSheet(u"#Course {\n"
"	background:transparent;\n"
"	border-width:0;\n"
"	border-style:outset;\n"
"}")
        self.Course.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Course.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.Course)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(1, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 3, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 425, 21))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"abCalculator", None))
        self.Button8.setText(QCoreApplication.translate("mainWindow", u"8", None))
        self.ButtonPlus.setText(QCoreApplication.translate("mainWindow", u"+", None))
        self.ButtonMul.setText(QCoreApplication.translate("mainWindow", u"*", None))
        self.Button0.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.Button6.setText(QCoreApplication.translate("mainWindow", u"6", None))
        self.Button4.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.ButtonPoint.setText(QCoreApplication.translate("mainWindow", u".", None))
        self.Button9.setText(QCoreApplication.translate("mainWindow", u"9", None))
        self.ButtonBackspace.setText(QCoreApplication.translate("mainWindow", u"Backspace", None))
        self.ButtonDiv.setText(QCoreApplication.translate("mainWindow", u"/", None))
        self.Button7.setText(QCoreApplication.translate("mainWindow", u"7", None))
        self.ButtonSub.setText(QCoreApplication.translate("mainWindow", u"-", None))
        self.Button3.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.ButtonClear.setText(QCoreApplication.translate("mainWindow", u"C", None))
        self.Button2.setText(QCoreApplication.translate("mainWindow", u"2", None))
        self.ButtonEqual.setText(QCoreApplication.translate("mainWindow", u"=", None))
        self.Button5.setText(QCoreApplication.translate("mainWindow", u"5", None))
        self.Button1.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.Result.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.Course.setText(QCoreApplication.translate("mainWindow", u"0", None))
    # retranslateUi

