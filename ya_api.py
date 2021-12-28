import requests

TOKEN_YADISK = ''
mkdir_url = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.put(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.delete(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


if __name__ == '__main__':
    print(create_folder('test_folder'))
    print(delete_folder('test_folder'))




