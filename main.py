from excel_reader import ExcelReader
from docx_writer import DocxWriter
from docx2pdf import convert
import os
import sys
from patient import Patient

def get_all_files_in_directory(directory):
    file_info = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            name, extension = os.path.splitext(filename)
            file_info.append({'name': name, 'extension': extension})
    return file_info

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

    directory_path = 'dest'
    files_info = get_all_files_in_directory(directory_path)

    print("Files in '{}' directory:".format(directory_path))
    for file_info in files_info:
        print("Name: {}, Extension: {}".format(file_info['name'], file_info['extension']))

    convert(dest)

