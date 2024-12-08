class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        return (f'Имя {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {sum(sum(v) for v in self.grades.values()) / len(self.grades)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')
      
    def __cmp__(self, student):
        average_rating_self = sum(sum(v) for v in self.grades.values() ) / len(self.grades)
        average_rating_student = sum(sum(v) for v in student.grades.values() ) / len(student.grades)
        if average_rating_self < average_rating_student:
            return -1
        if average_rating_self == average_rating_student:
            return 0
        if average_rating_self > average_rating_student: 
            return 1
            
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'    
         
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
       
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def __str__(self):
        return (f'Имя {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {sum(sum(v) for v in self.grades.values()) / len(self.grades)}')
        
    def average_rating_lecturer(grades):
        return 5    
        
    def __cmp__(self, lecturer):
        average_self = sum( v for v in self.grades.values() ) / len(self.grades)
        average_lecturer = sum( v for v in lecturer.grades.values() ) / len(lecturer.grades)        
        if average_self < average_lecturer:
            return -1
        if average_self == average_lecturer:
            return 0
        if average_self > average_lecturer: 
            return 1
                     
        
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
        return(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}') 
        
 
def average_student(list_student, courses):
    sum_student = 0
    for student in list_student:
        for cours, grade in student.grades.items():
            sum_cour = 0
            if cours == courses:
                sum_cour = sum(grade)
                break 
        sum_student += sum_cour         
    return sum_student/len(list_student)


def average_lecturer(list_lecturer, courses):
    sum_lecturer = 0
    for lecturer in list_lecturer:
        for cours, grade in lecturer.grades.items():
            sum_cour = 0
            if cours == courses:
                sum_cour = sum(grade)
                break 
        sum_lecturer += sum_cour         
    return sum_lecturer/len(list_lecturer)  
      
 
student1 = Student('Степанов', 'Петр', 'Мужчина')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Сидорова', 'Оля', 'Женщина')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

mentor1 = Reviewer('Мозгов', 'Иван')
mentor1.courses_attached += ['Python']
mentor1.courses_attached += ['Git']

mentor2 = Reviewer('Петров', 'Алексей')
mentor2.courses_attached += ['Python']
mentor2.courses_attached += ['Введение в программирование']
 
mentor1.rate_hw(student1, 'Python', 7)
mentor1.rate_hw(student1, 'Git', 5)
mentor1.rate_hw(student2, 'Git', 10)

mentor2.rate_hw(student2, 'Python', 10)
mentor2.rate_hw(student2, 'Введение в программирование', 10)
mentor2.rate_hw(student1, 'Введение в программирование', 9)

lecturer1 = Lecturer('Иванов', 'Федр')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Введение в программирование']

lecturer2 = Lecturer('Федоров', 'Василий')
lecturer2.courses_attached += ['Git']


student1.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Введение в программирование', 6)
student1.rate_hw(lecturer2, 'Git', 7)

student2.rate_hw(lecturer1, 'Python', 6)
student2.rate_hw(lecturer1, 'Введение в программирование', 7)
student2.rate_hw(lecturer2, 'Git', 9)


print(student1)
print(student2)


print(lecturer1)
print(lecturer2)


print(mentor1)
print(mentor2)



list_student = []
list_student.append(student1)
list_student.append(student2)
courses = "Python" 
print(f'Cредняя оценка за домашние задания по всем студентам в рамках курса: "{courses}": {average_student(list_student, courses)}')

list_lecturer = []
list_lecturer.append(lecturer1)
list_lecturer.append(lecturer2)
courses = "Git" 
print(f'Cредняя оценка за лекции всех лекторов в рамках курса: "{courses}": {average_lecturer(list_lecturer, courses)}')

eq = student1 == student2
if eq == 0:
    print(f'У Студента {student1.name} средняя оценка за домашние задания такая же, как и у {student2.name}')
if eq == -1:     
    print(f'У Студента {student1.name} средняя оценка за домашние задания хуже, чем у {student2.name}')
if eq == 1:     
    print(f'У Студента {student1.name} средняя оценка за домашние задания лучше, чем у {student2.name}')
    
eq = student2 == student1
if eq == 0:
    print(f'У студента {student2.name} средняя оценка за домашние задания такая же, как и у {student1.name}')
if eq == -1:     
    print(f'У студента {student2.name} средняя оценка за домашние задания хуже, чем у {student1.name}')
if eq == 1:     
    print(f'У студента {student2.name} средняя оценка за домашние задания лучше, чем у {student1.name}') 
    
eq = lecturer1 == lecturer2
if eq == 0:
    print(f'У лектора {lecturer1.name} средняя оценка за лекции такая же, как и у {lecturer2.name}')
if eq == -1:     
    print(f'У лектора {lecturer1.name} средняя оценка за лекции хуже, чем у {lecturer2.name}')
if eq == 1:     
    print(f'У лектора {lecturer1.name} средняя оценка за лекции лучше, чем у {lecturer2.name}')        