import sys
import csv
import zipfile
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QLabel

from filesystem import VirtualFileSystem
from shell_commands import ShellCommands

class ShellEmulator(QWidget):
    def __init__(self, config_file):
        super().__init__()
        self.initUI()
        self.load_config(config_file)
        self.commands = ShellCommands(self.fs, self.username, self.log_file)

    def initUI(self):
        self.layout = QVBoxLayout()

        self.prompt = QLabel('Shell > ')
        self.layout.addWidget(self.prompt)

        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.layout.addWidget(self.console)

        self.input = QLineEdit()
        self.input.returnPressed.connect(self.execute_command)
        self.layout.addWidget(self.input)

        self.setLayout(self.layout)
        self.setWindowTitle('Shell Emulator')
        self.show()

    def execute_command(self):
        command = self.input.text()
        self.console.append(f"{self.username}@shell: {command}")
        self.input.clear()

        # Обработка команды
        output = self.commands.execute(command)
        self.console.append(output)  # Вывод результата команды

        # Логирование команды
        with open(self.log_file, mode='a') as log:
            writer = csv.writer(log)
            writer.writerow([self.username, command])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    config_file = 'config.csv'  # путь к конфигурационному файлу
    emulator = ShellEmulator(config_file)
    sys.exit(app.exec_())
