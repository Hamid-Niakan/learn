import os
from shutil import copyfile


class FileManager:
    def find(self, name, address):
        file_paths = []
        for root, dirs, files in os.walk(address):
            for file in files:
                if file == name:
                    file_paths.append(os.path.join(root, file))
        return file_paths

    def create_file(self, name, address):
        if not os.path.exists(os.path.join(address, name)):
            os.makedirs(address, exist_ok=True)
            with open(os.path.join(address, name), 'w') as file:
                pass

    def create_dir(self, name, address):
        os.makedirs(os.path.join(address, name), exist_ok=True)

    def delete(self, name, address):
        if os.path.exists(os.path.join(address, name)):
            os.remove(os.path.join(address, name))

    def restore(self, name):
        pass

manager = FileManager()
manager.create_dir('test', './test/wow/')
manager.create_dir('test', './test/wow/')