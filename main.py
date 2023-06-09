from PySide6.QtWidgets import QWidget,QMessageBox,QMainWindow,QTableView, QPushButton,QInputDialog,QHeaderView,QFileDialog
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem,QPixmap
from loginpage import Ui_loginpage
from signuppage import Ui_signuppage
from addpatientinfopage import Ui_addpatientinfopage
from addpatientmedicalinfopage import Ui_addpatientmedicalinfopage
from editpatientinfopage import Ui_editpatientinfopage
from editpatientmedicalinfopage import Ui_editpatientmedicalinfopage
from viewpatientinfopage import Ui_viewpatientinfopage
from viewpatientmedicalinfopage import Ui_viewpatientmedicalinfopage
from dashboardpage import Ui_dashboard
from remarkspage import Ui_remarkspage
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator,QIntValidator
import datetime
import pytesseract
import cv2
import joblib
import re
import mysql.connector
from doctor import DOCTOR
from patient import PATIENT

def Connection():
    mydb= mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="fyp"
            )
    return mydb

model = joblib.load("model.pkl")

class loginrun(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginpage()
        self.ui.setupUi(self)
        self.ui.signin_pushButton.clicked.connect(self.run)
        self.load_saved_credentials()
        self.setup_input_validation()
        
    def load_saved_credentials(self):
        try:
            with open("credentials.txt", "r") as file:
                credentials = file.readline().strip().split(",")
                if len(credentials) == 2:
                    username, password = credentials
                    self.ui.username_lineEdit.setText(username)
                    self.ui.password_lineEdit.setText(password)
                    self.ui.remember_me_checkBox.setChecked(True)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "file error(credentials).")


    def setup_input_validation(self):
        username_validator = QRegularExpressionValidator(QRegularExpression("^[A-Za-z0-9]+$"))
        self.ui.username_lineEdit.setValidator(username_validator)

        password_validator = QRegularExpressionValidator(QRegularExpression("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\S]{8,}$"))
        self.ui.password_lineEdit.setValidator(password_validator)

    def run(self):
        username = self.ui.username_lineEdit.text().strip()
        password = self.ui.password_lineEdit.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both a username and password.")
            return

        if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\S]{8,}$", password):
            QMessageBox.warning(self, "Error", "Please enter a strong password.")
            return
        
        doc = DOCTOR()
        doc.username = username
        doc.password = password
        res = doc.Login()
        if res == 0:
            pass
        else:
            if self.ui.remember_me_checkBox.isChecked():
                with open("credentials.txt", "w") as file:
                    file.write(f"{username},{password}")
            else:
                with open("credentials.txt", "w") as file:
                    file.write("")
            self.hide()
            con = Connection()
            cursor = con.cursor()
            try:
                cursor.execute(f"SELECT id FROM doctor WHERE username = '{doc.username}'")
                result = cursor.fetchone()
                docid = result[0]
            finally:
                cursor.close()
                con.close()

            self.a = Dashboardrun(doc=doc, docid=docid)
            self.a.setWindowTitle("Dashboard")
            self.a.ui.profile_label.setText(doc.username)
            if docid != 20:
                self.a.ui.adddoctor_pushButton.hide()
            self.a.ui.menu_label.setText("Dashboard")
            self.a.show()

class signuprun(QWidget):
    def __init__(self,doc,docid=None):
        super().__init__()
        self.doc=doc
        self.ui = Ui_signuppage()
        self.ui.setupUi(self)
        self.ui.signup_pushButton.clicked.connect(self.run)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.setup_input_validation()
        self.docid=docid
        
    def setup_input_validation(self):
        fname_validator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-zA-Z]{2,30}$"), self.ui.first_name_lineEdit
        )
        lname_validator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-zA-Z]{2,30}$"), self.ui.last_name_lineEdit
        )
        age_validator = QIntValidator(1, 100, self.ui.age_lineEdit)
        income_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d+(\.\d+)?$"), self.ui.income_lineEdit
        )
        username_validator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-zA-Z0-9_]{3,20}$"), self.ui.username_lineEdit
        )
        password_validator = QRegularExpressionValidator(
            QRegularExpression(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"), self.ui.password_lineEdit
        )
        confirm_password_validator = QRegularExpressionValidator(
            QRegularExpression(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"), self.ui.confirm_password_lineEdit
        )
        phone_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d{12}$"), self.ui.phone_lineEdit
        )
        postal_code_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d{5}$"), self.ui.postal_code_lineEdit
        )
        email_validator = QRegularExpressionValidator(
            QRegularExpression(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            ),
            self.ui.email_lineEdit,
        )
        self.ui.phone_lineEdit.setValidator(phone_validator)
        self.ui.postal_code_lineEdit.setValidator(postal_code_validator)
        self.ui.email_lineEdit.setValidator(email_validator)
        self.ui.first_name_lineEdit.setValidator(fname_validator)
        self.ui.last_name_lineEdit.setValidator(lname_validator)
        self.ui.age_lineEdit.setValidator(age_validator)
        self.ui.income_lineEdit.setValidator(income_validator)
        self.ui.username_lineEdit.setValidator(username_validator)
        self.ui.password_lineEdit.setValidator(password_validator)
        self.ui.confirm_password_lineEdit.setValidator(confirm_password_validator)
        
    def back(self):
        self.close()
        self.a=Dashboardrun(doc=self.doc,docid=self.docid)
        self.a.setWindowTitle("Dashboard")
        self.a.ui.profile_label.setText(self.doc.username)
        self.a.ui.menu_label.setText("Dashboard")
        if self.docid != 20:
                self.a.ui.adddoctor_pushButton.hide()
        self.a.show()
        
    def run(self):
        doc=DOCTOR()
        fname = self.ui.first_name_lineEdit.text()
        lname = self.ui.last_name_lineEdit.text()
        age = self.ui.age_lineEdit.text()
        sex = self.ui.sex_comboBox.currentText()
        phone =self.ui.phone_lineEdit.text()
        education = self.ui.edu_comboBox.currentText()
        income = self.ui.income_lineEdit.text()
        city = self.ui.city_comboBox.currentText()
        country = self.ui.country_comboBox.currentText()
        email = self.ui.email_lineEdit.text()
        username = self.ui.username_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        confirm_password = self.ui.confirm_password_lineEdit.text()
        postal_code = self.ui.postal_code_lineEdit.text()
        
        if not fname:
            QMessageBox.warning(self, "Error", "Please enter the first name.")
            return
        
        elif not lname:
            QMessageBox.warning(self, "Error", "Please enter the last name.")
            return
        
        elif not age:
            QMessageBox.warning(self, "Error", "Please enter the age.")
            return
        
        elif not phone:
            QMessageBox.warning(self, "Error", "Please enter the phone number.")
            return
        
        elif not income:
            QMessageBox.warning(self, "Error", "Please enter the income.")
            return

        elif not email:
            QMessageBox.warning(self, "Error", "Please enter the email.")
            return
        
        elif not username:
            QMessageBox.warning(self, "Error", "Please enter the username.")
            return
        
        elif not password:
            QMessageBox.warning(self, "Error", "Please enter the password.")
            return
        
        elif not confirm_password:
            QMessageBox.warning(self, "Error", "Please confirm the password.")
            return
        
        elif password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return
        
        elif not postal_code:
            QMessageBox.warning(self, "Error", "Please enter the postal code.")
            return
        else:
            doc.fname=self.ui.first_name_lineEdit.text()
            doc.lname=self.ui.last_name_lineEdit.text()
            doc.age=self.ui.age_lineEdit.text()
            doc.sex=self.ui.sex_comboBox.currentText()
            doc.phone=self.ui.phone_lineEdit.text()
            doc.education=self.ui.edu_comboBox.currentText()
            doc.income=self.ui.income_lineEdit.text()
            doc.city=self.ui.city_comboBox.currentText()
            doc.country=self.ui.country_comboBox.currentText()
            doc.email=self.ui.email_lineEdit.text()
            doc.username=self.ui.username_lineEdit.text()
            doc.password=self.ui.password_lineEdit.text()
            doc.confirm_password=self.ui.confirm_password_lineEdit.text()
            doc.postal_code=self.ui.postal_code_lineEdit.text()
            res=doc.Signup()
            if res == 0:
                pass
            else:
                QMessageBox.warning(None,"Login", "signned up sucessfully!")
                self.hide()
                self.a=Dashboardrun(doc=self.doc,docid=self.docid)
                self.a.setWindowTitle("Dashboard")
                self.a.ui.profile_label.setText(self.doc.username)
                self.a.ui.menu_label.setText("Dashboard")
                self.a.show()
    
