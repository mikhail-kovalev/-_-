import os
import subprocess

class DependencyGraph:
    def __init__(self, package_path, max_depth):
        self.package_path = package_path
        self.max_depth = max_depth
        self.dependencies = {}

    def parse_dependencies(self):
        # Простой парсер для requirements.txt
        with open(self.package_path, 'r') as file:
            for line in file.readlines():
                package = line.strip().split('==')[0]
                self.dependencies[package] = []

        # TODO: поддержка транзитивных зависимостей

    def generate_mermaid(self):
        graph = "graph TD;\n"
        for package, deps in self.dependencies.items():
            for dep in deps:
                graph += f"{package} --> {dep}\n"
        return graph

    def save_to_mermaid_file(self, file_path):
        graph = self.generate_mermaid()
        with open(file_path, 'w') as file:
            file.write(graph)

    def generate_png(self, mermaid_file, output_file):
        # Генерация PNG с помощью внешнего инструмента
        subprocess.run(["mmdc", "-i", mermaid_file, "-o", output_file])

if __name__ == "__main__":
    package_path = "requirements.txt"
    mermaid_file = "graph.mmd"
    output_file = "graph.png"
    max_depth = 3

    graph = DependencyGraph(package_path, max_depth)
    graph.parse_dependencies()
    graph.save_to_mermaid_file(mermaid_file)
    graph.generate_png(mermaid_file, output_file)
