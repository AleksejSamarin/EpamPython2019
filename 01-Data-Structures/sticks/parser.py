import os


def list_of_dicts_to_json(dictionary: list) -> str:
    string_json = str(dictionary)
    replaces = (("[{'", '[{"', 1), ("'}]", '"}]', 1), ("': '", '": "'),
                ("', '", '", "'), ("'}, {'", '"}, {"'), ('""', '"'))
    for replace in replaces:
        string_json = string_json.replace(*replace)
    return string_json


def unique_dicts(list_of_dicts: list) -> list:
    return [dict(s) for s in set(tuple(d.items()) for d in list_of_dicts)]


def get_data_from_file(name: str) -> str:
    with open(os.path.join(path, f"./files/{name}"), 'r') as file_r:
        return file_r.read()


def write_to_file(name: str, string: str):
    with open(os.path.join(path, f"./files/{name}"), 'w') as file_w:
        file_w.write(string)


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    files = ('winedata_1.json', 'winedata_2.json')
    raw_data_files, json_data_files = [], []
    for file_name in files:
        raw_data_files.append(get_data_from_file(file_name)[3:-3].split('}, {"'))
    for file_data in raw_data_files:
        for item in file_data:
            json_data_files.append(dict(i.split('": ') for i in item.split(', "')))

    unique_json_data = unique_dicts(json_data_files)
    sorted_json_data = sorted(unique_json_data, key=lambda i: (i['price'], i['title']), reverse=True)
    write_to_file('winedata_full.json', list_of_dicts_to_json(sorted_json_data))

    wines = ('Gewürztraminer', 'Riesling', 'Merlot', 'Madera', 'Tempranillo', 'Red Blend')
    needs = ('average_price', 'min_price', 'max_price',
             'most_common_region', 'most_common_country', 'average_score')
    needs_all = ('most_expensive_wine', 'cheapest_wine', 'highest_score',
                 'lowest_score', 'most_expensive_country', 'cheapest_country',
                 'most_rated_country', 'underrated_country', 'most_active_commentator')
