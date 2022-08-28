from yandex_disk_work.yandex_disk import YandexDisk
from pathlib import Path

def add_new_file_in_disk(file_name_in_disk, file_path, token):
    ya = YandexDisk(token=token)
    return ya.upload_file_to_disk(file_name_in_disk, file_path)


if __name__ == '__main__':
    pass

