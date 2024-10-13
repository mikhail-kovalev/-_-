import tkinter as tk
from tkinter import scrolledtext
from shell_commands import shell_commands  # Импортируем вашу логику команд

class ShellEmulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shell Emulator")

        # Настройка текстовой области для вывода результата команд
        self.console = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled')
        self.console.grid(row=0, column=0, padx=10, pady=10)

        # Поле для ввода команд
        self.command_entry = tk.Entry(root, width=80)
        self.command_entry.grid(row=1, column=0, padx=10, pady=5)
        self.command_entry.bind('<Return>', self.execute_command)  # Привязываем нажатие Enter к функции

        # Кнопка выполнения команд
        self.execute_button = tk.Button(root, text="Execute", command=self.execute_command)
        self.execute_button.grid(row=2, column=0, padx=10, pady=5)

    def execute_command(self, event=None):
        # Получаем команду из поля ввода
        command = self.command_entry.get()

        # Добавляем команду в консоль
        self._append_console(f"User@Shell: {command}")

        # Очищаем поле ввода
        self.command_entry.delete(0, tk.END)

        # Выполняем команду через функцию shell_commands
        output = shell_commands(command, self.root)  # Передаем root в функцию shell_commands

        # Отображаем результат выполнения команды в консоли
        self._append_console(output)

    def _append_console(self, text):
        # Включаем возможность записи в текстовую область (по умолчанию она "disabled")
        self.console['state'] = 'normal'

        # Добавляем текст в консоль и прокручиваем вниз
        self.console.insert(tk.END, text + "\n")
        self.console.see(tk.END)

        # Отключаем возможность редактирования текста пользователем
        self.console['state'] = 'disabled'


def exit_shell(root):
    root.destroy()  # Закрывает главное окно


# Основная функция для запуска приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = ShellEmulatorApp(root)
    root.mainloop()
