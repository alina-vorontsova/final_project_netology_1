import requests
import os
from pprint import pprint

with open('config.txt') as config_file: # в файле построчно записаны токены для вк и я.диска
    vk_token = config_file.readline().strip()
    ya_token = config_file.readline().strip()

def get_id():
    '''Получение id пользователя, чьи фотографии надо скопировать на я.диск'''
    user_id = input('Введите id пользователя: ')
    return user_id

class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        '''Получение параметров авторизации для запроса'''
        self.token = vk_token
        # self.id = get_id()
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_photos_vk(self):
        '''Получение всех фотографий (в данном случае аватарок, смотря что в 'album_id') пользователя'''
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': user_id, 'album_id': 'profile', 'rev': 0, 'extended': 1, 'photo_sizes': 1}
        response = requests.get(url, params={**self.params, **params}).json()
        res = response['response']['items']
        return res

def get_photos_from_vk():
    '''Получение фотографий в максимальном размере'''
    all_photos = vk.get_photos_vk()
    url_dict = {}
    for photo in all_photos:
        max_size = 0
        file_sizes = photo['sizes']
        for size in file_sizes:
            file_size = size['height'] * size['width']
            if max_size < file_size:
                max_size = file_size
                url_to_biggest_photo = size['url']
                likes = photo['likes']['count']
        url_dict[url_to_biggest_photo] = likes
        #url_list.append(url_to_biggest_photo)
    return url_dict


access_token_vk = vk_token
user_id = get_id()
vk = VK(access_token_vk, user_id)
pprint(vk.get_photos_vk())
#print(get_photos_from_vk())