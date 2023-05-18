# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addpatientmedicalinfopage.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_addpatientmedicalinfopage(object):
    def setupUi(self, addpatientmedicalinfopage):
        if not addpatientmedicalinfopage.objectName():
            addpatientmedicalinfopage.setObjectName(u"addpatientmedicalinfopage")
        addpatientmedicalinfopage.resize(1121, 843)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        addpatientmedicalinfopage.setFont(font)
        self.verticalLayout = QVBoxLayout(addpatientmedicalinfopage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addpatientmedicalinfo_label = QLabel(addpatientmedicalinfopage)
        self.addpatientmedicalinfo_label.setObjectName(u"addpatientmedicalinfo_label")
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.addpatientmedicalinfo_label.setFont(font1)

        self.verticalLayout.addWidget(self.addpatientmedicalinfo_label)

        self.scrollArea = QScrollArea(addpatientmedicalinfopage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1076, 1604))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.HIGHBP_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.HIGHBP_groupBox.setObjectName(u"HIGHBP_groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.HIGHBP_groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.thbp_radioButton = QRadioButton(self.HIGHBP_groupBox)
        self.thbp_radioButton.setObjectName(u"thbp_radioButton")

        self.horizontalLayout_2.addWidget(self.thbp_radioButton)

        self.fhbp_radioButton = QRadioButton(self.HIGHBP_groupBox)
        self.fhbp_radioButton.setObjectName(u"fhbp_radioButton")

        self.horizontalLayout_2.addWidget(self.fhbp_radioButton)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_17)


        self.verticalLayout_2.addWidget(self.HIGHBP_groupBox)

        self.bmi_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.bmi_groupBox.setObjectName(u"bmi_groupBox")
        self.horizontalLayout = QHBoxLayout(self.bmi_groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bmi_lineEdit = QLineEdit(self.bmi_groupBox)
        self.bmi_lineEdit.setObjectName(u"bmi_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bmi_lineEdit.sizePolicy().hasHeightForWidth())
        self.bmi_lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.bmi_lineEdit)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_16)


        self.verticalLayout_2.addWidget(self.bmi_groupBox)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tcc_radioButton = QRadioButton(self.groupBox_4)
        self.tcc_radioButton.setObjectName(u"tcc_radioButton")

        self.horizontalLayout_4.addWidget(self.tcc_radioButton)

        self.fcc_radioButton = QRadioButton(self.groupBox_4)
        self.fcc_radioButton.setObjectName(u"fcc_radioButton")

        self.horizontalLayout_4.addWidget(self.fcc_radioButton)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.thc_radioButton = QRadioButton(self.groupBox_3)
        self.thc_radioButton.setObjectName(u"thc_radioButton")

        self.horizontalLayout_3.addWidget(self.thc_radioButton)

        self.fhc_radioButton = QRadioButton(self.groupBox_3)
        self.fhc_radioButton.setObjectName(u"fhc_radioButton")

        self.horizontalLayout_3.addWidget(self.fhc_radioButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tstroke_radioButton = QRadioButton(self.groupBox_6)
        self.tstroke_radioButton.setObjectName(u"tstroke_radioButton")

        self.horizontalLayout_6.addWidget(self.tstroke_radioButton)

        self.fstroke_radioButton = QRadioButton(self.groupBox_6)
        self.fstroke_radioButton.setObjectName(u"fstroke_radioButton")

        self.horizontalLayout_6.addWidget(self.fstroke_radioButton)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ts_radioButton = QRadioButton(self.groupBox_5)
        self.ts_radioButton.setObjectName(u"ts_radioButton")

        self.horizontalLayout_5.addWidget(self.ts_radioButton)

        self.fs_radioButton = QRadioButton(self.groupBox_5)
        self.fs_radioButton.setObjectName(u"fs_radioButton")

        self.horizontalLayout_5.addWidget(self.fs_radioButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tpa_radioButton = QRadioButton(self.groupBox_8)
        self.tpa_radioButton.setObjectName(u"tpa_radioButton")

        self.horizontalLayout_8.addWidget(self.tpa_radioButton)

        self.fpa_radioButton = QRadioButton(self.groupBox_8)
        self.fpa_radioButton.setObjectName(u"fpa_radioButton")

        self.horizontalLayout_8.addWidget(self.fpa_radioButton)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.thd_radioButton = QRadioButton(self.groupBox_7)
        self.thd_radioButton.setObjectName(u"thd_radioButton")

        self.horizontalLayout_7.addWidget(self.thd_radioButton)

        self.fhd_radioButton = QRadioButton(self.groupBox_7)
        self.fhd_radioButton.setObjectName(u"fhd_radioButton")

        self.horizontalLayout_7.addWidget(self.fhd_radioButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tv_radioButton = QRadioButton(self.groupBox_2)
        self.tv_radioButton.setObjectName(u"tv_radioButton")

        self.horizontalLayout_10.addWidget(self.tv_radioButton)

        self.fv_radioButton = QRadioButton(self.groupBox_2)
        self.fv_radioButton.setObjectName(u"fv_radioButton")

        self.horizontalLayout_10.addWidget(self.fv_radioButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tf_radioButton = QRadioButton(self.groupBox)
        self.tf_radioButton.setObjectName(u"tf_radioButton")

        self.horizontalLayout_9.addWidget(self.tf_radioButton)

        self.ff_radioButton = QRadioButton(self.groupBox)
        self.ff_radioButton.setObjectName(u"ff_radioButton")

        self.horizontalLayout_9.addWidget(self.ff_radioButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tah_radioButton = QRadioButton(self.groupBox_10)
        self.tah_radioButton.setObjectName(u"tah_radioButton")

        self.horizontalLayout_12.addWidget(self.tah_radioButton)

        self.fah_radioButton = QRadioButton(self.groupBox_10)
        self.fah_radioButton.setObjectName(u"fah_radioButton")

        self.horizontalLayout_12.addWidget(self.fah_radioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.thac_radioButton = QRadioButton(self.groupBox_9)
        self.thac_radioButton.setObjectName(u"thac_radioButton")

        self.horizontalLayout_11.addWidget(self.thac_radioButton)

        self.fhac_radioButton = QRadioButton(self.groupBox_9)
        self.fhac_radioButton.setObjectName(u"fhac_radioButton")

        self.horizontalLayout_11.addWidget(self.fhac_radioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.genhealth_lineEdit = QLineEdit(self.groupBox_12)
        self.genhealth_lineEdit.setObjectName(u"genhealth_lineEdit")
        sizePolicy.setHeightForWidth(self.genhealth_lineEdit.sizePolicy().hasHeightForWidth())
        self.genhealth_lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.genhealth_lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox_12)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tndboc_radioButton = QRadioButton(self.groupBox_11)
        self.tndboc_radioButton.setObjectName(u"tndboc_radioButton")

        self.horizontalLayout_13.addWidget(self.tndboc_radioButton)

        self.fndboc_radioButton = QRadioButton(self.groupBox_11)
        self.fndboc_radioButton.setObjectName(u"fndboc_radioButton")

        self.horizontalLayout_13.addWidget(self.fndboc_radioButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.groupBox_11)

        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.physhealth_lineEdit = QLineEdit(self.groupBox_14)
        self.physhealth_lineEdit.setObjectName(u"physhealth_lineEdit")
        sizePolicy.setHeightForWidth(self.physhealth_lineEdit.sizePolicy().hasHeightForWidth())
        self.physhealth_lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.physhealth_lineEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.groupBox_14)

        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.menhealth_lineEdit = QLineEdit(self.groupBox_13)
        self.menhealth_lineEdit.setObjectName(u"menhealth_lineEdit")
        sizePolicy.setHeightForWidth(self.menhealth_lineEdit.sizePolicy().hasHeightForWidth())
        self.menhealth_lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.menhealth_lineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.groupBox_13)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.td_radioButton = QRadioButton(self.groupBox_15)
        self.td_radioButton.setObjectName(u"td_radioButton")

        self.horizontalLayout_17.addWidget(self.td_radioButton)

        self.fd_radioButton = QRadioButton(self.groupBox_15)
        self.fd_radioButton.setObjectName(u"fd_radioButton")

        self.horizontalLayout_17.addWidget(self.fd_radioButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.groupBox_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.addpatientmedicalinfo_pushButton = QPushButton(addpatientmedicalinfopage)
        self.addpatientmedicalinfo_pushButton.setObjectName(u"addpatientmedicalinfo_pushButton")

        self.verticalLayout.addWidget(self.addpatientmedicalinfo_pushButton)


        self.retranslateUi(addpatientmedicalinfopage)

        QMetaObject.connectSlotsByName(addpatientmedicalinfopage)
    # setupUi

    def retranslateUi(self, addpatientmedicalinfopage):
        addpatientmedicalinfopage.setWindowTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"Form", None))
        self.addpatientmedicalinfo_label.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"Add Patient Medical Info", None))
        self.HIGHBP_groupBox.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"HIGH BLOOD PRESURE:", None))
        self.thbp_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fhbp_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.bmi_groupBox.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"BMI:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"CHOLESTROL CHECK:", None))
        self.tcc_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fcc_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"HIGH CHOLESTROL:", None))
        self.thc_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fhc_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"STROKE:", None))
        self.tstroke_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fstroke_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"SMOKER:", None))
        self.ts_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fs_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"PHYSICAL ACTIVITY:", None))
        self.tpa_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fpa_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"HEART DISEASE:", None))
        self.thd_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fhd_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"VEGETABLES:", None))
        self.tv_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fv_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"FRUITS:", None))
        self.tf_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.ff_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"ANY HEALTHCARE:", None))
        self.tah_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fah_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"HEAVY ALCOHOL CONSUMPTION:", None))
        self.thac_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fhac_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"GENERAL HEALTH", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"NO DOC BECAUSE OF COST:", None))
        self.tndboc_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fndboc_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"PHYSICAL HEALTH", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"MENTAL HEALTH", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("addpatientmedicalinfopage", u"DIFFWALK", None))
        self.td_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"TRUE", None))
        self.fd_radioButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"FALSE", None))
        self.addpatientmedicalinfo_pushButton.setText(QCoreApplication.translate("addpatientmedicalinfopage", u"Submit", None))
    # retranslateUi

