class Assembler:
    def __init__(self, source_file):
        self.source_file = source_file

    def assemble(self):
        with open(self.source_file, 'r') as file:
            instructions = file.readlines()

        # Преобразование инструкций в бинарный код
        binary_code = []
        for instr in instructions:
            binary_code.append(self.convert_to_binary(instr))
        return binary_code

    def convert_to_binary(self, instr):
        # Простая конвертация для демонстрации
        return bytes(instr.strip(), 'utf-8')

    def save_binary(self, output_file, binary_code):
        with open(output_file, 'wb') as file:
            file.write(b'\n'.join(binary_code))

if __name__ == "__main__":
    asm = Assembler("program.asm")
    binary = asm.assemble()
    asm.save_binary("program.bin", binary)
