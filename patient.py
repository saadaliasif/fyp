from user import USER
from PySide6.QtWidgets import QMessageBox
import mysql.connector
from address import ADDRESS

class PATIENT(USER):
    def __init__(self,fname=None,lname=None,phone=None,age=None,sex=None,educ=None,income=None,email=None,username=None,password=None,
                 address=None,bmi=None,smoker=None,stroke=None,heartdiseaseorattack=None,physactivity=None,fruits=None,veggies=None,
                 heavyalcoholconsumption=None,anyhealthcare=None,nodocbccost=None,menthealth=None,physhealth=None,diffwalk=None,highchol=None,
                 genhealth=None,highbp=None,cholcheck=None,docid=None,patid=None) -> None:
        super().__init__(fname,lname,phone,age,sex,educ,income,email,username,password)
        self.patid=patid
        self.bmi=bmi
        self.smoker=smoker
        self.stroke=stroke
        self.heartdisease=heartdiseaseorattack
        self.physactivity=physactivity
        self.fruits=fruits
        self.veggies=veggies
        self.heavyalcohol=heavyalcoholconsumption
        self.anyhealthcare=anyhealthcare
        self.nodoc=nodocbccost
        self.menthealth=menthealth
        self.physhelth=physhealth
        self.diffwalk=diffwalk
        self.highchol=highchol
        self.genhelth=genhealth
        self.highbp=highbp
        self.cholcheck=cholcheck
        
    def Connection(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="fyp"
        )
        return mydb
        
    def ValidateData(self):
        pass
    
    def AddPatientMedicalInfo(self):
        con=self.Connection()
        mycursor = con.cursor()
        try:
            sql=f"INSERT INTO patient (BMI,SMOKER, STROKE,HeartDiseaseorAttack,PhysActivity,Fruits,Veggies,HvyAlcoholConsump,AnyHealthcare,NoDocbcCost,MentHlth,PhysHlth,DiffWalk,HIGH_CHOL,GenHlth,HIGH_BP,CHOL_CHECK,patientinfo_id) VALUES ('{self.bmi}', '{self.smoker}','{self.stroke}', '{self.heartdisease}','{self.physactivity}', '{self.fruits}','{self.veggies}', '{self.heavyalcohol}', '{self.anyhealthcare}', '{self.nodoc}', '{self.menthealth}', '{self.physhelth}', '{self.diffwalk}', '{self.highchol}', '{self.genhelth}', '{self.highbp}', '{self.cholcheck}','{self.patid}')"
            mycursor.execute(sql)
            con.commit()
        except Exception as e:
            con.rollback()
            QMessageBox.warning(None,"Login", "database error"+ str(e))
        finally:
            mycursor.close()
            con.close()    
        self.mes=QMessageBox.information(None,'Information','added sucessfully')
    
    def DellRecord(self):
        pass
        # record_id = input("Enter the ID of the record you want to delete: ")
        # con = self.Connection()
        # cursor = con.cursor()
        # try:
        #     sql = f"DELETE FROM fyp WHERE id = {record_id}"
        #     cursor.execute(sql)
        #     con.commit()
        # except Exception as e:
        #     con.rollback()
        # QMessageBox.warning(None,"Login", "database error"+ str(e))
        # finally:
        #     cursor.close()
        #     con.close()
        #     print("Record deleted successfully!")
    
    def EditRecord(self):
        pass
        # fname = input("Enter new first name (or leave blank to keep current): ")
        # lname = input("Enter new last name (or leave blank to keep current): ")
        # phone = input("Enter new phone no (or leave blank to keep current): ")
        # Editrecordpage=editrecordpage.Ui_addrecord()
        # self.bmi=Editrecordpage.bmi_lineEdit.text()
        # self.smoker=Editrecordpage.smoker_lineEdit.text()
        # self.stroke=Editrecordpage.stroke_lineEdit.text()
        # self.heartdiseaseorattack=Editrecordpage.heart_disease_or_attack_lineEdit.text()
        # self.physactivity=Editrecordpage.physactivity_lineEdit.text()
        # self.fruits=Editrecordpage.fruits_lineEdit.text()
        # self.veggies=Editrecordpage.veggies_lineEdit.text()
        # self.heavyalcoholconsumption=Editrecordpage.heavy_alcohol_consumption_lineEdit.text()
        # self.anyhealthcare=Editrecordpage.any_healthcare_lineEdit.text()
        # self.nodocbccost=Editrecordpage.no_doc_bc_cost_lineEdit.text()
        # self.menthealth=Editrecordpage.menthealth_lineEdit.text()
        # self.physhealth=Editrecordpage.physhealth_lineEdit.text()
        # self.diffwalk=Editrecordpage.diffwalk_lineEdit.text()
        # self.highchol=Editrecordpage.highchol_lineEdit.text()
        # self.genhealth=Editrecordpage.genhealth_lineEdit.text()
        # self.highbp=Editrecordpage.highbp_lineEdit.text()
        # self.cholcheck=Editrecordpage.cholcheck_lineEdit.text()
        # con = self.Connection()
        # cursor = con.cursor()
        # sql = f"SELECT * FROM fyp WHERE id = {record_id}"
        # cursor.execute(sql)
        # record = cursor.fetchone()

        # if not record:
        #     print("No record found with that ID.")
        #     return

        # # Build the SQL query string based on the user's input
        # sql_parts = []
        # if fname:
        #     sql_parts.append(f"fname = '{fname}'")
        # if lname:
        #     sql_parts.append(f"lname = '{lname}'")
        # if phone:
        #     sql_parts.append(f"phone = '{phone}'")

        # if not sql_parts:
        #     print("No changes specified.")
        #     return
        # try:
        #     sql = "UPDATE fyp SET " + ", ".join(sql_parts) + f" WHERE id = {record_id}"
        #     cursor.execute(sql)
        #     con.commit()
        # except Exception as e:
        #     con.rollback()
        # QMessageBox.warning(None,"Login", "database error"+ str(e))
        # finally:
        #     cursor.close()
        #     con.close()
        #     print("Record updated successfully!")
    
    def AddPatientInfo(self):
        print(self.docid)
        con=self.Connection()
        mycursor = con.cursor()
        try:
            sql=f"INSERT INTO patientinfo (first_name,last_name,email,phone,sex,age,income,education,city,country,postal_code,doctor_id) VALUES ('{self.fname}', '{self.lname}','{self.email}','{self.phone}', '{self.sex}','{self.age}', '{self.income}','{self.education}', '{self.city}','{self.country}', '{self.postal_code}', '{self.docid}')"
            mycursor.execute(sql)
            con.commit()
        except Exception as e:
            con.rollback()
            QMessageBox.warning(None,"Login", "database error"+ str(e))
        finally:
            mycursor.close()
            con.close()