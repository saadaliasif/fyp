from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_editpatientinfopage(object):
    def setupUi(self, editpatientinfopage):
        if not editpatientinfopage.objectName():
            editpatientinfopage.setObjectName(u"editpatientinfopage")
        editpatientinfopage.resize(805, 567)
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(14)
        editpatientinfopage.setFont(font)
        self.verticalLayout = QVBoxLayout(editpatientinfopage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.editpatientinfo_label = QLabel(editpatientinfopage)
        self.editpatientinfo_label.setObjectName(u"editpatientinfo_label")
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(24)
        self.editpatientinfo_label.setFont(font1)
        self.editpatientinfo_label.setAlignment(Qt.AlignCenter)
        self.editpatientinfo_label.setWordWrap(False)

        self.verticalLayout.addWidget(self.editpatientinfo_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_lineEdit = QLineEdit(editpatientinfopage)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.gridLayout.addWidget(self.name_lineEdit, 0, 1, 1, 1)

        self.postal_code_label = QLabel(editpatientinfopage)
        self.postal_code_label.setObjectName(u"postal_code_label")

        self.gridLayout.addWidget(self.postal_code_label, 7, 0, 1, 1)

        self.country_label = QLabel(editpatientinfopage)
        self.country_label.setObjectName(u"country_label")

        self.gridLayout.addWidget(self.country_label, 5, 0, 1, 1)

        self.phone_lineEdit = QLineEdit(editpatientinfopage)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")

        self.gridLayout.addWidget(self.phone_lineEdit, 9, 1, 1, 1)

        self.postal_lineEdit = QLineEdit(editpatientinfopage)
        self.postal_lineEdit.setObjectName(u"postal_lineEdit")

        self.gridLayout.addWidget(self.postal_lineEdit, 7, 1, 1, 1)

        self.email_lineEdit = QLineEdit(editpatientinfopage)
        self.email_lineEdit.setObjectName(u"email_lineEdit")

        self.gridLayout.addWidget(self.email_lineEdit, 8, 1, 1, 1)

        self.age_lineEdit = QLineEdit(editpatientinfopage)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.gridLayout.addWidget(self.age_lineEdit, 1, 1, 1, 1)

        self.sex_label = QLabel(editpatientinfopage)
        self.sex_label.setObjectName(u"sex_label")

        self.gridLayout.addWidget(self.sex_label, 2, 0, 1, 1)

        self.age_label = QLabel(editpatientinfopage)
        self.age_label.setObjectName(u"age_label")

        self.gridLayout.addWidget(self.age_label, 1, 0, 1, 1)

        self.phone_label = QLabel(editpatientinfopage)
        self.phone_label.setObjectName(u"phone_label")

        self.gridLayout.addWidget(self.phone_label, 9, 0, 1, 1)

        self.income_label = QLabel(editpatientinfopage)
        self.income_label.setObjectName(u"income_label")

        self.gridLayout.addWidget(self.income_label, 3, 0, 1, 1)

        self.city_label = QLabel(editpatientinfopage)
        self.city_label.setObjectName(u"city_label")

        self.gridLayout.addWidget(self.city_label, 6, 0, 1, 1)

        self.income_lineEdit = QLineEdit(editpatientinfopage)
        self.income_lineEdit.setObjectName(u"income_lineEdit")

        self.gridLayout.addWidget(self.income_lineEdit, 3, 1, 1, 1)

        self.name_label = QLabel(editpatientinfopage)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.email_label = QLabel(editpatientinfopage)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout.addWidget(self.email_label, 8, 0, 1, 1)

        self.education_label = QLabel(editpatientinfopage)
        self.education_label.setObjectName(u"education_label")

        self.gridLayout.addWidget(self.education_label, 4, 0, 1, 1)

        self.sex_comboBox = QComboBox(editpatientinfopage)
        self.sex_comboBox.addItem("")
        self.sex_comboBox.addItem("")
        self.sex_comboBox.setObjectName(u"sex_comboBox")

        self.gridLayout.addWidget(self.sex_comboBox, 2, 1, 1, 1)

        self.edu_comboBox = QComboBox(editpatientinfopage)
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.setObjectName(u"edu_comboBox")

        self.gridLayout.addWidget(self.edu_comboBox, 4, 1, 1, 1)

        self.country_comboBox = QComboBox(editpatientinfopage)
        self.country_comboBox.addItem("")
        self.country_comboBox.setObjectName(u"country_comboBox")

        self.gridLayout.addWidget(self.country_comboBox, 5, 1, 1, 1)

        self.city_comboBox = QComboBox(editpatientinfopage)
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.setObjectName(u"city_comboBox")

        self.gridLayout.addWidget(self.city_comboBox, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.back_pushButton = QPushButton(editpatientinfopage)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.horizontalLayout.addWidget(self.back_pushButton)

        self.save_pushButton = QPushButton(editpatientinfopage)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.horizontalLayout.addWidget(self.save_pushButton)

        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(editpatientinfopage)

        QMetaObject.connectSlotsByName(editpatientinfopage)
    # setupUi

    def retranslateUi(self, editpatientinfopage):
        editpatientinfopage.setWindowTitle(QCoreApplication.translate("editpatientinfopage", u"Form", None))
        self.editpatientinfo_label.setText(QCoreApplication.translate("editpatientinfopage", u"Edit Patient Info", None))
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
        self.sex_comboBox.setItemText(0, QCoreApplication.translate("editpatientinfopage", u"male", None))
        self.sex_comboBox.setItemText(1, QCoreApplication.translate("editpatientinfopage", u"female", None))

        self.edu_comboBox.setItemText(0, QCoreApplication.translate("editpatientinfopage", u"undergraduate", None))
        self.edu_comboBox.setItemText(1, QCoreApplication.translate("editpatientinfopage", u"graduate", None))
        self.edu_comboBox.setItemText(2, QCoreApplication.translate("editpatientinfopage", u"postgraduate", None))
        self.edu_comboBox.setItemText(3, QCoreApplication.translate("editpatientinfopage", u"phd", None))

        self.country_comboBox.setItemText(0, QCoreApplication.translate("editpatientinfopage", u"pakistan", None))

        self.city_comboBox.setItemText(0, QCoreApplication.translate("editpatientinfopage", u"islamabad", None))
        self.city_comboBox.setItemText(1, QCoreApplication.translate("editpatientinfopage", u"lahore", None))
        self.city_comboBox.setItemText(2, QCoreApplication.translate("editpatientinfopage", u"karachi", None))
        self.city_comboBox.setItemText(3, QCoreApplication.translate("editpatientinfopage", u"peshawar", None))
        self.city_comboBox.setItemText(4, QCoreApplication.translate("editpatientinfopage", u"gujrawala", None))
        self.city_comboBox.setItemText(5, QCoreApplication.translate("editpatientinfopage", u"multan", None))

        self.back_pushButton.setText(QCoreApplication.translate("editpatientinfopage", u"Back", None))
        self.save_pushButton.setText(QCoreApplication.translate("editpatientinfopage", u"Save", None))
    # retranslateUi

