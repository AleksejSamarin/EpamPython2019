from random import randint
from threading import Timer

cache_storage = []


def make_cache(seconds):
    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            cache_storage.append(result)
            Timer(seconds, delete_first).start()
            return result

        def delete_first():
            cache_storage.pop(0)

        return wrapper
    return decorator


@make_cache(10)
def get_new_online_user_id():  # helpful usecase
    new_user_id = randint(0, 1000)
    print(f'New online user, id: {new_user_id}')
    return new_user_id


def print_cache_storage():
    print(cache_storage)


if __name__ == '__main__':
    get_new_online_user_id()
    Timer(9, print_cache_storage).start()  # [id]
    Timer(11, print_cache_storage).start()  # []
