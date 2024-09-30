import zipfile
import os

# Название ZIP-файла
zip_filename = "file.zip"

# Создание файлов file1.txt и file2.txt в папке dir
os.makedirs("dir", exist_ok=True)  # Создаем папку dir, если она не существует
with open("dir/file1.txt", "w") as f1:
    f1.write("This is the content of file1.txt")

with open("dir/file2.txt", "w") as f2:
    f2.write("This is the content of file2.txt")

# Создание ZIP-архива
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write("dir/file1.txt")
    zipf.write("dir/file2.txt")

print(f"{zip_filename} успешно создан с файлами file1.txt и file2.txt.")