class AddPatientInforun(QWidget):
    def __init__(self,doc=None,docid=None):
        super().__init__()
        self.doc=doc
        self.docid=docid
        self.ui = Ui_addpatientinfopage()
        self.ui.setupUi(self)
        self.ui.addpatientinfo_pushButton.clicked.connect(self.run)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.setup_input_validation()

    def setup_input_validation(self):
        fname_validator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-zA-Z]{2,30}$"), self.ui.first_name_lineEdit
        )
        lname_validator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-zA-Z]{2,30}$"), self.ui.last_name_lineEdit
        )
        age_validator = QIntValidator(1, 100, self.ui.age_lineEdit)
        income_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d+(\.\d+)?$"), self.ui.income_lineEdit
        )
        phone_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d{12}$"), self.ui.phone_lineEdit
        )
        postal_code_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d{5}$"), self.ui.postal_code_lineEdit
        )
        email_validator = QRegularExpressionValidator(
            QRegularExpression(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            ),
            self.ui.email_lineEdit,
        )
        self.ui.phone_lineEdit.setValidator(phone_validator)
        self.ui.postal_code_lineEdit.setValidator(postal_code_validator)
        self.ui.email_lineEdit.setValidator(email_validator)
        self.ui.first_name_lineEdit.setValidator(fname_validator)
        self.ui.last_name_lineEdit.setValidator(lname_validator)
        self.ui.age_lineEdit.setValidator(age_validator)
        self.ui.income_lineEdit.setValidator(income_validator)
        
    def back(self):
        self.a=Dashboardrun(doc=self.doc,docid=self.docid)
        self.a.setWindowTitle("Dashboard")
        self.a.ui.profile_label.setText(self.doc.username)
        self.a.ui.menu_label.setText("Dashboard")
        if self.docid != 20:
                self.a.ui.adddoctor_pushButton.hide()
        self.close()
        self.a.show()
        
    def run(self):
        if not self.ui.first_name_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the first name.")
            return
        
        elif not self.ui.last_name_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the last name.")
            return
        
        elif not self.ui.age_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the age.")
            return

        elif not self.ui.phone_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the phone number.")
            return
    
        elif not self.ui.income_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the income.")
            return
        
        elif not self.ui.city_comboBox.currentText():
            QMessageBox.warning(self, "Error", "Please enter the city.")
            return
        
        elif not self.ui.country_comboBox.currentText():
            QMessageBox.warning(self, "Error", "Please enter the country.")
            return
        
        elif not self.ui.email_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the email.")
            return
        
        elif not self.ui.postal_code_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the postal code.")
            return
        else:
            pat=PATIENT(self.docid)
            pat.fname=self.ui.first_name_lineEdit.text()
            pat.lname=self.ui.last_name_lineEdit.text()
            pat.age=self.ui.age_lineEdit.text()
            pat.city=self.ui.city_comboBox.currentText()
            pat.country=self.ui.country_comboBox.currentText()
            pat.education=self.ui.edu_comboBox.currentText()
            pat.email=self.ui.email_lineEdit.text()
            pat.phone=self.ui.phone_lineEdit.text()
            pat.sex=self.ui.sex_comboBox.currentText()
            pat.postal_code=self.ui.postal_code_lineEdit.text()
            pat.docid=self.docid
            pat.income=self.ui.income_lineEdit.text()
            res=pat.AddPatientInfo()
            if res==0:
                pass
            if res==1:
                QMessageBox.information(self, "info", "sucessfull!!!")
                self.hide()
                con =Connection()
                cursor=con.cursor()
                try:
                    cursor.execute("SELECT idinfo FROM patientinfo ORDER BY idinfo DESC LIMIT 1")
                    result = cursor.fetchall()
                    patid=int(result[0][0])
                finally:
                    cursor.close()
                    con.close()
                self.a=AddPatientMedicalInforun(doc=self.doc,patid=patid,docid=self.docid,sex=pat.sex,education=pat.education,income=pat.income,age=pat.age)
                self.a.show()

