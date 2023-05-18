from PySide6.QtWidgets import QWidget,QMessageBox,QMainWindow,QTableView, QPushButton
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem
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
import datetime
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


class loginrun(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginpage()
        self.ui.setupUi(self)
        self.ui.signin_pushButton.clicked.connect(self.run)
        
    def run(self):
        doc=DOCTOR()
        doc.username=self.ui.username_lineEdit.text()
        doc.password=self.ui.password_lineEdit.text()
        res=doc.Login()
        if res == 0:
            pass
        else:
            self.hide()
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"SELECT id FROM doctor WHERE username = ('{doc.username}')")
                result = cursor.fetchone()
                docid=result[0]
                # print('talha'+str(docid))
            finally:
                cursor.close()
                con.close()
            self.a=Dashboardrun(doc=doc,docid=docid)
            self.a.setWindowTitle("Dashboard")
            self.a.ui.profile_label.setText(doc.username)
            self.a.ui.menu_label.setText("Dashboard")
            self.a.show()

class signuprun(QWidget):
    def __init__(self,doc,docid=None):
        super().__init__()
        self.doc=doc
        self.ui = Ui_signuppage()
        self.ui.setupUi(self)
        self.ui.signup_pushButton.clicked.connect(self.run)
        self.docid=docid
        
    def run(self):
        doc=DOCTOR()
        doc.fname=self.ui.first_name_lineEdit.text()
        doc.lname=self.ui.last_name_lineEdit.text()
        doc.age=self.ui.age_lineEdit.text()
        doc.sex=self.ui.sex_lineEdit.text()
        doc.phone=self.ui.phone_lineEdit.text()
        doc.education=self.ui.education_lineEdit.text()
        doc.income=self.ui.income_lineEdit.text()
        doc.city=self.ui.city_lineEdit.text()
        doc.country=self.ui.country_lineEdit.text()
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
            self.a.ui.profile_label.setText(doc.username)
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

        
    def run(self):
        pat=PATIENT(self.docid)
        pat.fname=self.ui.first_name_lineEdit.text()
        pat.lname=self.ui.last_name_lineEdit.text()
        pat.age=self.ui.age_lineEdit.text()
        pat.city=self.ui.city_lineEdit.text()
        pat.country=self.ui.country_lineEdit.text()
        pat.education=self.ui.education_lineEdit.text()
        pat.email=self.ui.email_lineEdit.text()
        pat.phone=self.ui.phone_lineEdit.text()
        pat.sex=self.ui.sex_lineEdit.text()
        pat.postal_code=self.ui.postal_code_lineEdit.text()
        pat.docid=self.docid
        pat.income=self.ui.income_lineEdit.text()
        pat.AddPatientInfo()
        self.hide()
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute("SELECT idinfo FROM patientinfo ORDER BY idinfo DESC LIMIT 1")
            result = cursor.fetchall()
            patid=int(result[0][0])
            # print('hello1 '+str(patid))
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
        # print('t1:'+patid)
        if self.sex == "male" or self.sex == "Male" or self.sex == "MALE":
            self.sex=1
        if self.sex == "female" == self.sex == "Female" == self.sex == "FEMALE":
            self.sex=2
        self.age=age
        self.ui = Ui_addpatientmedicalinfopage()
        self.ui.setupUi(self)
        self.ui.addpatientmedicalinfo_pushButton.clicked.connect(self.run)
        
    def run(self):
        pat=PATIENT(patid=self.patid,docid=self.docid)
        pat.bmi=self.ui.bmi_lineEdit.text()
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
        pat.nodoc=y
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
            "Education": '4',
            "Income": self.income
            }
            pat.AddPatientMedicalInfo()
            self.hide()
            self.a=remarkspagerun(self.doc,self.docid,self.patid,input_data)
            # print(input_data)
            self.a.show()
        else:
            QMessageBox.critical(None,'selection error','you missed something')

class ViewPatientInforun(QWidget):
    def __init__(self,pid=None,doc=None,patient_id=None,docid=None):
        super().__init__()
        self.id=pid
        self.doc=doc
        self.docid=docid
        self.ui = Ui_viewpatientinfopage()
        self.ui.setupUi(self)
        self.patient_id=patient_id
        self.ui.edit_pushButton.clicked.connect(self.edit)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.ui.delete_pushButton.clicked.connect(self.delete)
        # print(self.username)

        
    def edit(self):
        self.hide()
        self.a=EditPatientInforun(pid=self.id,doc=self.doc,docid=self.docid)
        self.a.show()
        
    def delete(self):
        con =Connection()
        cursor=con.cursor()
        try:
            cursor.execute(f"DELETE FROM patientinfo where idinfo = ({self.patient_id})")
            cursor.execute(f"DELETE FROM patientinfo where patientinfo_id = ({self.patient_id})")
        finally:
            cursor.close()
            con.close()
        
    def back(self):
        # doc=DOCTOR()
        self.a=Dashboardrun(doc=self.doc,docid=self.docid)
        self.a.setWindowTitle("Dashboard")
        self.a.ui.profile_label.setText(self.doc.username)
        self.a.ui.menu_label.setText("Dashboard")
        self.close()
        self.a.show()

class ViewPatientMedicalInforun(QWidget):
    def __init__(self,doc=None,patient_id=None,docid=None):
        super().__init__()
        self.doc=doc
        self.ui = Ui_viewpatientmedicalinfopage()
        self.ui.setupUi(self)
        self.patient_id=patient_id
        self.ui.delete_pushButton.clicked.connect(self.delete)
        self.ui.edit_pushButton.clicked.connect(self.edit)
        self.ui.back_pushButton.clicked.connect(self.back)

        
    def edit(self):
        self.hide()
        self.a=EditPatientMedicalInforun(doc=self.doc,docid=self.docid)
        self.a.show()
        
    def delete(self):
        pass

    def back(self):
        doc=DOCTOR()
        self.a=Dashboardrun(docid=self.docid)
        self.a.setWindowTitle("Dashboard")
        self.a.ui.profile_label.setText(doc.username)
        self.a.ui.menu_label.setText("Dashboard")
        self.close()
        self.a.show()

