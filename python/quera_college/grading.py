class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    def __init__(self):
        self.file_data = []
        self.file_path = ''

    def set_file(self, address):
        self.file_path = address
        with open(address) as file:
            self.file_data = file.readlines()

    def load(self, line_number):
        if line_number - 1 < len(self.file_data):
            values = self.file_data[line_number - 1].split()
            return Grade(int(values[0]), int(values[1]), float(values[2]))
        return None

    def calc_student_average(self, student_id):
        scores = []
        for _ in self.file_data:
            values = _.split()
            if int(values[0]) == student_id:
                scores.append(float(values[2]))
        scores_sum = 0
        for score in scores:
            scores_sum += score
        return float(scores_sum / len(scores))

    def calc_course_average(self, course_code):
        scores = []
        for _ in self.file_data:
            values = _.split()
            if int(values[1]) == course_code:
                scores.append(float(values[2]))
        scores_sum = 0
        for score in scores:
            scores_sum += score
        return float(scores_sum / len(scores))

    def count(self):
        return len(self.file_data)

    def save(self, grade):
        for _ in self.file_data:
            if f'{grade.student_id} {grade.course_code}' in _:
                break
        else:
            student_score = f'\n{grade.student_id} {grade.course_code} {grade.score}'
            self.file_data.append(student_score)
            with open(self.file_path, 'a') as file:
                file.write(student_score)


util = CourseUtil()
util.set_file('sample_scores.txt')
score = Grade(123123123, 312, 19)
util.save(score)
print(util.load(5).score)
# util.save(grade)
# print(util.file_data)
