"""
С помощью паттерна "Наблюдатель" реализуйте простую систему подписок и уведомлений видеохостинга MyTube.

Для реализации можно использовать следующие определения классов:

MyTubeChannel - канал, у которого есть владелец.
    Параметры:
        name: str - Название канала
        owner: MyTubeUser - Владелец канала
        playlists: Dict[str, List[str]] - Плейлисты на канале ({'Название плейлиста': ['видео 1', 'видео 2', 'видео 3']})

    Методы:
        __init__(channel_name: str, chanel_owner: MyTubeUser) - При создании канала указывается название канала и его владелец
        subscribe(user: MyTubeUser) - Подписка пользователя user на канал
        publish_video(video: str) - Публикация нового видео и рассылка новости о публикации всем подписчика
        publish_playlist(name: str, playlist: List[str]) - Публикация нового плейлиста и рассылка новости о публикации всем подписчикам

MyTubeUser - Пользователь видеохостинга MyTube
    Параметры:
        _name: str - Имя пользователя MyTube
    Методы:
        __init__(user_name: str) - У нового пользователя есть имя
        update(message: str): - Метод для приёма уведомлений о публикации

Примерн кода, который должен работать:

matt = MyTubeUser('Matt')
john = MyTubeUser('John')
erica = MyTubeUser('Erica')

dogs_life = MyTubeChannel('All about dogs', matt)
dogs_life.subscribe(john)
dogs_life.subscribe(erica)

dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}

for video in dogs_nutrition_videos:
    dogs_life.publish_video(video)

dogs_life.publish_playlist(dogs_nutrition_playlist)

Output:
Dear John, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear Erica, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear John, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear Erica, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear John, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'
Dear Erica, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'

"""

from abc import ABC, abstractmethod
from typing import Dict, List


class User(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class MyTubeUser(User):
    def __init__(self, user_name: str):
        self._name = user_name

    def update(self, message: str):
        print(f'Dear {self._name}, {message}')


class MyTubeChannel:
    def __init__(self, channel_name: str, chanel_owner: MyTubeUser):
        self.name = channel_name
        self.owner = chanel_owner
        self.playlists = []
        self.subscribers = []

    def subscribe(self, user: MyTubeUser):
        self.subscribers.append(user)

    def unsubscribe(self, user: MyTubeUser):
        self.subscribers.remove(user)

    def notify_subscribers(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)

    def publish_video(self, video: str):
        message = f"there is new video on '{self.name}' channel: '{video}'"
        self.notify_subscribers(message)

    def publish_playlist(self, playlist: Dict[str, List[str]]):
        message = f"there is new playlist on '{self.name}' channel: '{list(playlist.keys())[0]}'"
        self.notify_subscribers(message)


if __name__ == '__main__':
    matt = MyTubeUser('Matt')
    john = MyTubeUser('John')
    erica = MyTubeUser('Erica')

    dogs_life = MyTubeChannel('All about dogs', matt)
    dogs_life.subscribe(john)
    dogs_life.subscribe(erica)

    dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
    dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}

    for video in dogs_nutrition_videos:
        dogs_life.publish_video(video)

    dogs_life.publish_playlist(dogs_nutrition_playlist)
