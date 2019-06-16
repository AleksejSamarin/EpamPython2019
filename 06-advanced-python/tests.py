"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""

import os
import pytest
from task1.task1 import PrintableFile, PrintableFolder
from task2.task2 import Graph
from task3.task3 import CeasarSipher


@pytest.fixture
def data_task1():
    current_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(current_path, '../02-Functions')
    contents_generator = os.walk(project_path)
    contents = []
    next(iter(contents_generator))
    for root, dirs, files in contents_generator:
        contents.append((root, dirs, files))
    return project_path, contents


@pytest.fixture
def data_task3():
    obj = CeasarSipher()
    obj.message = 'abc'
    obj.another_message = 'hellox'
    return obj


def test_task1(data_task1):
    path, contents = data_task1
    folder1 = PrintableFolder(path, contents)
    file1 = PrintableFile('hw1.py')
    file2 = PrintableFile('hw11.py')
    result = 'V 02-Functions\n' \
             '|-> V hw1\n|\t|-> hw1.py\n|\t|-> hw1.txt\n' \
             '|-> V hw2\n|\t|-> hw2.py\n|\t|-> hw2.txt\n' \
             '|-> V hw3\n|\t|-> hw3.py\n|\t|-> hw3.txt\n' \
             '|-> V hw4\n|\t|-> hw4.py\n|\t|-> hw4.txt\n' \
             '|-> V slides\n|\t|-> functions slides.pdf\n'
    assert str(folder1) == result
    assert file1 in folder1
    assert file2 not in folder1


@pytest.mark.parametrize('structure, expected', [
    ({'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']},
     ['A', 'B', 'C', 'D']),
    ({'A': ['B', 'D', 'C'], 'X': ['G'], 'B': ['X', 'C'], 'C': ['A'], 'D': ['B'], 'G': ['A', 'B']},
     ['A', 'B', 'D', 'C', 'X', 'G'])
])
def test_task2(structure, expected):
    assert [vertice for vertice in Graph(structure)] == expected


def test_task3(data_task3):
    obj = data_task3
    assert obj.message == 'efg'
    assert obj.another_message == 'olssve'
