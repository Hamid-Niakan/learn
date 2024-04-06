import os


def combet(type1, type2, path):
    type1_count = 0
    type2_count = 0
    file_names_count = {}
    type1_chosen_names = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_names_count[file.split('.')[0]] = file_names_count.get(
                file.split('.')[0], 0) + 1
            if file.endswith(type1):
                type1_count += 1
                type1_chosen_names[file.split('.')[0]] = type1_chosen_names.get(
                    file.split('.')[0], 0) + 1
            elif file.endswith(type2):
                type2_count += 1
    max_key = max(file_names_count, key=file_names_count.get)
    if type2_count > type1_count:
        return 'Win! Normally!'
    else:
        max_key_count = file_names_count[max_key]
        if max_key in type1_chosen_names:
            type1_count -= max_key_count
        type2_count += max_key_count
        if type2_count > type1_count:
            return f"Win! you can win if you cheat on '{max_key}'!"
        else:
            return "Lose! you can't win this game!"


print(combet('py', 'png', './'))
