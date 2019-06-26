import configparser
import json
import os
import re
import requests
from collections import Counter
from prettytable import PrettyTable
from tqdm import tqdm


def get_data_from_json_file(path, name):
    with open(os.path.join(path, f'./configs/{name}.json'), 'r') as file:
        return json.load(file)


def get_page_with_auth(url, headers):
    response = requests.get(url, headers=headers)
    page_data = response.text
    return page_data


def get_most_common_tags(pages_count, url, headers, params):
    tags = []
    for _ in tqdm(range(pages_count)):
        response = requests.get(url, headers=headers, params=params)
        page_data = response.json()['data']['stories']
        for post in page_data:
            post_tags = re.findall(r'data-tag="(.+?)"', post['html'])
            tags.extend(post_tags)
        params['page'] = str(int(params['page']) + 1)
    return tags


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(path, './configs/scraper.ini'))

    headers_pages = get_data_from_json_file(path, 'headers_pages')
    headers_auth = get_data_from_json_file(path, 'headers_auth')
    home = config['home']['url']
    params_pages = config['params_pages']
    pages_count = int(config['settings']['pages_count'])
    most_count = int(config['settings']['most_count'])

    tags = get_most_common_tags(pages_count, home, headers_pages, params_pages)
    table = PrettyTable(["Tag", "Count"])
    for tag_post in Counter(tags).most_common(most_count):
        table.add_row(tag_post)
    print(table)

    # print(len(re.findall(r'aleksejsamarin', get_page_with_auth(home, headers_auth))))
