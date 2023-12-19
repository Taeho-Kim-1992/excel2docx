import re
from datetime import datetime 

class Patient:

    def __init__(self, address, gender, last_name, first_name, dob, ehr_id, tel, medicare_number):
        self.address = str(address)
        self.gender = str(gender)
        self.last_name = str(last_name)
        self.first_name = str(first_name)
        self.ehr_id = str(ehr_id)
        self.dob = str(dob)
        self.tel = str(tel)
        self.medicare_number = str(medicare_number)

    def desc(self):
        print(f"Gender: {self.gender} [{self.get_patient_gender()}]")
        print(f"Address :: {self.address}")
        print(f"Full name :: {self.get_full_name()}")
        print(f"EHR ID :: {self.ehr_id}")
        print(f"DOB: {self.dob}")
        print(f"Tel: {self.tel}")
        print(f"Medicare number: # {self.medicare_number}")

    def get_patient_gender(self):
        return self.gender[0].upper()

    def get_file_name(self):
        full_name = f'{self.last_name}, {self.first_name}'
        return re.sub(r'\s', '', full_name.upper())

    def get_full_name(self):
        # return f'{self.last_name}, {self.first_name}'
        return f'{self.last_name}, {self.first_name}'.upper()

    def get_date_of_birth(self): 
        original_date = datetime.strptime(self.dob, '%Y-%m-%d %H:%M:%S')
        us_date_format = original_date.strftime('%m/%d/%Y')
        return us_date_format

