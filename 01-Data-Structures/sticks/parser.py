import os


def list_of_dicts_to_json(dictionary: list) -> str:
    string_json = str(dictionary)
    replaces = (("[{'", '[{"', 1), ("'}]", '"}]', 1), ("': '", '": "'), ("', '", '", "'),
                ("'}, {'", '"}, {"'), ("': {'", '": {"'), ("}, '", '}, "'), ("'}", '"}'), ("\\'", "'"),
                ("': ", '": '), (", '", ', "'), ("'\"", '"'), ("\"'", "\""), ('""', '"'), ("\\\\", "\\"))
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


def count_most(filtered_list: list, attr: str, sum_attr: str = None) -> tuple:
    sum_map, count_map = {}, {}
    if not sum_attr:
        for entry in filtered_list:
            try:
                if entry[attr] != 'null':
                    sum_map[entry[attr]] += 1
            except KeyError:
                sum_map[entry[attr]] = 1
    else:
        for entry in filtered_list:
            try:
                if entry[attr] != 'null' and entry[sum_attr] != 'null':
                    sum_map[entry[attr]] += int(entry[sum_attr].replace('"', ''))
                    count_map[entry[attr]] += 1
            except KeyError:
                count_map[entry[attr]], sum_map[entry[attr]] = 1, 1
        for key in count_map.keys():
            sum_map[key] = sum_map[key] / count_map[key]
    return max(sum_map, key=lambda k: sum_map[k]), min(sum_map, key=lambda k: sum_map[k])


def json_to_markdown(json: str, title: str, cuts: tuple) -> str:
    markdown = title + json[cuts[0]:cuts[1]]
    replaces = (('[', '\n'), ('{', '\n'), ('"', '\t'), (':', '->'),
                ('}', '\n'), (']', '\n'), (',', '\n'))
    for replace in replaces:
        markdown = markdown.replace(*replace)
    return markdown


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

    wines = ('Gew\\u00fcrztraminer', 'Riesling', 'Merlot', 'Madera', 'Tempranillo', 'Red Blend')
    needs = ('average_price', 'min_price', 'max_price',
             'most_common_region', 'most_common_country', 'average_score')
    needs_all = ('most_expensive_wine', 'cheapest_wine', 'highest_score',
                 'lowest_score', 'most_expensive_country', 'cheapest_country',
                 'most_rated_country', 'underrated_country', 'most_active_commentator')

    dict_wines, dict_all = {}, {}
    for wine_variety in wines:
        filtered_wine_list = list(filter(lambda wine: wine_variety in wine['variety'], sorted_json_data))
        digit_prices_count = sum(wine['price'].isdigit() for wine in filtered_wine_list)
        digit_prices_sum = sum(int(wine['price']) for wine in filtered_wine_list if wine['price'].isdigit())
        average_price = digit_prices_sum / digit_prices_count if digit_prices_count else 0
        if average_price:
            min_price = min(int(wine['price']) for wine in filtered_wine_list if wine['price'].isdigit())
            max_price = max(int(wine['price']) for wine in filtered_wine_list if wine['price'].isdigit())
            most_common_region, _ = count_most(filtered_wine_list, 'region_1')
            most_common_country, _ = count_most(filtered_wine_list, 'country')
        else:
            min_price, max_price, most_common_region, most_common_country = (0, 0, "-", "-")
        digit_score_count = sum(wine['points'].replace('"', '').isdigit() for wine in filtered_wine_list)
        digit_score_sum = sum(int(wine['points'].replace('"', '')) for wine in filtered_wine_list
                              if wine['points'].replace('"', '').isdigit())
        average_score = digit_score_sum / digit_score_count if digit_score_count else 0
        dict_wines.update({wine_variety: dict(((k, globals()[k]) for k in needs))})

    biggest_price = max(int(wine['price']) for wine in sorted_json_data if wine['price'].isdigit())
    most_expensive_wine_list = list(filter(lambda wine: wine['price'] == str(biggest_price), sorted_json_data))
    most_expensive_wine = [wine['title'] for wine in most_expensive_wine_list if 'title' in wine]
    smallest_price = min(int(wine['price']) for wine in sorted_json_data if wine['price'].isdigit())
    cheapest_wine_list = list(filter(lambda wine: wine['price'] == str(smallest_price), sorted_json_data))
    cheapest_wine = [wine['title'] for wine in cheapest_wine_list if 'title' in wine]
    highest_score = max(int(wine['points'].replace('"', ''))
                        for wine in sorted_json_data if wine['points'].replace('"', '').isdigit())
    lowest_score = min(int(wine['points'].replace('"', ''))
                       for wine in sorted_json_data if wine['points'].replace('"', '').isdigit())
    most_expensive_country, cheapest_country = count_most(sorted_json_data, 'country', 'price')
    most_rated_country, underrated_country = count_most(sorted_json_data, 'country', 'points')
    most_active_commentator, _ = count_most(sorted_json_data, 'taster_name')
    dict_all.update(dict(((k, globals()[k]) for k in needs_all)))

    stats = {'statistics': {'wine': {}}}
    stats['statistics']['wine'].update(dict_wines)
    stats['statistics'].update(dict_all)
    json_stats = list_of_dicts_to_json([stats])
    write_to_file('stats.json', json_stats)
    write_to_file('stats.md', json_to_markdown(json_stats, '# Statistics for winedata_full.json\n', (25, -3)))
