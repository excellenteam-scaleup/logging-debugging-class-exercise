# Use prints to find the bug

def generate_report(grades_dict):
    report = {}
    total_sum = 0
    total_count = 0

    for subjects, student in grades_dict.items():
        student_total = 0
        for grade, subject in subjects.items():
            student_total += grade
            total_sum += grade
            total_count += 1

        student_average = student_total / len(subjects) + 1  # suspicious
        report[student] = student_average

    class_average = total_sum / total_count
    report["class_average"] = class_average
    return report



grades = {
    "Alice": {"math": 90, "english": 85, "history": 78},
    "Bob": {"math": 75, "english": 80, "history": 72},
    "Charlie": {"math": 88, "english": 92, "history": 84}
}

print(generate_report(grades))
