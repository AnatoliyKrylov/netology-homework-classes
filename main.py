class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades(self, sum_grades=0.0, count_grades=0):
        for grades in self.grades.values():
            for grade in grades:
                sum_grades += grade
                count_grades += 1
        return round(sum_grades / count_grades, 1)

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за'
               f' домашние задания: {self.avg_grades()}\nКурсы в процессе '
               f'завершения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Кто-то не студент')
            return
        else:
            return self.avg_grades() < other.avg_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lecturers =[]

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.all_lecturers.append(self)

    def avg_grades(self, sum_grades=0.0, count_grades=0):
        for grades in self.grades.values():
            for grade in grades:
                sum_grades += grade
                count_grades += 1
        return round(sum_grades / count_grades, 1)

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.avg_grades()}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Кто-то не лектор')
            return
        else:
            return self.avg_grades() < other.avg_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def avg_hw(students, course, sum_grades=0.0, count_grades=0):
    for student in students:
        if student.grades.get(course) is not None:
            for grade in student.grades.get(course):
                sum_grades += grade
                count_grades += 1
    return round(sum_grades / count_grades, 1)


def avg_lecture(lecturers, course, sum_grades=0.0, count_grades=0):
    for lecturer in lecturers:
        if lecturer.grades.get(course) is not None:
            for grade in lecturer.grades.get(course):
                sum_grades += grade
                count_grades += 1
    return round(sum_grades / count_grades, 1)


first_student = Student('Peter', 'Parker', 'Male')
first_student.grades = {'Python': [10, 10, 10], 'Git': [10, 9]}
first_student.courses_in_progress = ['Python', 'Git']
first_student.finished_courses = ['Введение в программирование']
second_student = Student('Natasha', 'Romanoff', 'Female')
second_student.grades = {'Python': [10, 8, 10], 'Java': [10, 6]}
second_student.courses_in_progress = ['Python', 'Java']
second_student.finished_courses = ['Введение в программирование']
first_lecturer = Lecturer('Tony', 'Stark')
first_lecturer.courses_attached = ['Python', 'Java', 'Git']
first_lecturer.grades = ({'Python': [10, 10, 10], 'Java': [10, 8, 7],
                          'Git': [7, 9]})
second_lecturer = Lecturer('Bruce', 'Banner')
second_lecturer.courses_attached = ['Python', 'Git']
second_lecturer.grades = {'Python': [10, 9, 9], 'Git': [6, 8]}
first_reviewer = Reviewer('Nick', 'Fury')
first_reviewer.courses_attached = ['Python', 'Java', 'Git']
second_reviewer = Lecturer('Margaret', 'Carter')
second_reviewer.courses_attached = ['Python', 'Java']
first_student.rate_lecture(first_lecturer, 'Python', 10)
print(first_student)
print(first_student > second_student)
print(second_lecturer)
print(first_lecturer < second_lecturer)
first_reviewer.rate_hw(first_student, 'Git', 9)
print(first_lecturer)
print(avg_hw(Student.all_students, 'Python'))
print(avg_lecture(Lecturer.all_lecturers, 'Java'))
