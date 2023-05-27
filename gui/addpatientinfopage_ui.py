# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addpatientinfopage.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_addpatientinfopage(object):
    def setupUi(self, addpatientinfopage):
        if not addpatientinfopage.objectName():
            addpatientinfopage.setObjectName(u"addpatientinfopage")
        addpatientinfopage.resize(1123, 723)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        addpatientinfopage.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(addpatientinfopage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addpatientinfo_label = QLabel(addpatientinfopage)
        self.addpatientinfo_label.setObjectName(u"addpatientinfo_label")
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.addpatientinfo_label.setFont(font1)
        self.addpatientinfo_label.setTextFormat(Qt.AutoText)

        self.verticalLayout.addWidget(self.addpatientinfo_label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(69)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.first_name_label = QLabel(addpatientinfopage)
        self.first_name_label.setObjectName(u"first_name_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.first_name_label)

        self.first_name_lineEdit = QLineEdit(addpatientinfopage)
        self.first_name_lineEdit.setObjectName(u"first_name_lineEdit")
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.first_name_lineEdit.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.first_name_lineEdit)

        self.last_name_label = QLabel(addpatientinfopage)
        self.last_name_label.setObjectName(u"last_name_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.last_name_label)

        self.last_name_lineEdit = QLineEdit(addpatientinfopage)
        self.last_name_lineEdit.setObjectName(u"last_name_lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.last_name_lineEdit)

        self.age_label = QLabel(addpatientinfopage)
        self.age_label.setObjectName(u"age_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.age_label)

        self.age_lineEdit = QLineEdit(addpatientinfopage)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.age_lineEdit)

        self.sex_label = QLabel(addpatientinfopage)
        self.sex_label.setObjectName(u"sex_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.sex_label)

        self.sex_lineEdit = QLineEdit(addpatientinfopage)
        self.sex_lineEdit.setObjectName(u"sex_lineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.sex_lineEdit)

        self.phone_label = QLabel(addpatientinfopage)
        self.phone_label.setObjectName(u"phone_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.phone_label)

        self.phone_lineEdit = QLineEdit(addpatientinfopage)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.phone_lineEdit)

        self.education_label = QLabel(addpatientinfopage)
        self.education_label.setObjectName(u"education_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.education_label)

        self.education_lineEdit = QLineEdit(addpatientinfopage)
        self.education_lineEdit.setObjectName(u"education_lineEdit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.education_lineEdit)

        self.income_label = QLabel(addpatientinfopage)
        self.income_label.setObjectName(u"income_label")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.income_label)

        self.income_lineEdit = QLineEdit(addpatientinfopage)
        self.income_lineEdit.setObjectName(u"income_lineEdit")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.income_lineEdit)

        self.city_label = QLabel(addpatientinfopage)
        self.city_label.setObjectName(u"city_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.city_label)

        self.city_lineEdit = QLineEdit(addpatientinfopage)
        self.city_lineEdit.setObjectName(u"city_lineEdit")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.city_lineEdit)

        self.country_label = QLabel(addpatientinfopage)
        self.country_label.setObjectName(u"country_label")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.country_label)

        self.country_lineEdit = QLineEdit(addpatientinfopage)
        self.country_lineEdit.setObjectName(u"country_lineEdit")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.country_lineEdit)

        self.email_lineEdit = QLineEdit(addpatientinfopage)
        self.email_lineEdit.setObjectName(u"email_lineEdit")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.email_lineEdit)

        self.postal_code_label = QLabel(addpatientinfopage)
        self.postal_code_label.setObjectName(u"postal_code_label")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.postal_code_label)

        self.postal_code_lineEdit = QLineEdit(addpatientinfopage)
        self.postal_code_lineEdit.setObjectName(u"postal_code_lineEdit")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.postal_code_lineEdit)

        self.email_label = QLabel(addpatientinfopage)
        self.email_label.setObjectName(u"email_label")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.email_label)


        self.verticalLayout.addLayout(self.formLayout)

        self.addpatientinfo_pushButton = QPushButton(addpatientinfopage)
        self.addpatientinfo_pushButton.setObjectName(u"addpatientinfo_pushButton")

        self.verticalLayout.addWidget(self.addpatientinfo_pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(addpatientinfopage)

        QMetaObject.connectSlotsByName(addpatientinfopage)
    # setupUi

    def retranslateUi(self, addpatientinfopage):
        addpatientinfopage.setWindowTitle(QCoreApplication.translate("addpatientinfopage", u"Form", None))
        self.addpatientinfo_label.setText(QCoreApplication.translate("addpatientinfopage", u"Add Patient Info", None))
        self.first_name_label.setText(QCoreApplication.translate("addpatientinfopage", u"first name:", None))
        self.last_name_label.setText(QCoreApplication.translate("addpatientinfopage", u"last name:", None))
        self.age_label.setText(QCoreApplication.translate("addpatientinfopage", u"age:", None))
        self.sex_label.setText(QCoreApplication.translate("addpatientinfopage", u"sex:", None))
        self.phone_label.setText(QCoreApplication.translate("addpatientinfopage", u"phone:", None))
        self.education_label.setText(QCoreApplication.translate("addpatientinfopage", u"education:", None))
        self.income_label.setText(QCoreApplication.translate("addpatientinfopage", u"income:", None))
        self.city_label.setText(QCoreApplication.translate("addpatientinfopage", u"city:", None))
        self.country_label.setText(QCoreApplication.translate("addpatientinfopage", u"country:", None))
        self.postal_code_label.setText(QCoreApplication.translate("addpatientinfopage", u"postal code:", None))
        self.email_label.setText(QCoreApplication.translate("addpatientinfopage", u"email", None))
        self.addpatientinfo_pushButton.setText(QCoreApplication.translate("addpatientinfopage", u"Add Patient Info", None))
    # retranslateUi

