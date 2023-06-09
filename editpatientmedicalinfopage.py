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

class Ui_editpatientmedicalinfopage(object):
    def setupUi(self, editpatientmedicalinfopage):
        if not editpatientmedicalinfopage.objectName():
            editpatientmedicalinfopage.setObjectName(u"editpatientmedicalinfopage")
        editpatientmedicalinfopage.resize(807, 838)
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        font.setBold(True)
        editpatientmedicalinfopage.setFont(font)
        self.verticalLayout = QVBoxLayout(editpatientmedicalinfopage)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 4, 7, 4)
        self.editpatientmedicalinfo_label = QLabel(editpatientmedicalinfopage)
        self.editpatientmedicalinfo_label.setObjectName(u"editpatientmedicalinfo_label")
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(22)
        self.editpatientmedicalinfo_label.setFont(font1)
        self.editpatientmedicalinfo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.editpatientmedicalinfo_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.highchol_label = QLabel(editpatientmedicalinfopage)
        self.highchol_label.setObjectName(u"highchol_label")

        self.gridLayout.addWidget(self.highchol_label, 1, 0, 1, 1)

        self.cholcheck_label = QLabel(editpatientmedicalinfopage)
        self.cholcheck_label.setObjectName(u"cholcheck_label")

        self.gridLayout.addWidget(self.cholcheck_label, 2, 0, 1, 1)

        self.bmi_label = QLabel(editpatientmedicalinfopage)
        self.bmi_label.setObjectName(u"bmi_label")

        self.gridLayout.addWidget(self.bmi_label, 3, 0, 1, 1)

        self.highbp_label = QLabel(editpatientmedicalinfopage)
        self.highbp_label.setObjectName(u"highbp_label")

        self.gridLayout.addWidget(self.highbp_label, 0, 0, 1, 1)

        self.hb_comboBox = QComboBox(editpatientmedicalinfopage)
        self.hb_comboBox.addItem("")
        self.hb_comboBox.addItem("")
        self.hb_comboBox.setObjectName(u"hb_comboBox")

        self.gridLayout.addWidget(self.hb_comboBox, 0, 1, 1, 1)

        self.bmi_lineEdit = QLineEdit(editpatientmedicalinfopage)
        self.bmi_lineEdit.setObjectName(u"bmi_lineEdit")

        self.gridLayout.addWidget(self.bmi_lineEdit, 3, 1, 1, 1)

        self.stroke_label = QLabel(editpatientmedicalinfopage)
        self.stroke_label.setObjectName(u"stroke_label")

        self.gridLayout.addWidget(self.stroke_label, 5, 0, 1, 1)

        self.smoker_label = QLabel(editpatientmedicalinfopage)
        self.smoker_label.setObjectName(u"smoker_label")

        self.gridLayout.addWidget(self.smoker_label, 4, 0, 1, 1)

        self.heartdis_label = QLabel(editpatientmedicalinfopage)
        self.heartdis_label.setObjectName(u"heartdis_label")

        self.gridLayout.addWidget(self.heartdis_label, 6, 0, 1, 1)

        self.phyact_label = QLabel(editpatientmedicalinfopage)
        self.phyact_label.setObjectName(u"phyact_label")

        self.gridLayout.addWidget(self.phyact_label, 7, 0, 1, 1)

        self.fruit_label = QLabel(editpatientmedicalinfopage)
        self.fruit_label.setObjectName(u"fruit_label")

        self.gridLayout.addWidget(self.fruit_label, 8, 0, 1, 1)

        self.veg_label = QLabel(editpatientmedicalinfopage)
        self.veg_label.setObjectName(u"veg_label")

        self.gridLayout.addWidget(self.veg_label, 9, 0, 1, 1)

        self.heavyalcholcons_label = QLabel(editpatientmedicalinfopage)
        self.heavyalcholcons_label.setObjectName(u"heavyalcholcons_label")

        self.gridLayout.addWidget(self.heavyalcholcons_label, 10, 0, 1, 1)

        self.anyhealthcare_label = QLabel(editpatientmedicalinfopage)
        self.anyhealthcare_label.setObjectName(u"anyhealthcare_label")

        self.gridLayout.addWidget(self.anyhealthcare_label, 11, 0, 1, 1)

        self.genhelth_label = QLabel(editpatientmedicalinfopage)
        self.genhelth_label.setObjectName(u"genhelth_label")

        self.gridLayout.addWidget(self.genhelth_label, 13, 0, 1, 1)

        self.nodocbccost_label = QLabel(editpatientmedicalinfopage)
        self.nodocbccost_label.setObjectName(u"nodocbccost_label")

        self.gridLayout.addWidget(self.nodocbccost_label, 12, 0, 1, 1)

        self.genhelth_lineEdit = QLineEdit(editpatientmedicalinfopage)
        self.genhelth_lineEdit.setObjectName(u"genhelth_lineEdit")

        self.gridLayout.addWidget(self.genhelth_lineEdit, 13, 1, 1, 1)

        self.menhelth_label = QLabel(editpatientmedicalinfopage)
        self.menhelth_label.setObjectName(u"menhelth_label")

        self.gridLayout.addWidget(self.menhelth_label, 15, 0, 1, 1)

        self.phyhelth_label = QLabel(editpatientmedicalinfopage)
        self.phyhelth_label.setObjectName(u"phyhelth_label")

        self.gridLayout.addWidget(self.phyhelth_label, 14, 0, 1, 1)

        self.phyhelth_lineEdit = QLineEdit(editpatientmedicalinfopage)
        self.phyhelth_lineEdit.setObjectName(u"phyhelth_lineEdit")

        self.gridLayout.addWidget(self.phyhelth_lineEdit, 14, 1, 1, 1)

        self.diffwalk_label = QLabel(editpatientmedicalinfopage)
        self.diffwalk_label.setObjectName(u"diffwalk_label")

        self.gridLayout.addWidget(self.diffwalk_label, 16, 0, 1, 1)

        self.menhelth_lineEdit = QLineEdit(editpatientmedicalinfopage)
        self.menhelth_lineEdit.setObjectName(u"menhelth_lineEdit")

        self.gridLayout.addWidget(self.menhelth_lineEdit, 15, 1, 1, 1)

        self.hc_comboBox = QComboBox(editpatientmedicalinfopage)
        self.hc_comboBox.addItem("")
        self.hc_comboBox.addItem("")
        self.hc_comboBox.setObjectName(u"hc_comboBox")

        self.gridLayout.addWidget(self.hc_comboBox, 1, 1, 1, 1)

        self.cc_comboBox = QComboBox(editpatientmedicalinfopage)
        self.cc_comboBox.addItem("")
        self.cc_comboBox.addItem("")
        self.cc_comboBox.setObjectName(u"cc_comboBox")

        self.gridLayout.addWidget(self.cc_comboBox, 2, 1, 1, 1)

        self.smoker_comboBox = QComboBox(editpatientmedicalinfopage)
        self.smoker_comboBox.addItem("")
        self.smoker_comboBox.addItem("")
        self.smoker_comboBox.setObjectName(u"smoker_comboBox")

        self.gridLayout.addWidget(self.smoker_comboBox, 4, 1, 1, 1)

        self.stroke_comboBox = QComboBox(editpatientmedicalinfopage)
        self.stroke_comboBox.addItem("")
        self.stroke_comboBox.addItem("")
        self.stroke_comboBox.setObjectName(u"stroke_comboBox")

        self.gridLayout.addWidget(self.stroke_comboBox, 5, 1, 1, 1)

        self.hd_comboBox = QComboBox(editpatientmedicalinfopage)
        self.hd_comboBox.addItem("")
        self.hd_comboBox.addItem("")
        self.hd_comboBox.setObjectName(u"hd_comboBox")

        self.gridLayout.addWidget(self.hd_comboBox, 6, 1, 1, 1)

        self.pa_comboBox = QComboBox(editpatientmedicalinfopage)
        self.pa_comboBox.addItem("")
        self.pa_comboBox.addItem("")
        self.pa_comboBox.setObjectName(u"pa_comboBox")

        self.gridLayout.addWidget(self.pa_comboBox, 7, 1, 1, 1)

        self.fruit_comboBox = QComboBox(editpatientmedicalinfopage)
        self.fruit_comboBox.addItem("")
        self.fruit_comboBox.addItem("")
        self.fruit_comboBox.setObjectName(u"fruit_comboBox")

        self.gridLayout.addWidget(self.fruit_comboBox, 8, 1, 1, 1)

        self.veggi_comboBox = QComboBox(editpatientmedicalinfopage)
        self.veggi_comboBox.addItem("")
        self.veggi_comboBox.addItem("")
        self.veggi_comboBox.setObjectName(u"veggi_comboBox")

        self.gridLayout.addWidget(self.veggi_comboBox, 9, 1, 1, 1)

        self.hac_comboBox = QComboBox(editpatientmedicalinfopage)
        self.hac_comboBox.addItem("")
        self.hac_comboBox.addItem("")
        self.hac_comboBox.setObjectName(u"hac_comboBox")

        self.gridLayout.addWidget(self.hac_comboBox, 10, 1, 1, 1)

        self.ahc_comboBox = QComboBox(editpatientmedicalinfopage)
        self.ahc_comboBox.addItem("")
        self.ahc_comboBox.addItem("")
        self.ahc_comboBox.setObjectName(u"ahc_comboBox")

        self.gridLayout.addWidget(self.ahc_comboBox, 11, 1, 1, 1)

        self.ndboc_comboBox = QComboBox(editpatientmedicalinfopage)
        self.ndboc_comboBox.addItem("")
        self.ndboc_comboBox.addItem("")
        self.ndboc_comboBox.setObjectName(u"ndboc_comboBox")

        self.gridLayout.addWidget(self.ndboc_comboBox, 12, 1, 1, 1)

        self.diffwalk_comboBox = QComboBox(editpatientmedicalinfopage)
        self.diffwalk_comboBox.addItem("")
        self.diffwalk_comboBox.addItem("")
        self.diffwalk_comboBox.setObjectName(u"diffwalk_comboBox")

        self.gridLayout.addWidget(self.diffwalk_comboBox, 16, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_18)

        self.back_pushButton = QPushButton(editpatientmedicalinfopage)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.horizontalLayout.addWidget(self.back_pushButton)

        self.save_pushButton = QPushButton(editpatientmedicalinfopage)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.horizontalLayout.addWidget(self.save_pushButton)

        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(editpatientmedicalinfopage)

        QMetaObject.connectSlotsByName(editpatientmedicalinfopage)
    # setupUi

    def retranslateUi(self, editpatientmedicalinfopage):
        editpatientmedicalinfopage.setWindowTitle(QCoreApplication.translate("editpatientmedicalinfopage", u"Form", None))
        self.editpatientmedicalinfo_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Edit Patient Medical Info", None))
        self.highchol_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"High cholestrol:", None))
        self.cholcheck_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Cholestrol check:", None))
        self.bmi_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"BMI:", None))
        self.highbp_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"High bp:", None))
        self.hb_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.hb_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.stroke_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Stroke:", None))
        self.smoker_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Smoker:", None))
        self.heartdis_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Heart Disease:", None))
        self.phyact_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Physical Activity:", None))
        self.fruit_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Fruits:", None))
        self.veg_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"vegetables:", None))
        self.heavyalcholcons_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Heavy Alcohol Consumption:", None))
        self.anyhealthcare_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Any healthcare:", None))
        self.genhelth_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"general health:", None))
        self.nodocbccost_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"No doctor because of cost:", None))
        self.menhelth_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"mental health:", None))
        self.phyhelth_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"physical health:", None))
        self.diffwalk_label.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"diffwalk", None))
        self.hc_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.hc_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.cc_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.cc_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.smoker_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.smoker_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.stroke_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.stroke_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.hd_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.hd_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.pa_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.pa_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.fruit_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.fruit_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.veggi_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.veggi_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.hac_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.hac_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.ahc_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.ahc_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.ndboc_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.ndboc_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.diffwalk_comboBox.setItemText(0, QCoreApplication.translate("editpatientmedicalinfopage", u"True", None))
        self.diffwalk_comboBox.setItemText(1, QCoreApplication.translate("editpatientmedicalinfopage", u"False", None))

        self.back_pushButton.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Back", None))
        self.save_pushButton.setText(QCoreApplication.translate("editpatientmedicalinfopage", u"Save", None))
    # retranslateUi

