import json

class ConfigParser:
    def __init__(self, json_input):
        self.data = json.loads(json_input)

    def parse(self):
        return self.convert(self.data)

    def convert(self, data):
        if isinstance(data, dict):
            return self.convert_dict(data)
        elif isinstance(data, list):
            return self.convert_list(data)
        else:
            return f"[[{str(data)}]]"

    def convert_dict(self, data):
        result = ""
        for key, value in data.items():
            result += f"const {key} = {self.convert(value)}\n"
        return result

    def convert_list(self, data):
        result = "list("
        result += ', '.join([self.convert(item) for item in data])
        result += ")"
        return result

if __name__ == "__main__":
    import sys
    json_input = sys.stdin.read()
    parser = ConfigParser(json_input)
    result = parser.parse()

    with open("output.txt", "w") as file:
        file.write(result)