class AddPatientMedicalInforun(QWidget):
    def __init__(self,doc=None,patid=None,docid=None,education=None,income=None,age=None,sex=None):
        super().__init__()
        self.doc=doc
        self.patid=patid
        self.docid=docid
        self.educ=education
        self.income=income
        self.sex=sex
        print(self.sex)
        if self.sex == "male" or self.sex == "Male" or self.sex == "MALE":
            self.sex=1
        if self.sex == "female" or self.sex == "Female" or self.sex == "FEMALE":
            self.sex=2
        print(self.sex)
        self.age=age
        self.ui = Ui_addpatientmedicalinfopage()
        self.ui.setupUi(self)
        self.ui.addpatientmedicalinfo_pushButton.clicked.connect(self.run)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.ui.browse_pushButton.clicked.connect(self.file)
        self.setup_input_validation()
        
    def setup_input_validation(self):
        genhelth_validator = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.ui.genhealth_lineEdit.setValidator(genhelth_validator)

        phyhelth_validator = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.ui.physhealth_lineEdit.setValidator(phyhelth_validator)
        
        menthealth_validator = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.ui.menhealth_lineEdit.setValidator(menthealth_validator)
        
        bmi_validator = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.ui.bmi_lineEdit.setValidator(bmi_validator)
        
    def back(self):
        self.a=AddPatientInforun(doc=self.doc,docid=self.docid)
        # self.a.setWindowTitle("Dashboard")
        # self.a.ui.profile_label.setText(self.doc.username)
        # self.a.ui.menu_label.setText("Dashboard")
        # if self.docid != 20:
        #         self.a.ui.adddoctor_pushButton.hide()
        self.close()
        self.a.show()
        
    def file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            image_path = selected_files[0]
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            self.ui.file_label.setText(image_path)
            print(text)
        
    def run(self):
        print(self.sex)
        pat=PATIENT(patid=self.patid,docid=self.docid)
        if self.ui.fhbp_radioButton.isChecked():
            a=0
        elif self.ui.thbp_radioButton.isChecked():
            a=1
        else:
            a=2
        pat.highbp=a
        if self.ui.fhc_radioButton.isChecked():
            b=0
        elif self.ui.thc_radioButton.isChecked():
            b=1
        else: 
            b=2
        pat.highchol=b
        if self.ui.fcc_radioButton.isChecked():
            c=0
        elif self.ui.tcc_radioButton.isChecked():
            c=1
        else: 
            c=2
        pat.cholcheck=c
        if self.ui.fs_radioButton.isChecked():
            d=0
        elif self.ui.ts_radioButton.isChecked():
            d=1
        else: 
            d=2
        pat.smoker=d
        if self.ui.fstroke_radioButton.isChecked():
            e=0
        elif self.ui.tstroke_radioButton.isChecked():
            e=1
        else: 
            e=2
        pat.stroke=e
        if self.ui.fhd_radioButton.isChecked():
            f=0
        elif self.ui.thd_radioButton.isChecked():
            f=1
        else: 
            f=2
        pat.heartdisease=f
        if self.ui.fpa_radioButton.isChecked():
            g=0
        elif self.ui.tpa_radioButton.isChecked():
            g=1
        else: 
            g=2
        pat.physactivity=g
        if self.ui.ff_radioButton.isChecked():
            h=0
        elif self.ui.tf_radioButton.isChecked():
            h=1
        else: 
            h=2
        pat.fruits=h
        if self.ui.fv_radioButton.isChecked():
            i=0
        elif self.ui.tv_radioButton.isChecked():
            i=1
        else: 
            i=2
        pat.veggies=i
        if self.ui.fhac_radioButton.isChecked():
            j=0
        elif self.ui.thac_radioButton.isChecked():
            j=1
        else: 
            j=2
        pat.heavyalcohol=j
        if self.ui.fah_radioButton.isChecked():
            z=0
        elif self.ui.tah_radioButton.isChecked():
            z=1
        else: 
            z=2
        pat.anyhealthcare=z
        if self.ui.fndboc_radioButton.isChecked():
            y=0
        elif self.ui.tndboc_radioButton.isChecked():
            y=1
        else: 
            y=2
        
        if not self.ui.bmi_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the BMI.")
            return
        elif not self.ui.genhealth_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter the Gen health.")
            return
        
        elif not self.ui.physhealth_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter phsyical health.")
            return
        
        elif not self.ui.menhealth_lineEdit.text():
            QMessageBox.warning(self, "Error", "Please enter mental health.")
            return
        
        pat.nodoc=y
        pat.bmi=self.ui.bmi_lineEdit.text()
        pat.genhelth=self.ui.genhealth_lineEdit.text()
        pat.physhelth=self.ui.physhealth_lineEdit.text()
        pat.menthealth=self.ui.menhealth_lineEdit.text()
        if self.ui.fd_radioButton.isChecked():
            n=0
        elif self.ui.td_radioButton.isChecked():
            n=1
        else: 
            n=2
        pat.diffwalk=n
        if (a!=2) and (b!=2) and (c!=2) and (d!=2) and (e!=2) and (f!=2) and (g!=2) and (h!=2) and (i!=2) and (j!=2) and (n!=2) and (z!=2) and (y!=2):
            if self.educ == "undergraduate":
                education = 1
            elif self.educ == "graduate":
                education = 2
            elif self.educ == "postgraduate":
                education = 3
            elif self.educ == "phd":
                education = 4
            else: education = 0
            print(self.sex)
            input_data = {
            "HighBP": pat.highbp,
            "HighChol": pat.highchol,
            "CholCheck": pat.cholcheck,
            "BMI": pat.bmi,
            "Smoker": pat.smoker,
            "Stroke": pat.stroke,
            "HeartDiseaseorAttack": pat.heartdisease,
            "PhysActivity": pat.physactivity,
            "Fruits": pat.fruits,
            "Veggies": pat.veggies,
            "HvyAlcoholConsump": pat.heavyalcohol,
            "AnyHealthcare": pat.anyhealthcare,
            "NoDocbcCost": pat.nodoc,
            "GenHlth": pat.genhelth,
            "MentHlth": pat.menthealth,
            "PhysHlth": pat.physhelth,
            "DiffWalk": pat.diffwalk,
            "Sex": self.sex,
            "Age": self.age,
            "Education": education,
            "Income": self.income
            }
            
            pat.AddPatientMedicalInfo()
            self.hide()
            self.a=remarkspagerun(self.doc,self.docid,self.patid,input_data,0)
            self.a.show()
        else:
            QMessageBox.critical(None,'selection error','You missed something')

