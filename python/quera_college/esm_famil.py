import csv

valid_names = None
participants = {}


def ready_up():
    global valid_names
    columns = [[] for _ in range(6)]

    with open('esm_famil_data.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            for i, column in enumerate(columns):
                if line[i]:
                    column.append(line[i].replace(' ', ''))
    valid_names = {
        'esm': columns[0],
        'famil': columns[1],
        'keshvar': columns[2],
        'rang': columns[3],
        'ashia': columns[4],
        'ghaza': columns[5]
    }


def add_participant(participant, answers):
    global participants
    for key, value in answers.items():
        answers[key] = value.strip().replace(' ', '')
    participants[participant] = answers


def calculate_all():
    result = {participant: 0 for participant in participants}
    unique_point = None
    not_unique_point = None

    def has_everyone_answered(category):
        for answer in participants.values():
            if len(answer[category]) == 0:
                return False
        return True

    def is_duplicate_answer(current_participant, category, word):
        for participant, answer in participants.items():
            if current_participant != participant and answer[category] == word:
                return True
        return False

    for category, category_value in valid_names.items():
        for participant, answer in participants.items():
            if answer[category] in category_value:
                if has_everyone_answered(category):
                    unique_point = 10
                    not_unique_point = 5
                else:
                    unique_point = 15
                    not_unique_point = 10
                if is_duplicate_answer(participant, category, answer[category]):
                    result[participant] += not_unique_point
                else:
                    result[participant] += unique_point
    return result


ready_up()
add_participant(participant='salib', answers={
                'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant='kianoush', answers={
                'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant='sajjad', answers={
                'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant='farhad', answers={
                'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
calculate_all()
