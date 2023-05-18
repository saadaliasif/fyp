from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QVBoxLayout, QWidget)
import icon_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1124, 832)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        dashboard.setFont(font)
        self.actionQuit = QAction(dashboard)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(dashboard)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionCheck_For_Updates = QAction(dashboard)
        self.actionCheck_For_Updates.setObjectName(u"actionCheck_For_Updates")
        self.actionAddDoctor = QAction(dashboard)
        self.actionAddDoctor.setObjectName(u"actionAddDoctor")
        self.actionAddPatientRecord = QAction(dashboard)
        self.actionAddPatientRecord.setObjectName(u"actionAddPatientRecord")
        self.actionProfileInfo = QAction(dashboard)
        self.actionProfileInfo.setObjectName(u"actionProfileInfo")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu_pushButton = QPushButton(self.centralwidget)
        self.menu_pushButton.setObjectName(u"menu_pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.menu_pushButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_pushButton.setIcon(icon)
        self.menu_pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.menu_pushButton)

        self.menu_label = QLabel(self.centralwidget)
        self.menu_label.setObjectName(u"menu_label")
        self.menu_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.menu_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.profile_label = QLabel(self.centralwidget)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.profile_label)

        self.profile_pushButton = QPushButton(self.centralwidget)
        self.profile_pushButton.setObjectName(u"profile_pushButton")
        self.profile_pushButton.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/person-circle-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_pushButton.setIcon(icon1)
        self.profile_pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.profile_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 7, 7, 7)
        self.adddoctor_pushButton = QPushButton(self.centralwidget)
        self.adddoctor_pushButton.setObjectName(u"adddoctor_pushButton")
        self.adddoctor_pushButton.setFont(font1)
        self.adddoctor_pushButton.setAutoFillBackground(False)
        self.adddoctor_pushButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add-circle-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adddoctor_pushButton.setIcon(icon2)
        self.adddoctor_pushButton.setIconSize(QSize(40, 40))
        self.adddoctor_pushButton.setCheckable(False)
        self.adddoctor_pushButton.setAutoDefault(False)
        self.adddoctor_pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.adddoctor_pushButton)

        self.logout_pushButton = QPushButton(self.centralwidget)
        self.logout_pushButton.setObjectName(u"logout_pushButton")
        self.logout_pushButton.setFont(font1)
        self.logout_pushButton.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/remove-circle-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_pushButton.setIcon(icon3)
        self.logout_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.logout_pushButton)

        self.addpatient_pushButton = QPushButton(self.centralwidget)
        self.addpatient_pushButton.setObjectName(u"addpatient_pushButton")
        self.addpatient_pushButton.setFont(font1)
        self.addpatient_pushButton.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/person-add-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addpatient_pushButton.setIcon(icon4)
        self.addpatient_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.addpatient_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.search_label = QLabel(self.centralwidget)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setFont(font1)

        self.horizontalLayout.addWidget(self.search_label)

        self.search_comboBox = QComboBox(self.centralwidget)
        self.search_comboBox.setObjectName(u"search_comboBox")
        self.search_comboBox.setBaseSize(QSize(0, 0))
        self.search_comboBox.setFont(font1)
        self.search_comboBox.addItem("full_name")
        self.search_comboBox.addItem("age")
        self.search_comboBox.addItem("id")
        self.search_comboBox.addItem("sex")
        self.search_comboBox.addItem("resultcol")

        self.horizontalLayout.addWidget(self.search_comboBox)

        self.filter_lineEdit = QLineEdit(self.centralwidget)
        self.filter_lineEdit.setObjectName(u"filter_lineEdit")
        self.filter_lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.filter_lineEdit)

        self.search_pushButton = QPushButton(self.centralwidget)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.search_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.records_tableView = QTableView(self.centralwidget)
        self.records_tableView.setObjectName(u"records_tableView")
        self.records_tableView.setShowGrid(True)
        self.records_tableView.setGridStyle(Qt.NoPen)
        self.records_tableView.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.records_tableView)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 20)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1124, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        dashboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dashboard)
        self.statusbar.setObjectName(u"statusbar")
        dashboard.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionAddDoctor)
        self.menuFile.addAction(self.actionAddPatientRecord)
        self.menuView.addAction(self.actionProfileInfo)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionCheck_For_Updates)

        self.retranslateUi(dashboard)

        self.adddoctor_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Dashboard", None))
        self.actionQuit.setText(QCoreApplication.translate("dashboard", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("dashboard", u"About", None))
        self.actionCheck_For_Updates.setText(QCoreApplication.translate("dashboard", u"Check For Updates", None))
        self.actionAddDoctor.setText(QCoreApplication.translate("dashboard", u"AddDoctor", None))
        self.actionAddPatientRecord.setText(QCoreApplication.translate("dashboard", u"AddPatientRecord", None))
        self.actionProfileInfo.setText(QCoreApplication.translate("dashboard", u"ProfileInfo", None))
        self.menu_pushButton.setText("")
        self.menu_label.setText(QCoreApplication.translate("dashboard", u"pagename", None))
        self.profile_label.setText(QCoreApplication.translate("dashboard", u"profilename", None))
        self.profile_pushButton.setText("")
        self.adddoctor_pushButton.setText(QCoreApplication.translate("dashboard", u"add doctor", None))
        self.logout_pushButton.setText(QCoreApplication.translate("dashboard", u"logout", None))
        self.addpatient_pushButton.setText(QCoreApplication.translate("dashboard", u"add patient record", None))
        self.search_label.setText(QCoreApplication.translate("dashboard", u"Search By: ", None))
        self.search_pushButton.setText(QCoreApplication.translate("dashboard", u"search", None))
        self.menuFile.setTitle(QCoreApplication.translate("dashboard", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("dashboard", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("dashboard", u"View", None))
        self.menuSetting.setTitle(QCoreApplication.translate("dashboard", u"Setting", None))
        self.menuHelp.setTitle(QCoreApplication.translate("dashboard", u"Help", None))
        self.menuAbout.setTitle(QCoreApplication.translate("dashboard", u"About", None))
    # retranslateUi

