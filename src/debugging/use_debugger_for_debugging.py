# Use pdb to do the following instructions -
# Setup - download pycharm
# 0. Add a breakpoint in the return line, inside the top_student function inside the Course class.
# 1. Continue to the next line using the button
# 2. Continue to the next line using the shortcut
# 3. Continue to the next occurrence of the breakpoint
# 4. Add a breakpoint at the beginning of the main function
# 5. Arrive inside the average property using keyboard shortcuts only
# 6. While debugging, create a variable called new_student and assign it a new Student called mark without grades (use evaluate expression)
# 7.while debugging, add the new student to the students attribute, inside the current course object.
# 8. Change marks name to rob
# 9. View all the breakpoints you have set up so far
# 10. Disable (don't delete) the first one you have created.
# 11. Run the program again and add course and student to the watch
# 12. Create a conditional breakpoint somewhere in the code that stops only when the student's name is "Dave"
# 13. Disable all your breakpoints,put your cursor on the last line of code and run you program to the cursor using
# a single command.


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    @property
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __repr__(self):
        return f"{self.name} (Avg: {self.average:.2f})"


class Course:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    @property
    def average(self):
        if not self.students:
            return 0
        return sum(student.average for student in self.students) / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average)

    def __repr__(self):
        return f"Course: {self.name}, Avg: {self.average:.2f}"


math_students = [
    Student("Alice", [90, 80, 85]),
    Student("Bob", [60, 70, 75]),
    Student("Carol", [95, 100, 90]),
]

cs_students = [
    Student("Dave", [88, 77, 85]),
    Student("Eve", [100, 90]),
    Student("Frank", [50, 60])
]

# Create courses
courses = [
    Course("Math 101", math_students),
    Course("CS 201", cs_students)
]

def main():
    for course in courses:
        print(course)
        for student in course.students:
            print("  -", student)
        print("  >> Top Student:", course.top_student())
        print()

    all_students = [student for course in courses for student in course.students]

    top_performers = [s.name for s in all_students if s.average > 90]

    print("🔥 Top Performers Across All Courses (avg > 90):")
    print(top_performers)


if __name__ == '__main__':
    main()