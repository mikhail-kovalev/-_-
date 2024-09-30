# emulator/filesystem.py
import zipfile
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
import tempfile

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.current_dir = 'dir'  # Изменяем на 'dir', чтобы начать с папки с файлами
        self._create_zip()

    def _create_zip(self):
        with zipfile.ZipFile(self.zip_path, 'w') as z:
            z.writestr('dir/file1.txt', 'Test file content')  # Запись тестового файла
            z.writestr('dir/file2.txt', 'Another test file')  # Второй файл

    def change_dir(self, dir_name):
        if dir_name == 'dir':
            self.current_dir = dir_name
            return True
        return False

    def get_current_dir(self):
        return self.current_dir

    def list_dir(self):
        if self.current_dir == 'dir':
            return ['file1.txt', 'file2.txt']  # Возвращаем имена файлов в текущем каталоге
        return []

    def chown(self, file_name, new_owner):
        # Здесь мы просто симулируем изменение владельца
        return f"Changed owner of {file_name} to {new_owner}."

    def uniq(self, file_name):
        # Симулируем чтение уникальных строк из файла
        if file_name == 'file1.txt':
            return "Unique content from file1.txt"
        return f"File {file_name} not found."


class EmulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CMD Emulator")

        # Текстовая область для вывода
        self.output_area = scrolledtext.ScrolledText(root, width=50, height=20)
        self.output_area.pack()

        # Поле ввода для команд
        self.command_entry = tk.Entry(root, width=50)
        self.command_entry.pack()

        # Кнопка для выполнения команды
        self.execute_button = tk.Button(root, text="Выполнить", command=self.execute_command)
        self.execute_button.pack()

        # Создаем экземпляр виртуальной файловой системы
        self.fs = VirtualFileSystem(zip_path=tempfile.NamedTemporaryFile(delete=False, suffix='.zip').name)

    def execute_command(self):
        command = self.command_entry.get()
        self.output_area.insert(tk.END, f"> {command}\n")  # Отображаем введенную команду
        
        # Обработка команд
        if command.startswith("cd "):
            dir_name = command[3:]
            if self.fs.change_dir(dir_name):
                self.output_area.insert(tk.END, f"Changed directory to: {dir_name}\n")
            else:
                self.output_area.insert(tk.END, f"Failed to change directory to: {dir_name}\n")
        
        elif command == "ls":
            files = self.fs.list_dir()
            if files:
                self.output_area.insert(tk.END, f"Files: {', '.join(files)}\n")
            else:
                self.output_area.insert(tk.END, "No files in current directory.\n")

        elif command == "pwd":
            current_dir = self.fs.get_current_dir()
            self.output_area.insert(tk.END, f"Current directory: {current_dir}\n")

        elif command.startswith("chown "):
            parts = command.split()
            if len(parts) == 3:
                file_name = parts[1]
                new_owner = parts[2]
                result = self.fs.chown(file_name, new_owner)
                self.output_area.insert(tk.END, f"{result}\n")
            else:
                self.output_area.insert(tk.END, "Usage: chown <file_name> <new_owner>\n")

        elif command.startswith("uniq "):
            file_name = command[5:]
            result = self.fs.uniq(file_name)
            self.output_area.insert(tk.END, f"{result}\n")

        elif command == "exit":
            self.root.quit()  # Закрываем приложение
            self.output_area.insert(tk.END, "Exiting the emulator.\n")

        else:
            self.output_area.insert(tk.END, "Unknown command.\n")

        # Очищаем поле ввода
        self.command_entry.delete(0, tk.END)

# Создаем главное окно
root = tk.Tk()
app = EmulatorGUI(root)
root.mainloop()