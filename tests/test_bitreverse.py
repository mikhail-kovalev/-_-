# tests/test_bitreverse.py

import unittest
from emulator.bitreverse import bitreverse  # Импортируем функцию из bitreverse.py

class TestBitReverse(unittest.TestCase):
    
    def test_bitreverse(self):
        # Тестирование различных входных данных
        self.assertEqual(bitreverse(0b00000001), 0b10000000)  # 1 -> 128
        self.assertEqual(bitreverse(0b00000011), 0b11000000)  # Ожидаем 192
        self.assertEqual(bitreverse(0b11111111), 0b11111111)  # 255 -> 255
        self.assertEqual(bitreverse(0b00000000), 0b00000000)  # 0 -> 0
        self.assertEqual(bitreverse(0b10101010), 0b01010101)  # 170 -> 85

    def test_invalid_input(self):
        # Тестирование на исключение для недопустимого ввода
        with self.assertRaises(ValueError):
            bitreverse(-1)  # Значение вне диапазона
        with self.assertRaises(ValueError):
            bitreverse(256)  # Значение вне диапазона

if __name__ == '__main__':
    unittest.main()
