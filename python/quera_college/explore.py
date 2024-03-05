import os


def explore(type, address):
    type = type.lower()
    result = {}
    for dirpath, dirnames, filenames in os.walk(address):
        for filename in filenames:
            if type == filename.rsplit('.')[-1]:
                result[dirpath] = result.get(dirpath, 0) + 1
    return result
