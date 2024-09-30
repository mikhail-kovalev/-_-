import os

# Имитация файловой системы для примера
file_system = {
    'file1.txt': 'This is file 1',
    'file2.txt': 'This is file 2',
    'dir': {
        'file1.txt': 'This is a file in a directory',
        'file2.txt': 'This is another file in a directory'
    }
}

current_directory = "."  # Указывает на текущую директорию

# Хранит текущую имитацию файловой системы
virtual_file_system = {
    ".": file_system,
    "dir": file_system['dir']
}

def shell_commands(command):
    global current_directory
    commands = command.split()
    if not commands:
        return

    cmd = commands[0]

    if cmd == 'exit':
        return exit_shell()
    elif cmd == 'chown':
        if len(commands) != 3:
            return "Usage: chown <file_name> <new_owner>"
        else:
            return chown(commands[1], commands[2])
    elif cmd == 'ls':
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
def exit_shell():
    return "Exiting the shell..."

# Реализация команды chown
def chown(file_name, new_owner):
    global current_directory
    files = virtual_file_system[current_directory]
    if file_name in files:
        return f"Changed owner of {file_name} to {new_owner}."
    else:
        return f"File {file_name} not found."

# Реализация команды uniq
def uniq(file_name):
    global current_directory
    if file_name in virtual_file_system[current_directory]:
        contents = virtual_file_system[current_directory][file_name]
        unique_lines = set(contents.splitlines())
        return "Unique lines in file:\n" + "\n".join(unique_lines)
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
