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

class Ui_signuppage(object):
    def setupUi(self, signuppage):
        if not signuppage.objectName():
            signuppage.setObjectName(u"signuppage")
        signuppage.resize(908, 815)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        signuppage.setFont(font)
        self.verticalLayout = QVBoxLayout(signuppage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signup_label = QLabel(signuppage)
        self.signup_label.setObjectName(u"signup_label")
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.signup_label.setFont(font1)
        self.signup_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.signup_label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setHorizontalSpacing(69)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.first_name_label = QLabel(signuppage)
        self.first_name_label.setObjectName(u"first_name_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.first_name_label)

        self.first_name_lineEdit = QLineEdit(signuppage)
        self.first_name_lineEdit.setObjectName(u"first_name_lineEdit")
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.first_name_lineEdit.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.first_name_lineEdit)

        self.last_name_label = QLabel(signuppage)
        self.last_name_label.setObjectName(u"last_name_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.last_name_label)

        self.last_name_lineEdit = QLineEdit(signuppage)
        self.last_name_lineEdit.setObjectName(u"last_name_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.last_name_lineEdit)

        self.age_label = QLabel(signuppage)
        self.age_label.setObjectName(u"age_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.age_label)

        self.age_lineEdit = QLineEdit(signuppage)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.age_lineEdit)

        self.sex_label = QLabel(signuppage)
        self.sex_label.setObjectName(u"sex_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sex_label)

        self.phone_label = QLabel(signuppage)
        self.phone_label.setObjectName(u"phone_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.phone_label)

        self.phone_lineEdit = QLineEdit(signuppage)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.phone_lineEdit)

        self.education_label = QLabel(signuppage)
        self.education_label.setObjectName(u"education_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.education_label)

        self.income_label = QLabel(signuppage)
        self.income_label.setObjectName(u"income_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.income_label)

        self.income_lineEdit = QLineEdit(signuppage)
        self.income_lineEdit.setObjectName(u"income_lineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.income_lineEdit)

        self.city_label = QLabel(signuppage)
        self.city_label.setObjectName(u"city_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.city_label)

        self.country_label = QLabel(signuppage)
        self.country_label.setObjectName(u"country_label")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.country_label)

        self.email_label = QLabel(signuppage)
        self.email_label.setObjectName(u"email_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.email_label)

        self.email_lineEdit = QLineEdit(signuppage)
        self.email_lineEdit.setObjectName(u"email_lineEdit")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.email_lineEdit)

        self.username_label = QLabel(signuppage)
        self.username_label.setObjectName(u"username_label")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.username_label)

        self.username_lineEdit = QLineEdit(signuppage)
        self.username_lineEdit.setObjectName(u"username_lineEdit")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.username_lineEdit)

        self.password_label = QLabel(signuppage)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.password_label)

        self.password_lineEdit = QLineEdit(signuppage)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.password_lineEdit)

        self.confirm_password_lineEdit = QLineEdit(signuppage)
        self.confirm_password_lineEdit.setObjectName(u"confirm_password_lineEdit")
        self.confirm_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.confirm_password_lineEdit)

        self.confirm_password_label = QLabel(signuppage)
        self.confirm_password_label.setObjectName(u"confirm_password_label")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.confirm_password_label)

        self.postal_code_lineEdit = QLineEdit(signuppage)
        self.postal_code_lineEdit.setObjectName(u"postal_code_lineEdit")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.postal_code_lineEdit)

        self.postal_code_label = QLabel(signuppage)
        self.postal_code_label.setObjectName(u"postal_code_label")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.postal_code_label)

        self.sex_comboBox = QComboBox(signuppage)
        self.sex_comboBox.addItem("")
        self.sex_comboBox.addItem("")
        self.sex_comboBox.setObjectName(u"sex_comboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sex_comboBox)

        self.edu_comboBox = QComboBox(signuppage)
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.addItem("")
        self.edu_comboBox.setObjectName(u"edu_comboBox")
        self.edu_comboBox.setIconSize(QSize(50, 20))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.edu_comboBox)

        self.city_comboBox = QComboBox(signuppage)
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.setObjectName(u"city_comboBox")
        self.city_comboBox.setIconSize(QSize(40, 20))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.city_comboBox)

        self.country_comboBox = QComboBox(signuppage)
        self.country_comboBox.addItem("")
        self.country_comboBox.setObjectName(u"country_comboBox")
        self.country_comboBox.setIconSize(QSize(40, 20))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.country_comboBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.back_pushButton = QPushButton(signuppage)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.horizontalLayout.addWidget(self.back_pushButton)

        self.signup_pushButton = QPushButton(signuppage)
        self.signup_pushButton.setObjectName(u"signup_pushButton")

        self.horizontalLayout.addWidget(self.signup_pushButton)

        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(signuppage)

        QMetaObject.connectSlotsByName(signuppage)
    # setupUi

    def retranslateUi(self, signuppage):
        signuppage.setWindowTitle(QCoreApplication.translate("signuppage", u"Form", None))
        self.signup_label.setText(QCoreApplication.translate("signuppage", u"Registeration", None))
        self.first_name_label.setText(QCoreApplication.translate("signuppage", u"first name:", None))
        self.last_name_label.setText(QCoreApplication.translate("signuppage", u"last name:", None))
        self.age_label.setText(QCoreApplication.translate("signuppage", u"age:", None))
        self.sex_label.setText(QCoreApplication.translate("signuppage", u"sex:", None))
        self.phone_label.setText(QCoreApplication.translate("signuppage", u"phone:", None))
        self.education_label.setText(QCoreApplication.translate("signuppage", u"education:", None))
        self.income_label.setText(QCoreApplication.translate("signuppage", u"income:", None))
        self.city_label.setText(QCoreApplication.translate("signuppage", u"city:", None))
        self.country_label.setText(QCoreApplication.translate("signuppage", u"country:", None))
        self.email_label.setText(QCoreApplication.translate("signuppage", u"email", None))
        self.username_label.setText(QCoreApplication.translate("signuppage", u"username:", None))
        self.password_label.setText(QCoreApplication.translate("signuppage", u"password:", None))
        self.confirm_password_label.setText(QCoreApplication.translate("signuppage", u"confirm password:", None))
        self.postal_code_label.setText(QCoreApplication.translate("signuppage", u"postal code:", None))
        self.sex_comboBox.setItemText(0, QCoreApplication.translate("signuppage", u"male", None))
        self.sex_comboBox.setItemText(1, QCoreApplication.translate("signuppage", u"female", None))

        self.edu_comboBox.setItemText(0, QCoreApplication.translate("signuppage", u"undergraduate", None))
        self.edu_comboBox.setItemText(1, QCoreApplication.translate("signuppage", u"graduate", None))
        self.edu_comboBox.setItemText(2, QCoreApplication.translate("signuppage", u"postgraduate", None))
        self.edu_comboBox.setItemText(3, QCoreApplication.translate("signuppage", u"phd", None))

        self.city_comboBox.setItemText(0, QCoreApplication.translate("signuppage", u"islamabad", None))
        self.city_comboBox.setItemText(1, QCoreApplication.translate("signuppage", u"karachi", None))
        self.city_comboBox.setItemText(2, QCoreApplication.translate("signuppage", u"multan", None))
        self.city_comboBox.setItemText(3, QCoreApplication.translate("signuppage", u"lahore", None))
        self.city_comboBox.setItemText(4, QCoreApplication.translate("signuppage", u"gujranwala", None))
        self.city_comboBox.setItemText(5, QCoreApplication.translate("signuppage", u"peshawar", None))

        self.country_comboBox.setItemText(0, QCoreApplication.translate("signuppage", u"pakistan", None))

        self.back_pushButton.setText(QCoreApplication.translate("signuppage", u"Back", None))
        self.signup_pushButton.setText(QCoreApplication.translate("signuppage", u"SignUp", None))
    # retranslateUi

