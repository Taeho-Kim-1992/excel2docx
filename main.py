from excel_reader import ExcelReader
from docx_writer import DocxWriter
from docx2pdf import convert
import os
from patient import Patient

if __name__ == '__main__':
    patients = ExcelReader.get_patients()

    # set patient data into docx file
    for patient in patients:
        docx = DocxWriter(patient)
        docx.write_patient(patient)

    print(f'patient from excel :: {len(patients)} files done!')

    destination_dir = os.listdir('dest')
    docx_files = [file for file in destination_dir if file.endswith('.docx')]

    for docx_file in docx_files:
        print(docx_file)
        convert(f'dest/{docx_file}.docx', f'dest/{docx_file}.pdf')

