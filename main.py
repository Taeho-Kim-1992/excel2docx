import os
import sys
from excel_reader import ExcelReader
from docx_writer import DocxWriter
from docx2pdf import convert
from patient import Patient

if __name__ == '__main__':
    patients = ExcelReader.get_patients()

    result = 'result'

    # set patient data into docx file
    for patient in patients:
        docx = DocxWriter(patient)
        docx.write_patient(patient, result)

    print('converting docx file to pdf')
    convert(result)