class ViewPatientInforun(QWidget):
    def __init__(self,doc=None,patient_id=None,docid=None):
        super().__init__()
        self.doc=doc
        self.docid=docid
        self.ui = Ui_viewpatientinfopage()
        self.ui.setupUi(self)
        self.patient_id=patient_id
        self.ui.edit_pushButton.clicked.connect(self.edit)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.ui.delete_pushButton.clicked.connect(self.delete)

        
    def edit(self):
        self.hide()
        self.a=EditPatientInforun(pid=self.patient_id,doc=self.doc,docid=self.docid)
        self.a.show()
        
    def delete(self):
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"DELETE FROM result where patient_id = ({self.patient_id})")
            cursor.execute(f"DELETE FROM patient where patientinfo_id = ({self.patient_id})")
            cursor.execute(f"DELETE FROM patientinfo where idinfo = ({self.patient_id})")
            con.commit()
            QMessageBox.information(None, 'Information', 'Deleted successfully')
            doc=DOCTOR()
            self.a=Dashboardrun(doc=self.doc,docid=self.docid,)
            self.a.setWindowTitle("Dashboard")
            self.a.ui.profile_label.setText(self.doc.username)
            self.a.ui.menu_label.setText("Dashboard")
            self.close()
            self.a.show()
        except Exception as e:
            QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            con.close()
        
    def back(self):
        self.a=Dashboardrun(doc=self.doc,docid=self.docid)
        self.a.setWindowTitle("Dashboard")
        self.a.ui.profile_label.setText(self.doc.username)
        self.a.ui.menu_label.setText("Dashboard")
        if self.docid != 20:
                self.a.ui.adddoctor_pushButton.hide()
        self.close()
        self.a.show()

class ViewPatientMedicalInforun(QWidget):
    def __init__(self,doc=None,patient_id=None,docid=None):
        super().__init__()
        self.doc=doc
        self.docid=docid
        self.ui = Ui_viewpatientmedicalinfopage()
        self.ui.setupUi(self)
        self.patient_id=patient_id
        self.ui.delete_pushButton.clicked.connect(self.delete)
        self.ui.edit_pushButton.clicked.connect(self.edit)
        self.ui.back_pushButton.clicked.connect(self.back)

        
    def edit(self):
        self.hide()
        self.a=EditPatientMedicalInforun(doc=self.doc,docid=self.docid,patientid=self.patient_id)
        self.a.show()
        
    def delete(self):
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"DELETE FROM result where patient_id = ({self.patient_id})")
            cursor.execute(f"DELETE FROM patient where patientinfo_id = ({self.patient_id})")
            cursor.execute(f"DELETE FROM patientinfo where idinfo = ({self.patient_id})")
            con.commit()
            QMessageBox.information(None, 'Information', 'Deleted successfully')
            doc=DOCTOR()
            self.a=Dashboardrun(doc=self.doc,docid=self.docid,)
            self.a.setWindowTitle("Dashboard")
            self.a.ui.profile_label.setText(self.doc.username)
            self.a.ui.menu_label.setText("Dashboard")
            self.close()
            self.a.show()
        except Exception as e:
            QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            con.close()

    def back(self):
        doc=DOCTOR()
        self.a=Dashboardrun(docid=self.docid)
        self.a.setWindowTitle("Dashboard")
        self.a.ui.profile_label.setText(doc.username)
        self.a.ui.menu_label.setText("Dashboard")
        if self.docid != 20:
                self.a.ui.adddoctor_pushButton.hide()
        self.close()
        self.a.show()

