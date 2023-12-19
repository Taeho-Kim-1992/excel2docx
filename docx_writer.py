from patient import Patient
from docx import Document

TEMPLATE_PATH = 'resources/emptyform.docx'

class DocxWriter:

    def __init__(self, patient):
        self.patient = patient

    @staticmethod
    def read_all_text():
        doc = Document(TEMPLATE_PATH)

        for paragraph in doc.paragraphs:
            print(paragraph.text)


    @staticmethod
    def write_patient(patient):
        doc = Document(TEMPLATE_PATH)

        for paragraph in doc.paragraphs:
            if 'Patient:' in paragraph.text:
                paragraph.text = f"Patient Name : {patient.get_full_name()} ({patient.get_patient_gender()})   EHR ID: {patient.ehr_id}"
            elif 'Patient Name : (Last, First)' in paragraph.text:
                paragraph.text = f"Patient Name : (Last, First) {patient.last_name}, {patient.first_name}"
            elif 'DOB :' in paragraph.text:
                paragraph.text = f"DOB : {patient.dob}"
            elif 'Address :' in paragraph.text:
                paragraph.text = f"Address : {patient.address}"
            elif 'Tel :' in paragraph.text:
                paragraph.text = f"Tel : {patient.tel}"
            elif 'Medicare # :' in paragraph.text:
                paragraph.text = f"Medicare # : {patient.medicare_number}"

        # 채워진 정보를 새로운 파일로 저장
        output_path = f'dest/{patient.get_file_name()}.docx'
        doc.save(output_path)
        print(f"Filled form saved at: {output_path}")

