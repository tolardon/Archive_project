import zipfile
import os

def create_archive(open_file, extract_file, algorithm, compresslevel):
    with zipfile.ZipFile(extract_file, 'w', compression=algorithm, compresslevel=compresslevel) as zip_file:
        if os.path.isfile(open_file):
            zip_file.write(open_file)
        
        elif os.path.isdir(open_file):
            for folder_name, sub_folders, filenames in os.walk(open_file):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    zip_file.write(file_path)
        else:
            print("error")
    
    print("Архив успешно создан!")


def extract_archive(open_file, extract_file, password):
    with zipfile.ZipFile(open_file, 'r') as zip_file:
        if zipfile.is_zipfile(open_file):
            zip_file.extractall(extract_file, pwd=password)
    
    print("Архив успешно распакован!")