class EditPatientInforun(QWidget):
    def __init__(self,pid=None,doc=None,docid=None):
        super().__init__()
        self.patientid=pid
        self.doc=doc
        print(self.patientid)
        self.docid=docid
        self.ui = Ui_editpatientinfopage()
        self.ui.setupUi(self)
        self.setup_input_validation()
        if self.patientid is None:
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"SELECT * FROM doctor WHERE id = ({self.docid})")
                self.result = cursor.fetchone()
            finally:
                cursor.close()
                con.close()
            self.setWindowTitle("edit doctor info")
            self.ui.editpatientinfo_label.setText("edit doctor info")
            self.ui.back_pushButton.clicked.connect(self.back)
            self.ui.save_pushButton.clicked.connect(self.save)
            self.ui.age_lineEdit.setText(str(self.result[4]))
            self.ui.city_comboBox.setCurrentText(str(self.result[10]))
            self.ui.name_lineEdit.setText(str(self.result[1]) + " " + str(self.result[2]))
            self.ui.income_lineEdit.setText(str(self.result[8]))
            self.ui.country_comboBox.setCurrentText(str(self.result[11]))
            self.ui.edu_comboBox.setCurrentText(str(self.result[9]))
            self.ui.sex_comboBox.setCurrentText(str(self.result[3]))
            self.ui.email_lineEdit.setText(str(self.result[6]))
            self.ui.phone_lineEdit.setText(str(self.result[13]))
            self.ui.postal_lineEdit.setText(str(self.result[12]))
        else:
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"SELECT * FROM patientinfo WHERE idinfo = ({self.patientid})")
                self.result = cursor.fetchone()
            finally:
                cursor.close()
                con.close()
            self.ui.back_pushButton.clicked.connect(self.back)
            self.ui.save_pushButton.clicked.connect(self.save)
            self.ui.name_lineEdit.setText(str(self.result[1]) + " " + str(self.result[2]))
            self.ui.age_lineEdit.setText(str(self.result[4]))
            self.ui.sex_comboBox.setCurrentText(str(self.result[3]))
            self.ui.postal_lineEdit.setText(str(self.result[9]))
            self.ui.country_comboBox.setCurrentText(str(self.result[7]))
            self.ui.city_comboBox.setCurrentText(str(self.result[8]))
            self.ui.edu_comboBox.setCurrentText(str(self.result[6]))
            self.ui.email_lineEdit.setText(str(self.result[10]))
            self.ui.phone_lineEdit.setText(str(self.result[11]))
            self.ui.income_lineEdit.setText(str(self.result[5]))
        
    def setup_input_validation(self):
        name_validator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-zA-Z]{2,30}$"), self.ui.name_lineEdit
        )
        age_validator = QIntValidator(1, 100, self.ui.age_lineEdit)
        income_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d+(\.\d+)?$"), self.ui.income_lineEdit
        )
        phone_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d{12}$"), self.ui.phone_lineEdit
        )
        postal_code_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d{5}$"), self.ui.postal_lineEdit
        )
        email_validator = QRegularExpressionValidator(
            QRegularExpression(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            ),
            self.ui.email_lineEdit,
        )
        self.ui.phone_lineEdit.setValidator(phone_validator)
        self.ui.postal_lineEdit.setValidator(postal_code_validator)
        self.ui.email_lineEdit.setValidator(email_validator)
        self.ui.name_lineEdit.setValidator(name_validator)
        self.ui.age_lineEdit.setValidator(age_validator)
        self.ui.income_lineEdit.setValidator(income_validator)
        
    def back(self):
        print(self.patientid)
        self.hide()
        if self.patientid is None:
            self.a=ViewPatientInforun(doc=self.doc,docid=self.docid,patient_id=self.patientid)
            self.a.setWindowTitle("Doctor Profile Info")
            self.a.ui.viewpatientinfo_label.setText("Doctor Profile Info")
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"SELECT * FROM doctor WHERE id = ('{self.docid}')")
                result = cursor.fetchone()
            finally:
                cursor.close()
                con.close()
            self.a.ui.postal_out_label.setText(str(result[12]))
            self.a.ui.email_out_label.setText(str(result[6]))
            self.a.ui.phone_out_label.setText(str(result[13]))
            self.a.ui.income_out_label.setText(str(result[8]))
            self.a.ui.result_out_label.hide()
            self.a.ui.result_label.hide()
            self.a.ui.gender_out_label.setText(str(result[3]))
            self.a.ui.country_out_label.setText(str(result[11]))
            self.a.ui.education_out_label.setText(str(result[9]))
            self.a.ui.city_out_label.setText(str(result[10]))
            self.a.ui.age_out_label.setText(str(result[4]))
            self.a.ui.name_out_label.setText(str(result[1]) + " " + str(result[2]))
            self.a.show()
        else:
            self.a=ViewPatientInforun(patient_id=self.patientid,doc=self.doc,docid=self.docid)
            self.a.setWindowTitle("Patient Profile Info")
            self.a.ui.viewpatientinfo_label.setText("Patient Profile Info")
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"SELECT * FROM patientinfo WHERE idinfo = ('{self.patientid}')")
                result = cursor.fetchone()
            finally:
                cursor.close()
                con.close()   
            self.a.ui.postal_out_label.setText(str(result[9]))
            self.a.ui.email_out_label.setText(str(result[10]))
            self.a.ui.phone_out_label.setText(str(result[11]))
            self.a.ui.income_out_label.setText(str(result[5]))
            self.a.ui.result_out_label.hide()
            self.a.ui.result_label.hide()
            self.a.ui.gender_out_label.setText(str(result[3]))
            self.a.ui.country_out_label.setText(str(result[7]))
            self.a.ui.education_out_label.setText(str(result[6]))
            self.a.ui.city_out_label.setText(str(result[8]))
            self.a.ui.age_out_label.setText(str(result[4]))
            self.a.ui.name_out_label.setText(str(result[1]) + " " + str(result[2]))
            self.a.show()
        
        
    def save(self):
        name = self.ui.name_lineEdit.text()
        name=name.split()
        fname=name[0]
        lname=name[1]
        age = self.ui.age_lineEdit.text()
        sex = self.ui.sex_comboBox.currentText()
        postal = self.ui.postal_lineEdit.text()
        country = self.ui.country_comboBox.currentText()
        city = self.ui.city_comboBox.currentText()
        education = self.ui.edu_comboBox.currentText()
        email = self.ui.email_lineEdit.text()
        phone = self.ui.phone_lineEdit.text()
        income = self.ui.income_lineEdit.text()

        if self.patientid is None:
            query = f"UPDATE doctor SET first_name = '{fname}', last_name = '{lname}', age = {age}, sex = '{sex}', postal_code = {postal}, country = '{country}' , city = '{city}' , education = '{education}' , email = '{email}' , phone = {phone} , income = {income} WHERE id = {self.docid}"
        else:
            query = f"UPDATE patientinfo SET first_name = '{fname}', last_name = '{lname}', age = {age}, sex = '{sex}', postal_code = {postal}, country = '{country}' , city = '{city}' , education = '{education}' , email = '{email}' , phone = {phone} , income = {income} WHERE idinfo = {self.patientid}"
            
        con = Connection()
        
        try:
            with con.cursor() as cursor:
                cursor.execute(query)
                con.commit()
                QMessageBox.information(None, 'Information', 'Saved successfully')
        except Exception as e:
            con.rollback()
            QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
        finally:
            con.close()
        self.a=Dashboardrun(doc=self.doc,docid=self.docid)
        self.a.setWindowTitle("Dashboard")
        self.a.ui.profile_label.setText(self.doc.username)
        self.a.ui.menu_label.setText("Dashboard")
        self.close()
        self.a.show()
        

