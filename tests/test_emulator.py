import os
import tempfile
import unittest
from emulator.filesystem import VirtualFileSystem  # Обновите путь импорта, если необходимо

class TestEmulator(unittest.TestCase):

    def setUp(self):
        # Создание временного ZIP файла и автоматическое его закрытие
        self.test_zip_path = tempfile.NamedTemporaryFile(delete=False, suffix='.zip').name
        with open(self.test_zip_path, 'w') as f:
            f.write('')  # Можно заполнить его данными, если нужно

        self.fs = VirtualFileSystem(self.test_zip_path)


    def tearDown(self):
        # Удаляем временный файл zip
        try:
            os.remove(self.test_zip_path)
        except OSError:
            pass  # Игнорируем ошибки удаления, если файл занят

    def test_change_dir(self):
        self.assertTrue(self.fs.change_dir('dir'))  # Проверяем изменение директории

    def test_current_dir(self):
        self.fs.change_dir('dir')
        self.assertEqual(self.fs.get_current_dir(), 'dir')  # Проверяем текущую директорию

    def test_list_dir(self):
        self.fs.change_dir('dir')
        self.assertIn('dir/file1.txt', self.fs.list_dir())  # Проверяем, что файл есть в списке
