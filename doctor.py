from user import USER
from PySide6.QtWidgets import QWidget,QMessageBox
import mysql.connector
import hashlib
import joblib
class DOCTOR(USER):      
    def __init__(self, fname=None, lname=None, phone=None, age=None, sex=None, 
                 education=None, income=None, email=None, username=None, 
                 password=None, city=None, country=None, postal_code=None, 
                 confirm_password=None,docid=None,remarks=None,patid=None,input_data=None):
        super().__init__(fname, lname, phone, age, sex, education, income, email, 
                         username, password)
        self.docid=docid
        self.patid=patid
        self.input_data=input_data
        print(self.input_data)
        print(input_data)
        self.model = joblib.load("model.pkl")
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="fyp"
        )
        
    def Prediction(self):
        input_list = []
        for key, value in self.input_data.items():
            input_list.append(value)
        input_list = [int(value) for value in input_list]
        # print(input_list)
        pred=self.model.predict([input_list])
        print(pred)
        return pred

    def Login(self):
        hashed_password = hashlib.md5(self.password.encode('utf-8')).hexdigest()   
        cursor = self.mydb.cursor()
        try:
            sql = "SELECT * FROM doctor WHERE username = %s AND password = %s"
            values = (self.username, hashed_password)
            cursor.execute(sql, values)
            result = cursor.fetchone()
        finally:
            cursor.close()
            self.mydb.close()
        
        if result is None:
            QMessageBox.information(None,'Information','user not found with these credentials!')
            return 0
        else:      
            QMessageBox.information(None,'Information','loggedin sucessfully!')
            return 1
            
    
    def Signup(self):
        if self.password != self.confirm_password:
            QMessageBox.warning(None,"Login", "password doesn't match")
            return 0    
        hashed_password = hashlib.md5(self.password.encode('utf-8')).hexdigest()    
        cursor = self.mydb.cursor()
        try:
            sql = f"INSERT INTO doctor (first_name,last_name,age,sex,education,income,city,country,postal_code,username, email, password,phone) VALUES ('{self.fname}','{self.lname}','{self.age}','{self.sex}','{self.education}','{self.income}','{self.city}','{self.country}','{self.postal_code}','{self.username}','{self.email}','{hashed_password}','{self.phone}')"
            cursor.execute(sql)
            self.mydb.commit()
            return 1
        except Exception as e:
            self.mydb.rollback()
            QMessageBox.warning(None,"Login", "database error"+ str(e))
            return 0
        finally:
            cursor.close()
            self.mydb.close()