class EditPatientMedicalInforun(QWidget):
    def __init__(self,doc=None,docid=None,patientid=None):
        super().__init__()
        self.patientid=patientid
        self.doc=doc
        self.docid=docid
        self.ui = Ui_editpatientmedicalinfopage()
        self.ui.setupUi(self)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.ui.save_pushButton.clicked.connect(self.save)
        self.setup_input_validation()
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"SELECT * FROM patient WHERE patientinfo_id = ('{self.patientid}')")
            self.result = cursor.fetchone()
        finally:
            # cursor.close()
            con.close()
        
        self.ui.bmi_lineEdit.setText(str(self.result[1]))
        res = True if self.result[2] == 1 else False
        self.ui.hb_comboBox.setCurrentText(str(res))
        res = True if self.result[3] == 1 else False
        self.ui.hc_comboBox.setCurrentText(str(res))
        res = True if self.result[4] == 1 else False
        self.ui.cc_comboBox.setCurrentText(str(res))
        res = True if self.result[5] == 1 else False
        self.ui.smoker_comboBox.setCurrentText(str(res))
        res = True if self.result[6] == 1 else False
        self.ui.stroke_comboBox.setCurrentText(str(res))
        res = True if self.result[7] == 1 else False
        self.ui.hd_comboBox.setCurrentText(str(res))
        res = True if self.result[8] == 1 else False
        self.ui.pa_comboBox.setCurrentText(str(res))
        res = True if self.result[9] == 1 else False
        self.ui.fruit_comboBox.setCurrentText(str(res))
        res = True if self.result[10] == 1 else False
        self.ui.veggi_comboBox.setCurrentText(str(res))
        res = True if self.result[11] == 1 else False
        self.ui.hac_comboBox.setCurrentText(str(res))
        res = True if self.result[12] == 1 else False
        self.ui.ahc_comboBox.setCurrentText(str(res))
        res = True if self.result[13] == 1 else False
        self.ui.ndboc_comboBox.setCurrentText(str(res))
        self.ui.genhelth_lineEdit.setText(str(self.result[14]))
        self.ui.menhelth_lineEdit.setText(str(self.result[15]))
        self.ui.phyhelth_lineEdit.setText(str(self.result[16]))
        res = True if self.result[17] == 1 else False
        self.ui.diffwalk_comboBox.setCurrentText(str(res))
        
    def setup_input_validation(self):
        stroke_validator = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.ui.genhelth_lineEdit.setValidator(stroke_validator)
        self.ui.phyhelth_lineEdit.setValidator(stroke_validator)        
        self.ui.menhelth_lineEdit.setValidator(stroke_validator)
        self.ui.bmi_lineEdit.setValidator(stroke_validator)        
        
    def back(self):
        self.hide()
        self.a=ViewPatientMedicalInforun(doc=self.doc,docid=self.docid,patient_id=self.patientid)
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"SELECT * FROM patient WHERE patientinfo_id = ('{self.patientid}')")
            result = cursor.fetchone()
        finally:
            con.close()
        
        self.a.ui.bmi_out_label.setText(str(result[1]))
        self.a.ui.highbp_out_label.setText(str(result[2]))
        self.a.ui.highchol_out_label.setText(str(result[3]))
        self.a.ui.cholcheck_out_label.setText(str(result[4]))
        self.a.ui.smoker_out_label.setText(str(result[5]))
        self.a.ui.stroke_out_label.setText(str(result[6]))
        self.a.ui.heartdis_out_label.setText(str(result[7]))
        self.a.ui.phyact_out_label.setText(str(result[8]))
        self.a.ui.fruit_out_label.setText(str(result[9]))
        self.a.ui.veg_out_label.setText(str(result[10]))
        self.a.ui.heavyalcholcons_out_label.setText(str(result[11]))
        self.a.ui.anyhealthcare_out_label.setText(str(result[12]))
        self.a.ui.nodocbcost_out_label.setText(str(result[13]))
        self.a.ui.genhelth_out_label.setText(str(result[14]))
        self.a.ui.menhelth_out_label.setText(str(result[15]))
        self.a.ui.phyhelth_out_label.setText(str(result[16]))
        self.a.ui.diffwalk_out_label.setText(str(result[17]))
        self.a.show()

    def save(self):
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"SELECT * FROM patientinfo WHERE idinfo = ({self.patientid})")
            self.result = cursor.fetchone()
        finally:
            cursor.close()
            con.close()
        bmi = self.ui.bmi_lineEdit.text()
        highbp = 1 if self.ui.hb_comboBox.currentText() == "True" else 0
        highchol = 1 if self.ui.hc_comboBox.currentText() == "True" else 0
        cholcheck = 1 if self.ui.cc_comboBox.currentText() == "True" else 0
        smoker = 1 if self.ui.smoker_comboBox.currentText() == "True" else 0
        stroke = 1 if self.ui.stroke_comboBox.currentText() == "True" else 0
        heartdisease = 1 if self.ui.hd_comboBox.currentText() == "True" else 0
        phyact = 1 if self.ui.pa_comboBox.currentText() == "True" else 0
        fruit = 1 if self.ui.fruit_comboBox.currentText() == "True" else 0
        vegetable = 1 if self.ui.veggi_comboBox.currentText() == "True" else 0
        heavyalcoholcons = 1 if self.ui.hac_comboBox.currentText() == "True" else 0
        anyhealthcare = 1 if self.ui.ahc_comboBox.currentText() == "True" else 0
        nocostbcdoc = 1 if self.ui.ndboc_comboBox.currentText() == "True" else 0
        genhelth = self.ui.genhelth_lineEdit.text()
        menhelth = self.ui.menhelth_lineEdit.text()
        phyhelth = self.ui.phyhelth_lineEdit.text()
        diffwalk = 1 if self.ui.diffwalk_comboBox.currentText() == "True" else 0
        if self.result[6] == "undergraduate":
            education = 1
        elif self.result[6] == "graduate":
            education = 2
        elif self.result[6] == "postgraduate":
            education = 3
        elif self.result[6] == "phd":
            education = 4
        else: education = 0
        if self.result[4] == 'male':
            result = 1
        else:
            result = 0
        input_data = {
            "HighBP": highbp,
            "HighChol": highchol,
            "CholCheck": cholcheck,
            "BMI": bmi,
            "Smoker": smoker,
            "Stroke": stroke,
            "HeartDiseaseorAttack": heartdisease,
            "PhysActivity": phyact,
            "Fruits": fruit,
            "Veggies": vegetable,
            "HvyAlcoholConsump": heavyalcoholcons,
            "AnyHealthcare": anyhealthcare,
            "NoDocbcCost": nocostbcdoc,
            "GenHlth": genhelth,
            "MentHlth": menhelth,
            "PhysHlth": phyhelth,
            "DiffWalk": diffwalk,
            "Sex": result,
            "Age": self.result[3],
            "Education": education,
            "Income": self.result[5]
            }

        query = f"UPDATE patient SET BMI = {bmi} , HIGH_BP = {highbp},HIGH_CHOL = {highchol}, CHOL_CHECK = {cholcheck},SMOKER = {smoker}, STROKE = {stroke},HeartDiseaseorAttack = {heartdisease}, PhysActivity = {phyact}, Fruits = {fruit}, Veggies = {vegetable}, HvyAlcoholConsump = {heavyalcoholcons},AnyHealthcare = {anyhealthcare}, NoDocbcCost = {nocostbcdoc}, GenHlth = {genhelth},MentHlth = {menhelth}, PhysHlth = {phyhelth}, DiffWalk = {diffwalk} WHERE patientinfo_id = {self.patientid}"
        user_id = self.result[0]
        con = Connection()
        input_list = []
        for key, value in input_data.items():
            input_list.append(value)
        input_list = [int(value) for value in input_list]
        pred=model.predict([input_list])
        print(pred)
        try:
            with con.cursor() as cursor:
                cursor.execute(query)
                con.commit()
                QMessageBox.information(None, 'Information', 'Saved successfully')
        except Exception as e:
            con.rollback()
            QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
        finally:
            con.close()
            self.hide()
            self.a=remarkspagerun(self.doc,self.docid,self.patientid,input_data,1,pred)
            self.a.show()
        

