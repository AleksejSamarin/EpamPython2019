import os


def get_data_from_file(name: str) -> str:
    with open(os.path.join(path, f"./files/{name}"), 'r') as file:
        return file.read()


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    files = ('winedata_1.json', 'winedata_2.json')
    raw_data_files, json_data_files = [], []
    for file_name in files:
        raw_data_files.append(get_data_from_file(file_name)[3:-3].split('}, {"'))
    for file_data in raw_data_files:
        for item in file_data:
            json_data_files.append(dict(i.split('": ') for i in item.split(', "')))
