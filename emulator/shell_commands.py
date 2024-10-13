import os
import sys

# Имитация файловой системы для примера
file_system = {
    'file1.txt': {'content': 'line1\nline2\nline2\nline3\nline1\n', 'owner': 'root'},
    'file2.txt': {'content': 'This is file 2', 'owner': 'root'},
    'dir': {
        'file1.txt': {'content': 'lineA\nlineB\nlineA\n', 'owner': 'root'},
        'file2.txt': {'content': 'This is another file in a directory', 'owner': 'root'}
    }
}

current_directory = "."  # Указывает на текущую директорию

# Хранит текущую имитацию файловой системы
virtual_file_system = {
    ".": file_system,
    "dir": file_system['dir']
}

def shell_commands(command, root):  # Добавили параметр root
    global current_directory
    commands = command.split()
    if not commands:
        return

    cmd = commands[0]

    if cmd == 'exit':
        exit_shell(root)  # Вызываем exit_shell с корнем
        return
    elif cmd == 'chown':
        if len(commands) != 3:
            return "Usage: chown <file_name> <new_owner>"
        else:
            return chown(commands[1], commands[2])
    elif cmd == 'ls':
        if len(commands) == 2 and commands[1] == '-l':
            return list_dir_detailed()
        else:
            return list_dir()
    elif cmd == 'cd':
        if len(commands) == 2:
            return change_dir(commands[1])
        else:
            return "Usage: cd <directory_name>"
    elif cmd == 'pwd':
        return pwd()
    elif cmd == 'uniq':
        if len(commands) == 2:
            return uniq(commands[1])
        else:
            return "Usage: uniq <file_name>"
    else:
        return f"Unknown command: {cmd}"

# Реализация команды ls
def list_dir():
    global current_directory
    files = virtual_file_system[current_directory]
    if files:
        return "Files: " + ", ".join(files.keys())
    else:
        return "No files in current directory."

# Реализация команды ls -l (подробный вывод)
def list_dir_detailed():
    global current_directory
    files = virtual_file_system[current_directory]
    if files:
        output = []
        for file_name, file_info in files.items():
            owner = file_info['owner']
            size = len(file_info['content'])
            output.append(f"-rw-r--r-- 1 {owner} {size} {file_name}")
        return "\n".join(output)
    else:
        return "No files in current directory."

# Реализация команды cd
def change_dir(directory_name):
    global current_directory
    if directory_name in virtual_file_system:
        current_directory = directory_name
        return f"Changed directory to: {current_directory}"
    else:
        return f"Directory {directory_name} not found."

# Реализация команды pwd
def pwd():
    global current_directory
    return f"Current directory: {current_directory}"

# Реализация команды exit
def exit_shell(root):
    print("Exiting the shell...")  # Печатаем сообщение
    root.destroy()  # Закрывает главное окно
    sys.exit()  # Завершает программу

# Реализация команды chown
def chown(file_name, new_owner):
    global current_directory
    files = virtual_file_system[current_directory]
    if file_name in files:
        files[file_name]['owner'] = new_owner
        return f"Changed owner of {file_name} to {new_owner}."
    else:
        return f"File {file_name} not found."

# Реализация команды uniq
def uniq(file_name):
    global current_directory
    file_path = os.path.join(current_directory, file_name)

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
                seen_lines = set()  # Множество для отслеживания уникальных строк
                unique_lines = []

                for line in lines:
                    stripped_line = line.strip()  # Убираем лишние пробелы и символы новой строки
                    if stripped_line and stripped_line not in seen_lines:  # Проверяем на пустую строку и уникальность
                        unique_lines.append(stripped_line)  # Добавляем очищенную строку в список уникальных
                        seen_lines.add(stripped_line)  # Помечаем строку как увиденную

                # Возвращаем уникальные строки, каждая с новой строки
                return "\n".join(unique_lines)  # Возвращаем уникальные строки
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        return f"File {file_name} not found."

# Пример использования в основном цикле
if __name__ == "__main__":
    running = True
    while running:
        command = input("Enter command: ")
        output = shell_commands(command)  # Получаем вывод команды
        print(output)  # Печатаем вывод
        if output == "Exiting the shell...":
            running = False