class Dashboardrun(QMainWindow):
    def __init__(self,doc=None,docid=None,search_value=None,search_term=None):
        super().__init__()
        self.doc=doc
        self.docid=docid
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        self.ui.logout_pushButton.clicked.connect(self.logout)
        self.ui.adddoctor_pushButton.clicked.connect(self.adddoctor)
        self.ui.addpatient_pushButton.clicked.connect(self.addpatient)
        self.ui.profile_pushButton.clicked.connect(self.profile)
        self.ui.search_pushButton.clicked.connect(self.searchrun)
        self.model = QStandardItemModel()
        self.username=self.ui.profile_label.text()
        self.ui.records_tableView.setModel(self.model)
        self.ui.records_tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if self.docid == None:
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"select id from doctor where username = ('{self.username}')")
                result = cursor.fetchone()
                self.docid=result[0]
            finally:
                cursor.close()
                con.close()    
        # print(type(self.docid))
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"select * from fyp.dashboard_view where doctor_id={self.docid};")
            self.data = cursor.fetchall()
            # print(self.data)
        finally:
            cursor.close()
            con.close()
        # print('value1 '+self.search_value)
        # print('term1 '+self.search_term)
        self.search()

        
    def viewpatient(self):
        self.hide()
        sender = self.sender()
        patient_id = sender.property("id")
        self.a=ViewPatientInforun(doc=self.doc,docid=self.docid,patient_id=patient_id)
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"SELECT * FROM patientinfo WHERE idinfo = ('{patient_id}')")
            result = cursor.fetchone()
        finally:
            cursor.close()
            con.close()
        self.a.ui.postal_out_label.setText(str(result[9]))
        self.a.ui.email_out_label.setText(str(result[10]))
        self.a.ui.phone_out_label.setText(str(result[11]))
        self.a.ui.income_out_label.setText(str(result[5]))
        self.a.ui.result_out_label.hide()
        self.a.ui.result_label.hide()
        self.a.ui.gender_out_label.setText(str(result[3]))
        self.a.ui.country_out_label.setText(str(result[7]))
        self.a.ui.education_out_label.setText(str(result[6]))
        self.a.ui.city_out_label.setText(str(result[8]))
        self.a.ui.age_out_label.setText(str(result[4]))
        self.a.ui.name_out_label.setText(str(result[1]) + " " + str(result[2]))
        self.a.show()
    
    def viewpatientmedical(self):
        self.hide()
        sender = self.sender()
        patient_id = sender.property("id")
        self.a=ViewPatientMedicalInforun(patient_id=patient_id,docid=self.docid,doc=self.doc)
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"SELECT * FROM patient WHERE patientinfo_id = ('{patient_id}')")
            result = cursor.fetchone()
        finally:
            # cursor.close()
            con.close()
        
        self.a.ui.bmi_out_label.setText(str(result[1]))
        self.a.ui.highbp_out_label.setText(str(result[2]))
        self.a.ui.highchol_out_label.setText(str(result[3]))
        self.a.ui.cholcheck_out_label.setText(str(result[4]))
        self.a.ui.smoker_out_label.setText(str(result[5]))
        self.a.ui.stroke_out_label.setText(str(result[6]))
        self.a.ui.heartdis_out_label.setText(str(result[7]))
        self.a.ui.phyact_out_label.setText(str(result[8]))
        self.a.ui.fruit_out_label.setText(str(result[9]))
        self.a.ui.veg_out_label.setText(str(result[10]))
        self.a.ui.heavyalcholcons_out_label.setText(str(result[11]))
        self.a.ui.anyhealthcare_out_label.setText(str(result[12]))
        self.a.ui.nodocbcost_out_label.setText(str(result[13]))
        self.a.ui.genhelth_out_label.setText(str(result[14]))
        self.a.ui.menhelth_out_label.setText(str(result[15]))
        self.a.ui.phyhelth_out_label.setText(str(result[16]))
        self.a.ui.diffwalk_out_label.setText(str(result[17]))
        self.a.show()
    
    def search(self):
       self.model.clear()
       headers = ["Name", "Age", "Patient ID", "Gender", "Result", "Remarks", "patient data", "medical data"]
       self.model.setHorizontalHeaderLabels(headers)

       for row_idx, row_data in enumerate(self.data):
           for col_idx, cell_data in enumerate(row_data):
               item = QStandardItem(str(cell_data))
               self.model.setItem(row_idx, col_idx, item)

           patient_data = QPushButton("patient data")
           medical_data = QPushButton("medical data")

           patient_data.clicked.connect(self.viewpatient)
           medical_data.clicked.connect(self.viewpatientmedical)
           
           patient_id=row_data[2]

           patient_data.setProperty("id", patient_id)
           medical_data.setProperty("id", patient_id)

           self.ui.records_tableView.setIndexWidget(self.model.index(row_idx, len(headers) - 2), patient_data)
           self.ui.records_tableView.setIndexWidget(self.model.index(row_idx, len(headers) - 1), medical_data)
        
        
        
    def logout(self):
        QMessageBox.information(None,'Information','logout sucessfully!!')
        self.close()
        self.a=loginrun()
        self.a.show()
    
    def adddoctor(self):
        self.a=signuprun(self.doc,self.docid)
        self.close()
        self.a.show()
    
    def addpatient(self):
        self.a=AddPatientInforun(self.doc,self.docid)
        self.close()
        self.a.show()
    
    def profile(self):
        self.close()
        self.username=self.ui.profile_label.text()
        self.a=ViewPatientInforun(doc=self.doc,docid=self.docid)
        self.a.setWindowTitle("Profile Info")
        self.a.ui.viewpatientinfo_label.setText("Profile Info")
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"SELECT * FROM doctor WHERE username = ('{self.username}')")
            result = cursor.fetchone()
        finally:
            cursor.close()
            con.close()
        self.a.ui.postal_out_label.setText(str(result[12]))
        self.a.ui.email_out_label.setText(str(result[6]))
        self.a.ui.phone_out_label.setText(str(result[13]))
        self.a.ui.income_out_label.setText(str(result[8]))
        self.a.ui.result_out_label.hide()
        self.a.ui.result_label.hide()
        self.a.ui.gender_out_label.setText(str(result[3]))
        self.a.ui.country_out_label.setText(str(result[11]))
        self.a.ui.education_out_label.setText(str(result[9]))
        self.a.ui.city_out_label.setText(str(result[10]))
        self.a.ui.age_out_label.setText(str(result[4]))
        self.a.ui.name_out_label.setText(str(result[1]) + " " + str(result[2]))
        self.a.show()
    
    def searchrun(self):
        self.search_value=self.ui.search_comboBox.currentText()
        self.search_term=self.ui.filter_lineEdit.text()
        docid=self.docid
        # print('value'+search_value)
        # print('term'+search_term)
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"select * from dashboard_view where doctor_id= {self.docid} and {self.search_value} LIKE '%{self.search_term}%';")
            # and {self.search_value} LIKE {self.search_term}
            self.data = cursor.fetchall()
        finally:
            cursor.close()
            con.close()
        self.search()
        # self.a=Dashboardrun(docid=docid,search_value=search_value,search_term=search_term)
        # self.close()
        # self.a.show()
        
    
