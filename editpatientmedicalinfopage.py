# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editpatientmedicalinfopage.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_editpatientmedicalinfopage(object):
    def setupUi(self, editpatientmedicalinfopage):
        if not editpatientmedicalinfopage.objectName():
            editpatientmedicalinfopage.setObjectName(u"editpatientmedicalinfopage")
        editpatientmedicalinfopage.resize(1121, 833)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        editpatientmedicalinfopage.setFont(font)
        self.editpatientmedicalinfo_label = QLabel(editpatientmedicalinfopage)
        self.editpatientmedicalinfo_label.setObjectName(u"editpatientmedicalinfo_label")
        self.editpatientmedicalinfo_label.setGeometry(QRect(320, 10, 501, 52))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.editpatientmedicalinfo_label.setFont(font1)
        self.widget = QWidget(editpatientmedicalinfopage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 60, 971, 691))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.fruit_label = QLabel(self.widget)
        self.fruit_label.setObjectName(u"fruit_label")

        self.gridLayout.addWidget(self.fruit_label, 8, 0, 1, 1)

        self.smoker_label = QLabel(self.widget)
        self.smoker_label.setObjectName(u"smoker_label")

        self.gridLayout.addWidget(self.smoker_label, 4, 0, 1, 1)

        self.bmi_label = QLabel(self.widget)
        self.bmi_label.setObjectName(u"bmi_label")

        self.gridLayout.addWidget(self.bmi_label, 3, 0, 1, 1)

        self.veg_label = QLabel(self.widget)
        self.veg_label.setObjectName(u"veg_label")

        self.gridLayout.addWidget(self.veg_label, 9, 0, 1, 1)

        self.heavyalcholcons_label = QLabel(self.widget)
        self.heavyalcholcons_label.setObjectName(u"heavyalcholcons_label")

        self.gridLayout.addWidget(self.heavyalcholcons_label, 10, 0, 1, 1)

        self.cholcheck_label = QLabel(self.widget)
        self.cholcheck_label.setObjectName(u"cholcheck_label")

        self.gridLayout.addWidget(self.cholcheck_label, 2, 0, 1, 1)

        self.highchol_label = QLabel(self.widget)
        self.highchol_label.setObjectName(u"highchol_label")

        self.gridLayout.addWidget(self.highchol_label, 1, 0, 1, 1)

        self.stroke_label = QLabel(self.widget)
        self.stroke_label.setObjectName(u"stroke_label")

        self.gridLayout.addWidget(self.stroke_label, 5, 0, 1, 1)

        self.phyact_label = QLabel(self.widget)
        self.phyact_label.setObjectName(u"phyact_label")

        self.gridLayout.addWidget(self.phyact_label, 7, 0, 1, 1)

        self.anyhealthcare_label = QLabel(self.widget)
        self.anyhealthcare_label.setObjectName(u"anyhealthcare_label")

        self.gridLayout.addWidget(self.anyhealthcare_label, 11, 0, 1, 1)

        self.menhelth_label = QLabel(self.widget)
        self.menhelth_label.setObjectName(u"menhelth_label")

        self.gridLayout.addWidget(self.menhelth_label, 15, 0, 1, 1)

        self.diffwalk_label = QLabel(self.widget)
        self.diffwalk_label.setObjectName(u"diffwalk_label")

        self.gridLayout.addWidget(self.diffwalk_label, 16, 0, 1, 1)

        self.phyhelth_lineEdit = QLineEdit(self.widget)
        self.phyhelth_lineEdit.setObjectName(u"phyhelth_lineEdit")

        self.gridLayout.addWidget(self.phyhelth_lineEdit, 14, 1, 1, 1)

        self.highbp_lineEdit = QLineEdit(self.widget)
        self.highbp_lineEdit.setObjectName(u"highbp_lineEdit")

        self.gridLayout.addWidget(self.highbp_lineEdit, 0, 1, 1, 1)

        self.diffwalk_lineEdit = QLineEdit(self.widget)
        self.diffwalk_lineEdit.setObjectName(u"diffwalk_lineEdit")

        self.gridLayout.addWidget(self.diffwalk_lineEdit, 16, 1, 1, 1)

        self.highchol_lineEdit = QLineEdit(self.widget)
        self.highchol_lineEdit.setObjectName(u"highchol_lineEdit")

        self.gridLayout.addWidget(self.highchol_lineEdit, 1, 1, 1, 1)

        self.fruit_lineEdit = QLineEdit(self.widget)
        self.fruit_lineEdit.setObjectName(u"fruit_lineEdit")

        self.gridLayout.addWidget(self.fruit_lineEdit, 8, 1, 1, 1)

        self.heavyalcholcons_lineEdit = QLineEdit(self.widget)
        self.heavyalcholcons_lineEdit.setObjectName(u"heavyalcholcons_lineEdit")

        self.gridLayout.addWidget(self.heavyalcholcons_lineEdit, 10, 1, 1, 1)

        self.vegitable_lineEdit = QLineEdit(self.widget)
        self.vegitable_lineEdit.setObjectName(u"vegitable_lineEdit")

        self.gridLayout.addWidget(self.vegitable_lineEdit, 9, 1, 1, 1)

        self.anyhealthcare_lineEdit = QLineEdit(self.widget)
        self.anyhealthcare_lineEdit.setObjectName(u"anyhealthcare_lineEdit")

        self.gridLayout.addWidget(self.anyhealthcare_lineEdit, 11, 1, 1, 1)

        self.genhelth_lineEdit = QLineEdit(self.widget)
        self.genhelth_lineEdit.setObjectName(u"genhelth_lineEdit")

        self.gridLayout.addWidget(self.genhelth_lineEdit, 13, 1, 1, 1)

        self.nocostbcdoc_lineEdit = QLineEdit(self.widget)
        self.nocostbcdoc_lineEdit.setObjectName(u"nocostbcdoc_lineEdit")

        self.gridLayout.addWidget(self.nocostbcdoc_lineEdit, 12, 1, 1, 1)

        self.genhelth_label = QLabel(self.widget)
        self.genhelth_label.setObjectName(u"genhelth_label")

        self.gridLayout.addWidget(self.genhelth_label, 13, 0, 1, 1)

        self.phyhelth_label = QLabel(self.widget)
        self.phyhelth_label.setObjectName(u"phyhelth_label")

        self.gridLayout.addWidget(self.phyhelth_label, 14, 0, 1, 1)

        self.menhelth_lineEdit = QLineEdit(self.widget)
        self.menhelth_lineEdit.setObjectName(u"menhelth_lineEdit")

        self.gridLayout.addWidget(self.menhelth_lineEdit, 15, 1, 1, 1)

        self.nodocbccost_label = QLabel(self.widget)
        self.nodocbccost_label.setObjectName(u"nodocbccost_label")

        self.gridLayout.addWidget(self.nodocbccost_label, 12, 0, 1, 1)

        self.highbp_label = QLabel(self.widget)
        self.highbp_label.setObjectName(u"highbp_label")

        self.gridLayout.addWidget(self.highbp_label, 0, 0, 1, 1)

        self.heartdis_label = QLabel(self.widget)
        self.heartdis_label.setObjectName(u"heartdis_label")

        self.gridLayout.addWidget(self.heartdis_label, 6, 0, 1, 1)

        self.bmi_lineEdit = QLineEdit(self.widget)
        self.bmi_lineEdit.setObjectName(u"bmi_lineEdit")

        self.gridLayout.addWidget(self.bmi_lineEdit, 3, 1, 1, 1)

        self.cholcheck_lineEdit = QLineEdit(self.widget)
        self.cholcheck_lineEdit.setObjectName(u"cholcheck_lineEdit")

        self.gridLayout.addWidget(self.cholcheck_lineEdit, 2, 1, 1, 1)

        self.smoker_lineEdit = QLineEdit(self.widget)
        self.smoker_lineEdit.setObjectName(u"smoker_lineEdit")

        self.gridLayout.addWidget(self.smoker_lineEdit, 4, 1, 1, 1)

        self.stroke_lineEdit = QLineEdit(self.widget)
        self.stroke_lineEdit.setObjectName(u"stroke_lineEdit")

        self.gridLayout.addWidget(self.stroke_lineEdit, 5, 1, 1, 1)

        self.heartdisese__lineEdit = QLineEdit(self.widget)
        self.heartdisese__lineEdit.setObjectName(u"heartdisese__lineEdit")

        self.gridLayout.addWidget(self.heartdisese__lineEdit, 6, 1, 1, 1)

        self.phyact_lineEdit = QLineEdit(self.widget)
        self.phyact_lineEdit.setObjectName(u"phyact_lineEdit")

        self.gridLayout.addWidget(self.phyact_lineEdit, 7, 1, 1, 1)

        self.widget1 = QWidget(editpatientmedicalinfopage)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(800, 760, 261, 61))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.back_pushButton = QPushButton(self.widget1)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.horizontalLayout.addWidget(self.back_pushButton)

        self.save_pushButton = QPushButton(self.widget1)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.horizontalLayout.addWidget(self.save_pushButton)


        self.retranslateUi(editpatientmedicalinfopage)

        QMetaObject.connectSlotsByName(editpatientmedicalinfopage)
    # setupUi

    def retranslateUi(self, editpatientmedicalinfopage):
        editpatientmedicalinfopage.setWindowTitle(QCoreApplication.translate("editpatientmedicalinfopage", u"Form", None))
        self.editpatientmedicalinfo_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Edit Patient Medical Info", None))
        self.fruit_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Fruits:", None))
        self.smoker_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Smoker:", None))
        self.bmi_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"BMI:", None))
        self.veg_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"vegetables:", None))
        self.heavyalcholcons_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Heavy Alcohol Consumption:", None))
        self.cholcheck_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Cholestrol check:", None))
        self.highchol_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"High cholestrol:", None))
        self.stroke_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Stroke:", None))
        self.phyact_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Physical Activity:", None))
        self.anyhealthcare_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Any healthcare:", None))
        self.menhelth_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"mental health:", None))
        self.diffwalk_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"diffwalk", None))
        self.genhelth_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"general health:", None))
        self.phyhelth_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"physical health:", None))
        self.nodocbccost_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"No doctor because of cost:", None))
        self.highbp_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"High bp:", None))
        self.heartdis_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Heart Disease:", None))
        self.back_pushButton.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Back", None))
        self.save_pushButton.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Save", None))
    # retranslateUi

