class Interpreter:
    def __init__(self, binary_file):
        self.binary_file = binary_file
        self.memory = [0] * 1024

    def load_binary(self):
        with open(self.binary_file, 'rb') as file:
            self.instructions = file.readlines()

    def execute(self):
        for instr in self.instructions:
            self.execute_instruction(instr)

    def execute_instruction(self, instr):
        # Простейшее выполнение команды
        print(f"Executing {instr}")

if __name__ == "__main__":
    interpreter = Interpreter("program.bin")
    interpreter.load_binary()
    interpreter.execute()
