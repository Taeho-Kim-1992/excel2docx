from excel_reader import ExcelReader
from docx_writer import DocxWriter
from docx2pdf import convert
import os
import sys
from patient import Patient

if __name__ == '__main__':
    sheet_name = input('Enter Excel sheet name : ')
    patients = ExcelReader.get_patients(sheet_name)

    destination_dir = input('Enter docs file destination : ')

    if destination_dir:
        dest = 'destination_dir'
    else:
        dest = 'dest'

    # set patient data into docx file
    for patient in patients:
        docx = DocxWriter(patient)
        docx.write_patient(patient, dest)

    print(f'patient from excel :: {len(patients)} files done!')
