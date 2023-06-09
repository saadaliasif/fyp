from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_remarkspage(object):
    def setupUi(self, remarkspage):
        if not remarkspage.objectName():
            remarkspage.setObjectName(u"remarkspage")
        remarkspage.resize(1124, 698)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(12)
        remarkspage.setFont(font)
        self.widget = QWidget(remarkspage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(230, 40, 581, 531))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.diagnosisheading_label = QLabel(self.widget)
        self.diagnosisheading_label.setObjectName(u"diagnosisheading_label")
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.diagnosisheading_label.setFont(font1)

        self.horizontalLayout.addWidget(self.diagnosisheading_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.predout_label = QLabel(self.widget)
        self.predout_label.setObjectName(u"predout_label")

        self.horizontalLayout_2.addWidget(self.predout_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.prescreption_label = QLabel(self.widget)
        self.prescreption_label.setObjectName(u"prescreption_label")
        font2 = QFont()
        font2.setPointSize(14)
        self.prescreption_label.setFont(font2)

        self.verticalLayout.addWidget(self.prescreption_label)

        self.remarks_textEdit = QTextEdit(self.widget)
        self.remarks_textEdit.setObjectName(u"remarks_textEdit")

        self.verticalLayout.addWidget(self.remarks_textEdit)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.back_pushButton = QPushButton(self.widget)
        self.back_pushButton.setObjectName(u"back_pushButton")
        font3 = QFont()
        font3.setFamilies([u"MV Boli"])
        font3.setPointSize(14)
        self.back_pushButton.setFont(font3)

        self.horizontalLayout_3.addWidget(self.back_pushButton)

        self.save_pushButton = QPushButton(self.widget)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setFont(font3)

        self.horizontalLayout_3.addWidget(self.save_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 2)

        self.retranslateUi(remarkspage)

        QMetaObject.connectSlotsByName(remarkspage)
    # setupUi

    def retranslateUi(self, remarkspage):
        remarkspage.setWindowTitle(QCoreApplication.translate("remarkspage", u"Form", None))
        self.diagnosisheading_label.setText(QCoreApplication.translate("remarkspage", u"Diagnosis", None))
        self.predout_label.setText(QCoreApplication.translate("remarkspage", u"abc", None))
        self.prescreption_label.setText(QCoreApplication.translate("remarkspage", u"prescription:", None))
        self.back_pushButton.setText(QCoreApplication.translate("remarkspage", u"back", None))
        self.save_pushButton.setText(QCoreApplication.translate("remarkspage", u"save", None))
    # retranslateUi