class EditPatientInforun(QWidget):
    def __init__(self,pid=None,doc=None,docid=None):
        super().__init__()
        self.id=pid
        self.doc=doc
        self.docid=docid
        self.ui = Ui_editpatientinfopage()
        self.ui.setupUi(self)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.ui.save_pushButton.clicked.connect(self.save)
        # print(self.username)
        
    def back(self):
        self.hide()
        if self.id is None:
            self.a=ViewPatientInforun(doc=self.doc,docid=self.docid)
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
            self.a=ViewPatientInforun(pid=self.id,doc=self.doc,docid=self.docid)
            self.a.setWindowTitle("Patient Profile Info")
            self.a.ui.viewpatientinfo_label.setText("Patient Profile Info")
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"SELECT * FROM patientinfo WHERE idinfo = ('{self.id}')")
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
        self.mes=QMessageBox.information(None,'Information','saved sucessfully')

class EditPatientMedicalInforun(QWidget):
    def __init__(self,doc=None,docid=None):
        super().__init__()
        self.doc=doc
        self.docid=docid
        self.ui = Ui_editpatientmedicalinfopage()
        self.ui.setupUi(self)
        self.ui.back_pushButton.clicked.connect(self.back)
        self.ui.save_pushButton.clicked.connect(self.save)
        
    def back(self):
        self.hide()
        self.a=ViewPatientMedicalInforun(doc=self.doc,docid=self.docid)
        self.a.show()

    def save(self):
        self.mes=QMessageBox.information(None,'Information','saved sucessfully')
        

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
        self.ui.menu_pushButton.clicked.connect(self.menu)
        self.ui.search_pushButton.clicked.connect(self.searchrun)
        self.model = QStandardItemModel()
        self.username=self.ui.profile_label.text()
        # self.search_value=search_value
        # self.search_term=search_term
        # print(self.search_tedorm)
        # print('username'+self.username)
        self.ui.records_tableView.setModel(self.model)
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
        self.a=ViewPatientInforun(pid=patient_id,doc=self.doc,docid=self.docid,patient_id=patient_id)
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
        self.a=ViewPatientMedicalInforun(patient_id=patient_id,docid=self.docid)
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
           patient_data.setFixedSize(80, 30)
           medical_data.setFixedSize(80, 30)

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
        self.a.setWindowTitle("Doctor Profile Info")
        self.a.ui.viewpatientinfo_label.setText("Doctor Profile Info")
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
        # self.a.ui.edit_pushButton.clicked.connect(ed())
        # def ed(self):
        #     self.hide()
        #     self.b=EditPatientInforun()
        #     self.b.setWindowTitle("edit doctor info")
        #     self.b.ui.editpatientinfo_label.setText("edit doctor info")
        #     self.b.ui.age_lineEdit.setText(str(result[4]))
        #     self.b.ui.city_lineEdit.setText(str(result[10]))
        #     self.b.ui.name_lineEdit.setText(str(result[1]) + " " + str(result[2]))
        #     self.b.ui.income_lineEdit.setText(str(result[8]))
        #     self.b.ui.country_lineEdit.setText(str(result[11]))
        #     self.b.ui.educ_lineEdit.setText(str(result[9]))
        #     self.b.ui.email_lineEdit.setText(str(result[6]))
        #     self.b.ui.phone_lineEdit.setText(str(result[13]))
        #     self.b.ui.postal_lineEdit.setText(str(result[12]))
        #     self.b.show()
    
    def menu(self):
        pass
    
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
    def __init__(self,doc=None,docid=None,patid=None,input_data=None):
        super().__init__()
        self.doc=doc
        self.docid=docid
        self.patid=patid
        self.input_data=input_data
        # print(input_data)
        # print(patid)
        # print(docid)
        self.ui = Ui_remarkspage()
        self.ui.setupUi(self)
        self.ui.save_pushButton.clicked.connect(self.save)
        self.ui.back_pushButton.clicked.connect(self.back)
        doc=DOCTOR(docid=self.docid,patid=self.patid,input_data=self.input_data)
        self.pred=doc.Prediction()
        if self.pred==0:
            self.ui.predout_label.setText("You Are Safe!!")
        elif self.pred==1:
            self.ui.predout_label.setText("You Have Diabeties!!")
        else:
            QMessageBox.critical(None,"Prediction","prediction Error")

        
    def save(self):
        if self.pred==0:
            remarks = self.ui.remarks_textEdit.toPlainText()
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"INSERT INTO result (doctor_id, resultcol, datetime,remarks,patient_id) VALUES ('{self.docid}','You are Safe','{datetime.datetime.now()}','{remarks}','{self.patid}')")
                con.commit()
                QMessageBox.information(None,"Congrats","Data saved successfully")
                # print()
            except Exception as e:
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
            con =Connection()
            cursor=con.cursor()
            try:
                cursor.execute(f"INSERT INTO result (doctor_id, resultcol, datetime,remarks,patient_id) VALUES ('{self.docid}','You Have Diabeties!!','{datetime.datetime.now()}','{remarks}','{self.patid}')")
                con.commit()
                QMessageBox.information(None,"Congrats","Data saved successfully")
            except Exception as e:
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
            
    def back(self):
        self.close()
        self.a=AddPatientMedicalInforun(doc=self.doc,docid=self.docid,patid=self.patid)
        self.close()
        self.a.show()
        
        
        
        