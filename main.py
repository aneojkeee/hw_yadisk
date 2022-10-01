import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        file_path = os.path.normpath(file_path)
        HEADERS = {"Authorization": f'OAuth {self.token}'}
        data = {"file": open(file_path, 'rb')}

        response_url = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": file_path},
            headers=HEADERS)
        url = response_url.json().get('href')
        response_upload = requests.put(url=url, files=data, headers={})
        return print(response_upload.status_code)

if __name__ == '__main__':
    path_to_file = ('my_text.txt')
    token = ''
    uploader = YaUploader(token)
