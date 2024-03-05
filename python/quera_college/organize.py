import os
import sys
import time


def get_file_format(filename):
    if '.' not in filename:
        return 'NotFile'
    return filename.lower().rsplit('.')[-1]


def get_file_year(file_address):
    return time.ctime(os.path.getmtime(file_address)).split()[-1]


def check_file_format(file_format):
    photos = ['jpg', 'jpeg', 'png']
    videos = ['mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov']
    if file_format in photos:
        return 'photos'
    if file_format in videos:
        return 'videos'
    return None


def copy_files(src, dest):
    for item in os.listdir(src):
        src_item_path = os.path.join(src, item)

        if os.path.isfile(src_item_path):
            file_format = check_file_format(get_file_format(item))

            if file_format is not None:
                year = get_file_year(src_item_path)
                dest_item_path = os.path.join(dest, year, file_format)

                with open(src_item_path, 'rb') as src_file:
                    file_data = src_file.read()

                if not os.path.exists(dest_item_path):
                    os.makedirs(dest_item_path)

                with open(os.path.join(dest_item_path, item), 'wb') as dest_file:
                    dest_file.write(file_data)
        else:
            copy_files(src_item_path, dest)


copy_files(sys.argv[1], sys.argv[2])
