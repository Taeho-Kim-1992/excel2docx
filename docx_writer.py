from patient import Patient
from docx import Document
from datetime import datetime

TEMPLATE_PATH = 'resources/emptyform.docx'

class DocxWriter:

    def __init__(self, patient):
        self.patient = patient

    @staticmethod
    def write_patient(patient, dest):
        doc = Document(TEMPLATE_PATH)
        patient.desc()

        for paragraph in doc.paragraphs:
            if 'Patient:' in paragraph.text:
                paragraph.text = f"Patient Name : {patient.get_full_name()} ({patient.get_patient_gender()})   EHR ID: {patient.ehr_id}"
            elif 'Patient Name : (Last, First)' in paragraph.text:
                paragraph.text = f"Patient Name : (Last, First) {patient.get_full_name()}"
            elif 'DOB :' in paragraph.text:
                paragraph.text = f"DOB : {patient.get_date_of_birth()}"
            elif 'Address :' in paragraph.text:
                paragraph.text = f"Address : {patient.address}"
            elif 'Tel :' in paragraph.text:
                paragraph.text = f"Tel : {patient.tel}"
            elif 'Medicare # :' in paragraph.text:
                paragraph.text = f"Medicare # : {patient.medicare_number}"
            elif 'Date :' in paragraph.text:
                sign_date = datetime.now().strftime('%m / %d / %Y')
                print(f'sign_date = {sign_date}')
                paragraph.text = f"Date : {sign_date}"

        # 채워진 정보를 새로운 파일로 저장
        output_path = f'{dest}/{patient.get_file_name()}.docx'
        doc.save(output_path)
        print(f"Filled form saved at: {output_path}")

