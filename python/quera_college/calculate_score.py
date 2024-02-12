def calculate_final_grade(exam_score, homework_score, attendance_score):
    if 0 <= exam_score <= 100 and 0 <= homework_score <= 100 and 0 <= attendance_score <= 100:
        final_grade = 0.6 * exam_score + 0.3 * homework_score + 0.1 * attendance_score
        return round(final_grade, 2)
    else:
        return 'Invalid input'
