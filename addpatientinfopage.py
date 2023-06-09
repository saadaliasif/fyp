from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_addpatientinfopage(object):
    def setupUi(self, addpatientinfopage):
        if not addpatientinfopage.objectName():
            addpatientinfopage.setObjectName(u"addpatientinfopage")
        addpatientinfopage.resize(859, 617)
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        font.setBold(True)
        addpatientinfopage.setFont(font)
        self.verticalLayout = QVBoxLayout(addpatientinfopage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addpatientinfo_label = QLabel(addpatientinfopage)
        self.addpatientinfo_label.setObjectName(u"addpatientinfo_label")
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.addpatientinfo_label.setFont(font1)
        self.addpatientinfo_label.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.addpatientinfo_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(100)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(7, 7, 7, 7)
        self.first_name_label = QLabel(addpatientinfopage)
        self.first_name_label.setObjectName(u"first_name_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.first_name_label)

        self.first_name_lineEdit = QLineEdit(addpatientinfopage)
        self.first_name_lineEdit.setObjectName(u"first_name_lineEdit")
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.first_name_lineEdit.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.first_name_lineEdit)

        self.last_name_label = QLabel(addpatientinfopage)
        self.last_name_label.setObjectName(u"last_name_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.last_name_label)

        self.last_name_lineEdit = QLineEdit(addpatientinfopage)
        self.last_name_lineEdit.setObjectName(u"last_name_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.last_name_lineEdit)

        self.age_label = QLabel(addpatientinfopage)
        self.age_label.setObjectName(u"age_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.age_label)

        self.age_lineEdit = QLineEdit(addpatientinfopage)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.age_lineEdit)

        self.sex_label = QLabel(addpatientinfopage)
        self.sex_label.setObjectName(u"sex_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sex_label)

        self.phone_label = QLabel(addpatientinfopage)
        self.phone_label.setObjectName(u"phone_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.phone_label)

        self.phone_lineEdit = QLineEdit(addpatientinfopage)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.phone_lineEdit)

        self.education_label = QLabel(addpatientinfopage)
        self.education_label.setObjectName(u"education_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.education_label)

        self.income_label = QLabel(addpatientinfopage)
        self.income_label.setObjectName(u"income_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.income_label)

        self.income_lineEdit = QLineEdit(addpatientinfopage)
        self.income_lineEdit.setObjectName(u"income_lineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.income_lineEdit)

        self.city_label = QLabel(addpatientinfopage)
        self.city_label.setObjectName(u"city_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.city_label)

        self.city_comboBox = QComboBox(addpatientinfopage)
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.setObjectName(u"city_comboBox")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.city_comboBox)

        self.country_label = QLabel(addpatientinfopage)
        self.country_label.setObjectName(u"country_label")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.country_label)

        self.country_comboBox = QComboBox(addpatientinfopage)
        self.country_comboBox.addItem("")
        self.country_comboBox.setObjectName(u"country_comboBox")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.country_comboBox)

        self.email_label = QLabel(addpatientinfopage)
        self.email_label.setObjectName(u"email_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.email_label)

        self.email_lineEdit = QLineEdit(addpatientinfopage)
        self.email_lineEdit.setObjectName(u"email_lineEdit")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.email_lineEdit)

        self.postal_code_label = QLabel(addpatientinfopage)
        self.postal_code_label.setObjectName(u"postal_code_label")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.postal_code_label)

        self.postal_code_lineEdit = QLineEdit(addpatientinfopage)
        self.postal_code_lineEdit.setObjectName(u"postal_code_lineEdit")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.postal_code_lineEdit)

        self.sex_comboBox = QComboBox(addpatientinfopage)
        self.sex_comboBox.addItem("")
        self.sex_comboBox.addItem("")
        self.sex_comboBox.setObjectName(u"sex_comboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sex_comboBox)

        self.edu_comboBox = QComboBox(addpatientinfopage)
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.setObjectName(u"edu_comboBox")
        self.edu_comboBox.setIconSize(QSize(40, 20))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.edu_comboBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.back_pushButton = QPushButton(addpatientinfopage)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.horizontalLayout_2.addWidget(self.back_pushButton)

        self.addpatientinfo_pushButton = QPushButton(addpatientinfopage)
        self.addpatientinfo_pushButton.setObjectName(u"addpatientinfo_pushButton")

        self.horizontalLayout_2.addWidget(self.addpatientinfo_pushButton)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)


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
        self.city_comboBox.setItemText(0, QCoreApplication.translate("addpatientinfopage", u"islamabad", None))
        self.city_comboBox.setItemText(1, QCoreApplication.translate("addpatientinfopage", u"karachi", None))
        self.city_comboBox.setItemText(2, QCoreApplication.translate("addpatientinfopage", u"lahore", None))
        self.city_comboBox.setItemText(3, QCoreApplication.translate("addpatientinfopage", u"peshawar", None))
        self.city_comboBox.setItemText(4, QCoreApplication.translate("addpatientinfopage", u"multan", None))
        self.city_comboBox.setItemText(5, QCoreApplication.translate("addpatientinfopage", u"gujrawala", None))

        self.country_label.setText(QCoreApplication.translate("addpatientinfopage", u"country:", None))
        self.country_comboBox.setItemText(0, QCoreApplication.translate("addpatientinfopage", u"pakistan", None))

        self.email_label.setText(QCoreApplication.translate("addpatientinfopage", u"email", None))
        self.postal_code_label.setText(QCoreApplication.translate("addpatientinfopage", u"postal code:", None))
        self.sex_comboBox.setItemText(0, QCoreApplication.translate("addpatientinfopage", u"male", None))
        self.sex_comboBox.setItemText(1, QCoreApplication.translate("addpatientinfopage", u"female", None))

        self.edu_comboBox.setItemText(0, QCoreApplication.translate("addpatientinfopage", u"undergraduate", None))
        self.edu_comboBox.setItemText(1, QCoreApplication.translate("addpatientinfopage", u"graduate", None))
        self.edu_comboBox.setItemText(2, QCoreApplication.translate("addpatientinfopage", u"postgraduate", None))
        self.edu_comboBox.setItemText(3, QCoreApplication.translate("addpatientinfopage", u"phd", None))

        self.back_pushButton.setText(QCoreApplication.translate("addpatientinfopage", u"back", None))
        self.addpatientinfo_pushButton.setText(QCoreApplication.translate("addpatientinfopage", u"save", None))
    # retranslateUi

