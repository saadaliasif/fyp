from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_loginpage(object):
    def setupUi(self, loginpage):
        if not loginpage.objectName():
            loginpage.setObjectName(u"loginpage")
        loginpage.resize(865, 550)
        self.groupBox = QGroupBox(loginpage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 30, 691, 441))
        self.groupBox.setStyleSheet("QGroupBox { border: 0px solid; }")
        self.signin_label = QLabel(self.groupBox)
        self.signin_label.setObjectName(u"signin_label")
        self.signin_label.setGeometry(QRect(270, 40, 121, 51))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(24)
        self.signin_label.setFont(font)
        self.signin_pushButton = QPushButton(self.groupBox)
        self.signin_pushButton.setObjectName(u"signin_pushButton")
        self.signin_pushButton.setGeometry(QRect(210, 310, 271, 41))
        self.forgot_password_label = QLabel(self.groupBox)
        self.forgot_password_label.setObjectName(u"forgot_password_label")
        self.forgot_password_label.setGeometry(QRect(380, 360, 111, 16))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(210, 90, 271, 101))
        self.groupBox_2.setStyleSheet("QGroupBox { border: 0px solid; }")
        self.username_lineEdit = QLineEdit(self.groupBox_2)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(10, 50, 251, 31))
        self.username_label = QLabel(self.groupBox_2)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(10, 20, 81, 16))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(210, 180, 271, 121))
        self.groupBox_3.setStyleSheet("QGroupBox { border: 0px solid; }")
        self.password_label = QLabel(self.groupBox_3)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(10, 20, 91, 16))
        self.password_lineEdit = QLineEdit(self.groupBox_3)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(10, 40, 251, 31))
        self.remember_me_checkBox = QCheckBox(self.groupBox_3)
        self.remember_me_checkBox.setObjectName(u"remember_me_checkBox")
        self.remember_me_checkBox.setGeometry(QRect(10, 80, 141, 20))

        self.retranslateUi(loginpage)

        QMetaObject.connectSlotsByName(loginpage)
    # setupUi

    def retranslateUi(self, loginpage):
        loginpage.setWindowTitle(QCoreApplication.translate("loginpage", u"loginpage", None))
        self.groupBox.setTitle(QCoreApplication.translate("loginpage", u"", None))
        self.signin_label.setText(QCoreApplication.translate("loginpage", u"SignIn", None))
        self.signin_pushButton.setText(QCoreApplication.translate("loginpage", u"SignIn", None))
        self.forgot_password_label.setText(QCoreApplication.translate("loginpage", u"Forgot Password?", None))
        self.groupBox_2.setTitle("")
        self.username_label.setText(QCoreApplication.translate("loginpage", u"Username:", None))
        self.groupBox_3.setTitle("")
        self.password_label.setText(QCoreApplication.translate("loginpage", u"Password:", None))
        self.remember_me_checkBox.setText(QCoreApplication.translate("loginpage", u"Remember me?", None))
    # retranslateUi

