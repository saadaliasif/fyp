from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_editpatientinfopage(object):
    def setupUi(self, editpatientinfopage):
        if not editpatientinfopage.objectName():
            editpatientinfopage.setObjectName(u"editpatientinfopage")
        editpatientinfopage.resize(1121, 843)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        editpatientinfopage.setFont(font)
        self.editpatientinfo_label = QLabel(editpatientinfopage)
        self.editpatientinfo_label.setObjectName(u"editpatientinfo_label")
        self.editpatientinfo_label.setGeometry(QRect(400, 10, 361, 52))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.editpatientinfo_label.setFont(font1)
        self.layoutWidget = QWidget(editpatientinfopage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(610, 560, 371, 71))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.back_pushButton = QPushButton(self.layoutWidget)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.horizontalLayout.addWidget(self.back_pushButton)

        self.save_pushButton = QPushButton(self.layoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.horizontalLayout.addWidget(self.save_pushButton)

        self.layoutWidget1 = QWidget(editpatientinfopage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(130, 80, 851, 481))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.name_lineEdit = QLineEdit(self.layoutWidget1)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.gridLayout.addWidget(self.name_lineEdit, 0, 1, 1, 1)

        self.postal_code_label = QLabel(self.layoutWidget1)
        self.postal_code_label.setObjectName(u"postal_code_label")

        self.gridLayout.addWidget(self.postal_code_label, 7, 0, 1, 1)

        self.country_label = QLabel(self.layoutWidget1)
        self.country_label.setObjectName(u"country_label")

        self.gridLayout.addWidget(self.country_label, 5, 0, 1, 1)

        self.phone_lineEdit = QLineEdit(self.layoutWidget1)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")

        self.gridLayout.addWidget(self.phone_lineEdit, 9, 1, 1, 1)

        self.postal_lineEdit = QLineEdit(self.layoutWidget1)
        self.postal_lineEdit.setObjectName(u"postal_lineEdit")

        self.gridLayout.addWidget(self.postal_lineEdit, 7, 1, 1, 1)

        self.email_lineEdit = QLineEdit(self.layoutWidget1)
        self.email_lineEdit.setObjectName(u"email_lineEdit")

        self.gridLayout.addWidget(self.email_lineEdit, 8, 1, 1, 1)

        self.age_lineEdit = QLineEdit(self.layoutWidget1)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.gridLayout.addWidget(self.age_lineEdit, 1, 1, 1, 1)

        self.sex_lineEdit = QLineEdit(self.layoutWidget1)
        self.sex_lineEdit.setObjectName(u"sex_lineEdit")

        self.gridLayout.addWidget(self.sex_lineEdit, 2, 1, 1, 1)

        self.sex_label = QLabel(self.layoutWidget1)
        self.sex_label.setObjectName(u"sex_label")

        self.gridLayout.addWidget(self.sex_label, 2, 0, 1, 1)

        self.age_label = QLabel(self.layoutWidget1)
        self.age_label.setObjectName(u"age_label")

        self.gridLayout.addWidget(self.age_label, 1, 0, 1, 1)

        self.phone_label = QLabel(self.layoutWidget1)
        self.phone_label.setObjectName(u"phone_label")

        self.gridLayout.addWidget(self.phone_label, 9, 0, 1, 1)

        self.income_label = QLabel(self.layoutWidget1)
        self.income_label.setObjectName(u"income_label")

        self.gridLayout.addWidget(self.income_label, 3, 0, 1, 1)

        self.city_label = QLabel(self.layoutWidget1)
        self.city_label.setObjectName(u"city_label")

        self.gridLayout.addWidget(self.city_label, 6, 0, 1, 1)

        self.income_lineEdit = QLineEdit(self.layoutWidget1)
        self.income_lineEdit.setObjectName(u"income_lineEdit")

        self.gridLayout.addWidget(self.income_lineEdit, 3, 1, 1, 1)

        self.educ_lineEdit = QLineEdit(self.layoutWidget1)
        self.educ_lineEdit.setObjectName(u"educ_lineEdit")

        self.gridLayout.addWidget(self.educ_lineEdit, 4, 1, 1, 1)

        self.city_lineEdit = QLineEdit(self.layoutWidget1)
        self.city_lineEdit.setObjectName(u"city_lineEdit")

        self.gridLayout.addWidget(self.city_lineEdit, 6, 1, 1, 1)

        self.country_lineEdit = QLineEdit(self.layoutWidget1)
        self.country_lineEdit.setObjectName(u"country_lineEdit")

        self.gridLayout.addWidget(self.country_lineEdit, 5, 1, 1, 1)

        self.name_label = QLabel(self.layoutWidget1)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.email_label = QLabel(self.layoutWidget1)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout.addWidget(self.email_label, 8, 0, 1, 1)

        self.education_label = QLabel(self.layoutWidget1)
        self.education_label.setObjectName(u"education_label")

        self.gridLayout.addWidget(self.education_label, 4, 0, 1, 1)


        self.retranslateUi(editpatientinfopage)

        QMetaObject.connectSlotsByName(editpatientinfopage)
    # setupUi

    def retranslateUi(self, editpatientinfopage):
        editpatientinfopage.setWindowTitle(QCoreApplication.translate("editpatientinfopage", u"Form", None))
        self.editpatientinfo_label.setText(QCoreApplication.translate("editpatientinfopage", u"Edit Patient Info", None))
        self.back_pushButton.setText(QCoreApplication.translate("editpatientinfopage", u"Back", None))
        self.save_pushButton.setText(QCoreApplication.translate("editpatientinfopage", u"Save", None))
        self.postal_code_label.setText(QCoreApplication.translate("editpatientinfopage", u"Postal code:", None))
        self.country_label.setText(QCoreApplication.translate("editpatientinfopage", u"Country:", None))
        self.sex_label.setText(QCoreApplication.translate("editpatientinfopage", u"Gender:", None))
        self.age_label.setText(QCoreApplication.translate("editpatientinfopage", u"Age:", None))
        self.phone_label.setText(QCoreApplication.translate("editpatientinfopage", u"Phone:", None))
        self.income_label.setText(QCoreApplication.translate("editpatientinfopage", u"Income:", None))
        self.city_label.setText(QCoreApplication.translate("editpatientinfopage", u"City:", None))
        self.name_label.setText(QCoreApplication.translate("editpatientinfopage", u"Name:", None))
        self.email_label.setText(QCoreApplication.translate("editpatientinfopage", u"Email:", None))
        self.education_label.setText(QCoreApplication.translate("editpatientinfopage", u"Education:", None))
    # retranslateUi

