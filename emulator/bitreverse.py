# emulator/bitreverse.py

def bitreverse(num):
    if not (0 <= num < 256):
        raise ValueError("Input must be a byte (0-255).")
    
    result = 0
    for i in range(8):  # Предполагаем, что num - 8-битное число
        result <<= 1  # Сдвигаем результат влево
        result |= (num & 1)  # Берем последний бит num и добавляем его к результату
        num >>= 1  # Сдвигаем num вправо
    return result

