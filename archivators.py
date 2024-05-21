import zipfile
import os

def create_archive(open_file_str, extract_file, algor, compresslevel, password=None):
    if algor=="None":
        algorithm = zipfile.ZIP_STORED
    elif algor=="Deflated":
        algorithm = zipfile.ZIP_DEFLATED
    elif algor == "Bzip":
        algorithm = zipfile.ZIP_BZIP2
    elif algor == "lzma":
        algorithm = zipfile.ZIP_LZMA
    result = f"Уровень сжатия: {algorithm}, алгоритм: {compresslevel}\n"
    try:
        with zipfile.ZipFile(extract_file, 'w', compression=algorithm, compresslevel=compresslevel) as zip_file:
            # Если указан пароль, устанавливаем его для архива
            if password:
                zip_file.setpassword(password.encode())
            
            # Разделяем open_file_str на отдельные пути, если таковые имеются
            paths = open_file_str.split('\n')
            for path in paths:
                if os.path.isfile(path):
                    # Если это файл, добавляем его в архив
                    zip_file.write(path, arcname=os.path.basename(path))
                    result += f"Добавлен файл: {path}\n"
                elif os.path.isdir(path):
                    # Если это директория, добавляем все файлы и поддиректории в архив
                    for folder_name, sub_folders, filenames in os.walk(path):
                        for filename in filenames:
                            file_path = os.path.join(folder_name, filename)
                            # Вычисляем относительный путь файла внутри архива
                            arcname = os.path.relpath(file_path, path)
                            zip_file.write(file_path, arcname=arcname)
                            result += f"Добавлен файл: {file_path}\n"
                else:
                    result += f"Некорректный путь: {path}\n"
        
        result += "Архивация завершена.\n"
        
        # Вывод информации о размере сжатых данных после архивации
        with zipfile.ZipFile(extract_file, 'r') as zip_file:
            for info in zip_file.infolist():
                result += f"Имя файла: {info.filename}\n"
                result += f"Сжатый размер: {info.compress_size} байт\n"
                result += f"Изначальный размер размер: {info.file_size} байт\n"
                result += "---\n"
    except zipfile.BadZipFile as e:
        result += f"Ошибка при создании архива: {e}\n"
    except Exception as e:
        result += f"Произошла ошибка: {e}\n"
    
    return result
        

def extract_archive(open_file, extract_file, password):
    result = f"Извлечение файлов из архива: {open_file}\n"
    try:
        # Проверяем, является ли файл допустимым ZIP-архивом
        if not zipfile.is_zipfile(open_file):
            result += "Ошибка: файл не является допустимым ZIP-архивом.\n"
            return result

        with zipfile.ZipFile(open_file, 'r') as zip_file:
            if password:
                zip_file.setpassword(password.encode())
            zip_file.extractall(path=extract_file)
        result += "Файлы успешно извлечены.\n"
    except zipfile.BadZipFile as e:
        result += f"Ошибка при чтении архива: {e}\n"
    except RuntimeError as e:
        if 'password' in str(e):
            result += "Неверный пароль для архива.\n"
        else:
            result += f"Ошибка при извлечении файлов: {e}\n"
    except Exception as e:
        result += f"Произошла непредвиденная ошибка: {e}\n"
    return result