class remarkspagerun(QWidget):
    def __init__(self,doc=None,docid=None,patid=None,input_data=None,edit=None,pred=None):
        super().__init__()
        self.edit=edit
        self.doc=doc
        self.docid=docid
        self.patid=patid
        self.input_data=input_data
        self.ui = Ui_remarkspage()
        self.ui.setupUi(self)
        self.ui.save_pushButton.clicked.connect(self.save)
        self.ui.back_pushButton.clicked.connect(self.back)
        doc=DOCTOR(docid=self.docid,patid=self.patid,input_data=self.input_data)
        print(pred)
        if pred ==None:
            self.pred=doc.Prediction()
            if self.pred==0:
                self.ui.predout_label.setText("You Are Safe!!")
                self.ui.remarks_textEdit.hide()
                self.ui.prescreption_label.hide()
            elif self.pred==1:
                self.ui.predout_label.setText("You Have Diabeties!!")
            else:
                QMessageBox.critical(None,"Prediction","prediction Error")
        else:
            self.pred=pred
            if self.pred==0:
                self.ui.predout_label.setText("You Are Safe!!")
                self.ui.remarks_textEdit.hide()
                self.ui.prescreption_label.hide()
            elif self.pred==1:
                self.ui.predout_label.setText("You Have Diabeties!!")
            else:
                QMessageBox.critical(None,"Prediction","prediction Error")

        
    def save(self):
        remarks = self.ui.remarks_textEdit.toPlainText()
        if self.edit==0:
            if self.pred==0:
                try:
                    con=Connection()
                    cursor=con.cursor()
                    cursor.execute(f"INSERT INTO result (doctor_id, resultcol, datetime,remarks,patient_id) VALUES ('{self.docid}','You are Safe','{datetime.datetime.now()}','{remarks}','{self.patid}')")
                    con.commit()
                    QMessageBox.information(None,"Congrats","Data saved successfully")
                    # print()
                except Exception as e:
                    con.rollback()
                    QMessageBox.information(None,"Error","Error occured")
                finally:
                    cursor.close()
                    con.close()
                    self.a=Dashboardrun(doc=self.doc,docid=self.docid)
                    self.a.setWindowTitle("Dashboard")
                    self.a.ui.profile_label.setText(self.doc.username)
                    self.a.ui.menu_label.setText("Dashboard")
                    self.close()
                    self.a.show()
            elif self.pred==1:
                remarks = self.ui.remarks_textEdit.toPlainText()
                try:
                    con=Connection()
                    cursor=con.cursor()
                    cursor.execute(f"INSERT INTO result (doctor_id, resultcol, datetime,remarks,patient_id) VALUES ('{self.docid}','You Have diabeties','{datetime.datetime.now()}','{remarks}','{self.patid}')")
                    con.commit()
                    QMessageBox.information(None,"Congrats","Data saved successfully")
                except Exception as e:
                    con.rollback()
                    QMessageBox.information(None,"Error","Error occurred")
                finally:
                    cursor.close()
                    con.close()
                    self.a=Dashboardrun(doc=self.doc,docid=self.docid)
                    self.a.setWindowTitle("Dashboard")
                    self.a.ui.profile_label.setText(self.doc.username)
                    self.a.ui.menu_label.setText("Dashboard")
                    self.close()
                    self.a.show()
        else:
            if self.pred==0:
                result='You are Safe'
            else:
                result='You have diabetes'
            query2 = f"UPDATE result SET resultcol = '{result}' , datetime = '{datetime.datetime.now()}', remarks = '{remarks}' WHERE patient_id = {self.patid}"
            try:
                con=Connection()
                cursor=con.cursor()
                cursor.execute(query2)
                con.commit()
                QMessageBox.information(None, 'Information', 'Updated successfully')
            except Exception as e:
                con.rollback()
                QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
            finally:
                    cursor.close()
                    con.close()
                    self.a=Dashboardrun(doc=self.doc,docid=self.docid)
                    self.a.setWindowTitle("Dashboard")
                    self.a.ui.profile_label.setText(self.doc.username)
                    self.a.ui.menu_label.setText("Dashboard")
                    self.close()
                    self.a.show()
            
    def back(self):
        if self.edit==0:
            self.close()
            self.a=AddPatientMedicalInforun(doc=self.doc,docid=self.docid,patid=self.patid)
            self.close()
            self.a.show()
        else:
            self.close()
            self.a=EditPatientMedicalInforun(doc=self.doc,docid=self.docid,patientid=self.patid)
            self.close()
            self.a.show()
        