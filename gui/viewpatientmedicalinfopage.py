# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewpatientmedicalinfopage.ui'
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

class Ui_viewpatientmedicalinfopage(object):
    def setupUi(self, viewpatientmedicalinfopage):
        if not viewpatientmedicalinfopage.objectName():
            viewpatientmedicalinfopage.setObjectName(u"viewpatientmedicalinfopage")
        viewpatientmedicalinfopage.resize(1121, 843)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        viewpatientmedicalinfopage.setFont(font)
        self.viewpatientmedicalinfo_label = QLabel(viewpatientmedicalinfopage)
        self.viewpatientmedicalinfo_label.setObjectName(u"viewpatientmedicalinfo_label")
        self.viewpatientmedicalinfo_label.setGeometry(QRect(320, 10, 501, 52))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.viewpatientmedicalinfo_label.setFont(font1)
        self.layoutWidget = QWidget(viewpatientmedicalinfopage)
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

        self.layoutWidget1 = QWidget(viewpatientmedicalinfopage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(90, 80, 971, 631))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.phyact_out_label = QLabel(self.layoutWidget1)
        self.phyact_out_label.setObjectName(u"phyact_out_label")

        self.gridLayout.addWidget(self.phyact_out_label, 7, 1, 1, 1)

        self.fruit_out_label = QLabel(self.layoutWidget1)
        self.fruit_out_label.setObjectName(u"fruit_out_label")

        self.gridLayout.addWidget(self.fruit_out_label, 8, 1, 1, 1)

        self.veg_out_label = QLabel(self.layoutWidget1)
        self.veg_out_label.setObjectName(u"veg_out_label")

        self.gridLayout.addWidget(self.veg_out_label, 9, 1, 1, 1)

        self.bmi_out_label = QLabel(self.layoutWidget1)
        self.bmi_out_label.setObjectName(u"bmi_out_label")

        self.gridLayout.addWidget(self.bmi_out_label, 3, 1, 1, 1)

        self.heavyalcholcons_out_label = QLabel(self.layoutWidget1)
        self.heavyalcholcons_out_label.setObjectName(u"heavyalcholcons_out_label")

        self.gridLayout.addWidget(self.heavyalcholcons_out_label, 10, 1, 1, 1)

        self.fruit_label = QLabel(self.layoutWidget1)
        self.fruit_label.setObjectName(u"fruit_label")

        self.gridLayout.addWidget(self.fruit_label, 8, 0, 1, 1)

        self.smoker_label = QLabel(self.layoutWidget1)
        self.smoker_label.setObjectName(u"smoker_label")

        self.gridLayout.addWidget(self.smoker_label, 4, 0, 1, 1)

        self.cholcheck_out_label = QLabel(self.layoutWidget1)
        self.cholcheck_out_label.setObjectName(u"cholcheck_out_label")

        self.gridLayout.addWidget(self.cholcheck_out_label, 2, 1, 1, 1)

        self.bmi_label = QLabel(self.layoutWidget1)
        self.bmi_label.setObjectName(u"bmi_label")

        self.gridLayout.addWidget(self.bmi_label, 3, 0, 1, 1)

        self.stroke_out_label = QLabel(self.layoutWidget1)
        self.stroke_out_label.setObjectName(u"stroke_out_label")

        self.gridLayout.addWidget(self.stroke_out_label, 5, 1, 1, 1)

        self.veg_label = QLabel(self.layoutWidget1)
        self.veg_label.setObjectName(u"veg_label")

        self.gridLayout.addWidget(self.veg_label, 9, 0, 1, 1)

        self.heavyalcholcons_label = QLabel(self.layoutWidget1)
        self.heavyalcholcons_label.setObjectName(u"heavyalcholcons_label")

        self.gridLayout.addWidget(self.heavyalcholcons_label, 10, 0, 1, 1)

        self.cholcheck_label = QLabel(self.layoutWidget1)
        self.cholcheck_label.setObjectName(u"cholcheck_label")

        self.gridLayout.addWidget(self.cholcheck_label, 2, 0, 1, 1)

        self.highchol_label = QLabel(self.layoutWidget1)
        self.highchol_label.setObjectName(u"highchol_label")

        self.gridLayout.addWidget(self.highchol_label, 1, 0, 1, 1)

        self.stroke_label = QLabel(self.layoutWidget1)
        self.stroke_label.setObjectName(u"stroke_label")

        self.gridLayout.addWidget(self.stroke_label, 5, 0, 1, 1)

        self.smoker_out_label = QLabel(self.layoutWidget1)
        self.smoker_out_label.setObjectName(u"smoker_out_label")

        self.gridLayout.addWidget(self.smoker_out_label, 4, 1, 1, 1)

        self.phyact_label = QLabel(self.layoutWidget1)
        self.phyact_label.setObjectName(u"phyact_label")

        self.gridLayout.addWidget(self.phyact_label, 7, 0, 1, 1)

        self.heartdis_out_label = QLabel(self.layoutWidget1)
        self.heartdis_out_label.setObjectName(u"heartdis_out_label")

        self.gridLayout.addWidget(self.heartdis_out_label, 6, 1, 1, 1)

        self.highchol_out_label = QLabel(self.layoutWidget1)
        self.highchol_out_label.setObjectName(u"highchol_out_label")

        self.gridLayout.addWidget(self.highchol_out_label, 1, 1, 1, 1)

        self.anyhealthcare_label = QLabel(self.layoutWidget1)
        self.anyhealthcare_label.setObjectName(u"anyhealthcare_label")

        self.gridLayout.addWidget(self.anyhealthcare_label, 11, 0, 1, 1)

        self.menhelth_label = QLabel(self.layoutWidget1)
        self.menhelth_label.setObjectName(u"menhelth_label")

        self.gridLayout.addWidget(self.menhelth_label, 15, 0, 1, 1)

        self.menhelth_out_label = QLabel(self.layoutWidget1)
        self.menhelth_out_label.setObjectName(u"menhelth_out_label")

        self.gridLayout.addWidget(self.menhelth_out_label, 15, 1, 1, 1)

        self.nodocbcost_out_label = QLabel(self.layoutWidget1)
        self.nodocbcost_out_label.setObjectName(u"nodocbcost_out_label")

        self.gridLayout.addWidget(self.nodocbcost_out_label, 12, 1, 1, 1)

        self.phyhelth_out_label = QLabel(self.layoutWidget1)
        self.phyhelth_out_label.setObjectName(u"phyhelth_out_label")

        self.gridLayout.addWidget(self.phyhelth_out_label, 14, 1, 1, 1)

        self.genhelth_label = QLabel(self.layoutWidget1)
        self.genhelth_label.setObjectName(u"genhelth_label")

        self.gridLayout.addWidget(self.genhelth_label, 13, 0, 1, 1)

        self.phyhelth_label = QLabel(self.layoutWidget1)
        self.phyhelth_label.setObjectName(u"phyhelth_label")

        self.gridLayout.addWidget(self.phyhelth_label, 14, 0, 1, 1)

        self.nodocbccost_label = QLabel(self.layoutWidget1)
        self.nodocbccost_label.setObjectName(u"nodocbccost_label")

        self.gridLayout.addWidget(self.nodocbccost_label, 12, 0, 1, 1)

        self.anyhealthcare_out_label = QLabel(self.layoutWidget1)
        self.anyhealthcare_out_label.setObjectName(u"anyhealthcare_out_label")

        self.gridLayout.addWidget(self.anyhealthcare_out_label, 11, 1, 1, 1)

        self.highbp_out_label = QLabel(self.layoutWidget1)
        self.highbp_out_label.setObjectName(u"highbp_out_label")

        self.gridLayout.addWidget(self.highbp_out_label, 0, 1, 1, 1)

        self.highbp_label = QLabel(self.layoutWidget1)
        self.highbp_label.setObjectName(u"highbp_label")

        self.gridLayout.addWidget(self.highbp_label, 0, 0, 1, 1)

        self.heartdis_label = QLabel(self.layoutWidget1)
        self.heartdis_label.setObjectName(u"heartdis_label")

        self.gridLayout.addWidget(self.heartdis_label, 6, 0, 1, 1)

        self.genhelth_out_label = QLabel(self.layoutWidget1)
        self.genhelth_out_label.setObjectName(u"genhelth_out_label")

        self.gridLayout.addWidget(self.genhelth_out_label, 13, 1, 1, 1)

        self.diffwalk_label = QLabel(self.layoutWidget1)
        self.diffwalk_label.setObjectName(u"diffwalk_label")

        self.gridLayout.addWidget(self.diffwalk_label, 16, 0, 1, 1)

        self.diffwalk_out_label = QLabel(self.layoutWidget1)
        self.diffwalk_out_label.setObjectName(u"diffwalk_out_label")

        self.gridLayout.addWidget(self.diffwalk_out_label, 16, 1, 1, 1)


        self.retranslateUi(viewpatientmedicalinfopage)

        QMetaObject.connectSlotsByName(viewpatientmedicalinfopage)
    # setupUi

    def retranslateUi(self, viewpatientmedicalinfopage):
        viewpatientmedicalinfopage.setWindowTitle(QCoreApplication.translate("viewpatientmedicalinfopage", u"Form", None))
        self.viewpatientmedicalinfo_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"View Patient Medical Info", None))
        self.back_pushButton.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Back", None))
        self.delete_pushButton.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"delete", None))
        self.edit_pushButton.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Edit", None))
        self.phyact_out_label.setText("")
        self.fruit_out_label.setText("")
        self.veg_out_label.setText("")
        self.bmi_out_label.setText("")
        self.heavyalcholcons_out_label.setText("")
        self.fruit_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Fruits:", None))
        self.smoker_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Smoker:", None))
        self.cholcheck_out_label.setText("")
        self.bmi_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"BMI:", None))
        self.stroke_out_label.setText("")
        self.veg_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"vegetables:", None))
        self.heavyalcholcons_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Heavy Alcohol Consumption:", None))
        self.cholcheck_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Cholestrol check:", None))
        self.highchol_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"High cholestrol:", None))
        self.stroke_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Stroke:", None))
        self.smoker_out_label.setText("")
        self.phyact_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Physical Activity:", None))
        self.heartdis_out_label.setText("")
        self.highchol_out_label.setText("")
        self.anyhealthcare_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Any healthcare:", None))
        self.menhelth_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"mental health:", None))
        self.menhelth_out_label.setText("")
        self.nodocbcost_out_label.setText("")
        self.phyhelth_out_label.setText("")
        self.genhelth_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"general health:", None))
        self.phyhelth_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"physical health:", None))
        self.nodocbccost_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"No doctor because of cost:", None))
        self.anyhealthcare_out_label.setText("")
        self.highbp_out_label.setText("")
        self.highbp_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"High bp:", None))
        self.heartdis_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"Heart Disease:", None))
        self.genhelth_out_label.setText("")
        self.diffwalk_label.setText(QCoreApplication.translate("viewpatientmedicalinfopage", u"diffwalk", None))
        self.diffwalk_out_label.setText("")
    # retranslateUi

