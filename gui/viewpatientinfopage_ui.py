# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewpatientinfopage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_viewpatientinfopage(object):
    def setupUi(self, viewpatientinfopage):
        if not viewpatientinfopage.objectName():
            viewpatientinfopage.setObjectName(u"viewpatientinfopage")
        viewpatientinfopage.resize(1121, 843)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        viewpatientinfopage.setFont(font)
        self.viewpatientinfo_label = QLabel(viewpatientinfopage)
        self.viewpatientinfo_label.setObjectName(u"viewpatientinfo_label")
        self.viewpatientinfo_label.setGeometry(QRect(400, 10, 361, 52))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.viewpatientinfo_label.setFont(font1)
        self.layoutWidget = QWidget(viewpatientinfopage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(690, 720, 371, 71))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.back_pushButton = QPushButton(self.layoutWidget)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.horizontalLayout.addWidget(self.back_pushButton)

        self.delete_pushButton = QPushButton(self.layoutWidget)
        self.delete_pushButton.setObjectName(u"delete_pushButton")

        self.horizontalLayout.addWidget(self.delete_pushButton)

        self.edit_pushButton = QPushButton(self.layoutWidget)
        self.edit_pushButton.setObjectName(u"edit_pushButton")

        self.horizontalLayout.addWidget(self.edit_pushButton)

        self.layoutWidget1 = QWidget(viewpatientinfopage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(90, 80, 971, 631))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.postal_out_label = QLabel(self.layoutWidget1)
        self.postal_out_label.setObjectName(u"postal_out_label")

        self.gridLayout.addWidget(self.postal_out_label, 7, 1, 1, 1)

        self.email_out_label = QLabel(self.layoutWidget1)
        self.email_out_label.setObjectName(u"email_out_label")

        self.gridLayout.addWidget(self.email_out_label, 8, 1, 1, 1)

        self.phone_out_label = QLabel(self.layoutWidget1)
        self.phone_out_label.setObjectName(u"phone_out_label")

        self.gridLayout.addWidget(self.phone_out_label, 9, 1, 1, 1)

        self.income_out_label = QLabel(self.layoutWidget1)
        self.income_out_label.setObjectName(u"income_out_label")

        self.gridLayout.addWidget(self.income_out_label, 3, 1, 1, 1)

        self.result_out_label = QLabel(self.layoutWidget1)
        self.result_out_label.setObjectName(u"result_out_label")

        self.gridLayout.addWidget(self.result_out_label, 10, 1, 1, 1)

        self.email_label = QLabel(self.layoutWidget1)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout.addWidget(self.email_label, 8, 0, 1, 1)

        self.education_label = QLabel(self.layoutWidget1)
        self.education_label.setObjectName(u"education_label")

        self.gridLayout.addWidget(self.education_label, 4, 0, 1, 1)

        self.gender_out_label = QLabel(self.layoutWidget1)
        self.gender_out_label.setObjectName(u"gender_out_label")

        self.gridLayout.addWidget(self.gender_out_label, 2, 1, 1, 1)

        self.income_label = QLabel(self.layoutWidget1)
        self.income_label.setObjectName(u"income_label")

        self.gridLayout.addWidget(self.income_label, 3, 0, 1, 1)

        self.country_out_label = QLabel(self.layoutWidget1)
        self.country_out_label.setObjectName(u"country_out_label")

        self.gridLayout.addWidget(self.country_out_label, 5, 1, 1, 1)

        self.city_label = QLabel(self.layoutWidget1)
        self.city_label.setObjectName(u"city_label")

        self.gridLayout.addWidget(self.city_label, 6, 0, 1, 1)

        self.phone_label = QLabel(self.layoutWidget1)
        self.phone_label.setObjectName(u"phone_label")

        self.gridLayout.addWidget(self.phone_label, 9, 0, 1, 1)

        self.result_label = QLabel(self.layoutWidget1)
        self.result_label.setObjectName(u"result_label")

        self.gridLayout.addWidget(self.result_label, 10, 0, 1, 1)

        self.sex_label = QLabel(self.layoutWidget1)
        self.sex_label.setObjectName(u"sex_label")

        self.gridLayout.addWidget(self.sex_label, 2, 0, 1, 1)

        self.age_label = QLabel(self.layoutWidget1)
        self.age_label.setObjectName(u"age_label")

        self.gridLayout.addWidget(self.age_label, 1, 0, 1, 1)

        self.country_label = QLabel(self.layoutWidget1)
        self.country_label.setObjectName(u"country_label")

        self.gridLayout.addWidget(self.country_label, 5, 0, 1, 1)

        self.education_out_label = QLabel(self.layoutWidget1)
        self.education_out_label.setObjectName(u"education_out_label")

        self.gridLayout.addWidget(self.education_out_label, 4, 1, 1, 1)

        self.postal_code_label = QLabel(self.layoutWidget1)
        self.postal_code_label.setObjectName(u"postal_code_label")

        self.gridLayout.addWidget(self.postal_code_label, 7, 0, 1, 1)

        self.city_out_label = QLabel(self.layoutWidget1)
        self.city_out_label.setObjectName(u"city_out_label")

        self.gridLayout.addWidget(self.city_out_label, 6, 1, 1, 1)

        self.age_out_label = QLabel(self.layoutWidget1)
        self.age_out_label.setObjectName(u"age_out_label")

        self.gridLayout.addWidget(self.age_out_label, 1, 1, 1, 1)

        self.name_out_label = QLabel(self.layoutWidget1)
        self.name_out_label.setObjectName(u"name_out_label")

        self.gridLayout.addWidget(self.name_out_label, 0, 1, 1, 1)

        self.name_label = QLabel(self.layoutWidget1)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)


        self.retranslateUi(viewpatientinfopage)

        QMetaObject.connectSlotsByName(viewpatientinfopage)
    # setupUi

    def retranslateUi(self, viewpatientinfopage):
        viewpatientinfopage.setWindowTitle(QCoreApplication.translate("viewpatientinfopage", u"Form", None))
        self.viewpatientinfo_label.setText(QCoreApplication.translate("viewpatientinfopage", u"View Patient Info", None))
        self.back_pushButton.setText(QCoreApplication.translate("viewpatientinfopage", u"Back", None))
        self.delete_pushButton.setText(QCoreApplication.translate("viewpatientinfopage", u"delete", None))
        self.edit_pushButton.setText(QCoreApplication.translate("viewpatientinfopage", u"Edit", None))
        self.postal_out_label.setText("")
        self.email_out_label.setText("")
        self.phone_out_label.setText("")
        self.income_out_label.setText("")
        self.result_out_label.setText("")
        self.email_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Email:", None))
        self.education_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Education:", None))
        self.gender_out_label.setText("")
        self.income_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Income:", None))
        self.country_out_label.setText("")
        self.city_label.setText(QCoreApplication.translate("viewpatientinfopage", u"City:", None))
        self.phone_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Phone:", None))
        self.result_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Result:", None))
        self.sex_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Gender:", None))
        self.age_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Age:", None))
        self.country_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Country:", None))
        self.education_out_label.setText("")
        self.postal_code_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Postal code:", None))
        self.city_out_label.setText("")
        self.age_out_label.setText("")
        self.name_out_label.setText("")
        self.name_label.setText(QCoreApplication.translate("viewpatientinfopage", u"Name:", None))
    # retranslateUi

