from address import ADDRESS

class USER(ADDRESS):
    def __init__(self,fname=None,lname=None,phone=None,age=None,sex=None,education=None,income=None,email=None,username=None,password=None,city=None,country=None,postal_code=None) -> None:
        super().__init__(city,country,postal_code)
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.age=age
        self.education=education
        self.sex=sex
        self.income=income
        self.email=email
        self.username=username
        self.password=password