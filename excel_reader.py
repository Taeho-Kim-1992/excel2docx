import pandas as pd
import os
from patient import Patient

RESOURCE_PATH = 'resources'
ROW_PATIENT_ADDRESS = 'Address'
ROW_PATIENT_NAME = 'Patient Name'
ROW_PATIENT_GENDER = 'Gender'
ROW_PATIENT_LAST_NAME = 'Last Name'
ROW_PATIENT_FIRST_NAME = 'First Name'
ROW_PATIENT_TEL = 'Tel'
ROW_PATIENT_DATE_OF_BIRTH = 'DOB'
ROW_PATIENT_EHR_ID = 'eHR-ID'
ROW_PATIENT_MED_NUMBER = 'Medicare No.'

class ExcelReader:

    @staticmethod
    def _get_patient_from_row(row):
        patient = Patient(
                address = row[ROW_PATIENT_ADDRESS],
                gender = row[ROW_PATIENT_GENDER],
                last_name = row[ROW_PATIENT_LAST_NAME],
                first_name = row[ROW_PATIENT_FIRST_NAME],
                ehr_id = row[ROW_PATIENT_EHR_ID],
                dob = row[ROW_PATIENT_DATE_OF_BIRTH],
                tel = row[ROW_PATIENT_TEL],
                medicare_number = row[ROW_PATIENT_MED_NUMBER]
                )

        return patient

    @staticmethod
    def _get_sheet_name(): 
        files = os.listdir('resources')
        excel_files = [file for file in files if file.endswith(".xlsx")]
        if len(excel_files) == 1:
            return excel_files[0]
        else:
            print('Please double check ~/resources directory')
            return None

    @staticmethod
    def get_patients(): 

        sheet_name = ExcelReader._get_sheet_name()

        print(f'Sheet :: {sheet_name}')
        df = pd.read_excel(f'{RESOURCE_PATH}/{sheet_name}', sheet_name = sheet_name.split('.')[0])

        patient_list = []

        # Patient 객체 생성
        for _, row in df.iterrows():
            patient = ExcelReader._get_patient_from_row(row)
            patient_list.append(patient)

        return patient_list
