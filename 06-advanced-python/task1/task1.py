"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""

import os


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        depth_project = self.name.count(os.path.sep) + 1
        result = 'V ' + os.path.basename(self.name) + '\n'
        for root, _, files in self.content:
            depth_root = len(root.split(os.sep))
            result += (depth_root - depth_project - 1) * '|\t' + '|-> V ' + os.path.basename(root) + '\n'
            for file in files:
                result += (depth_root - depth_project) * '|\t' + str(PrintableFile(file)) + '\n'
        return result

    def __contains__(self, file):
        return [True for _, _, files in self.content for f in files if f == file.name]


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '|-> ' + self.name


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(current_path, '../../06-advanced-python')
    contents_generator = os.walk(project_path)

    contents = []
    next(iter(contents_generator))
    for root, dirs, files in contents_generator:
        contents.append((root, dirs, files))

    folder1 = PrintableFolder(project_path, contents)
    print(folder1)
    file1 = PrintableFile('task1.py')
    print(file1 in folder1)
