class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_w(self,lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def _medium_grade(self):
        result = sum(self.grades.values()) / len(*self.grades.values())
        return result


    def __lt__(self,other):
        if not isinstance(other,Student):
            print('Такой студент не найден!')
            return
        return self._medium_grade() < other._medium_grade()

    def __str__(self):
        info = (
            f'Имя = {self.name}\nФамилия = {self.surname}\nСредняя оценка  = {self._medium_grade}\n'
            f'Курсы в процессе = {"/".join(self.courses_in_progress)}\nЗавершенные курсы = {self.finished_courses}')
        return info


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def _medium_grade(self):
        result = sum(*self.grades.values()) / len(self.grades.values())
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такой лектор не найден!')
            return
        return self._medium_grade() < other._medium_grade()

    def __str__(self):
        info = (
            f'Имя = {self.name}\nФамилия = {self.surname}\nСредняя оценка  = {self._medium_grade}')
        return info

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = (
            f'Имя = {self.name}\nФамилия = {self.surname}')
        return info



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python','GIT']
best_student.finished_courses += ['GIT']


good_student = Student('Alex','Romanovich','man')
good_student.finished_courses += ['GIT' , 'Django']
good_student.courses_in_progress += ['Python']



cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']


not_good_lecturer = Lecturer('Anrey', 'Ivanov')
not_good_lecturer.courses_attached += ['Python']


cool_reviewer = Reviewer('Marina', 'Ivanova')
cool_reviewer.courses_attached += ['GIT']

good_reviewer = Reviewer('Vlad', 'Demelov')
good_reviewer.courses_attached += ['Python']


good_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(good_student, 'Python', 10)


good_student.rate_w(not_good_lecturer, 'Python', 5)
best_student.rate_w(cool_lecturer, 'Python', 10)

student_list = [best_student, good_student]
lecturer_list = [cool_lecturer, not_good_lecturer]

students_grades_list = []

def medium_student_grade(student_list, course):
    '''This function print medium grade of all students on course'''
    for student in student_list:
        for key, value in student.grades.items():
            if key is course:
                students_grades_list.extend(value)
    result = sum(students_grades_list) / len(students_grades_list)
    print(f'Средний бал по всем студентам  {course} курса: {result}')


lecturer_grades_list = []

def medium_lecturer_grade(lecturer_list, course):
    '''This function print medium grade of all lecturer on course'''
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key is course:
                lecturer_grades_list.extend(value)
    result = sum(lecturer_grades_list) / len(lecturer_grades_list)
    print(f'Средний бал по всем лекторам  {course} курса: {result}')


medium_student_grade(student_list, 'Python')
medium_lecturer_grade(lecturer_list, 'Python')


print(best_student)
print()
print(not_good_lecturer)
print(not_good_lecturer > cool_lecturer)
print(good_student.grades)
