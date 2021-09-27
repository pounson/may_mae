class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rating(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_grade(self):
        rank = round(sum(self.grades.values()) / len(self.grades.values()))
        return rank

    def __str__(self):
        student_info = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за домашние задания: {self.get_grade()}\n' \
                       f'Курсе в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return student_info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.get_grade < other.get_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_grade(self):
        gradeses = round(sum(self.grades.values()) / len(self.grades.values()), 2)
        return gradeses

    def __str__(self):
        lecturer_info = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}\n' \
                        f'Средняя оценка за лекции: {self.get_grad()}'
        return lecturer_info



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_info = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}'
        return reviewer_info


student_1 = Student("Tom", 'Hill', 'male')
student_1.courses_in_progress = ['Python', 'Git']
student_1.finished_courses = ['Java', 'JavaScript']

student_2 = Student('Franklin', 'Clinton', 'male')
student_2.courses_in_progress = ['Python']
student_2.finished_courses = ['JavaScript']

lecturer_1 = Lecturer('Mia', 'Sing')
lecturer_1.courses_attached = ['Python', 'Git']

lecturer_2 = Lecturer('Lily', 'Dalas')
lecturer_2.courses_attached = ['Python', 'JavaScript']

reviewer_1 = Reviewer('Korben', 'Dalas')
reviewer_1.courses_attached = ['Python']

reviewer_2 = Reviewer('Trevor', 'Desanta')
reviewer_2.courses_attached = ['Git', 'JavaScript']

student_1.rating(lecturer_1, 'Python', 7)
student_1.rating(lecturer_1, 'Git', 6)

student_2.rating(lecturer_2, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Git', 7)


def student_avge_grade(student_list, course_name):
  for student in student_list:
    if course_name in student.courses_in_progress:
      if course_name in student.grades:
        all_grade = []
        avg = sum(student.grades.get(course_name)) / len(student.grades.get(course_name))
        all_grade.append(avg)
  all_avg = sum(all_grade) / len(all_grade)
  res = print(f'Средний балл за ДЗ по курсу {course_name} = {round(all_avg, 2)}')
  return res
  student_avge_grade(student_list , course_name)

def lecturer_avg_grade(lecturer_list, course_name):
  for lecturer in lecturer_list:
    if course_name in lecturer.courses_attached:
      if course_name in lecturer.grades:
        all_grade = []
        avg = sum(lecturer.grades.get(course_name)) / len(lecturer.grades.get(course_name))
        all_grade.append(avg)
  all_avg = sum(all_grade) / len(all_grade)
  res = print(f'Средний балл за лекции по курсу {course_name} = {round(all_avg, 2)}')
  return res
  lecturer_avg_grade(lecturer_list, course_name)