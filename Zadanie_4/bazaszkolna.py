import sys


def take_groups():
    init_groups = []
    while True:
        take_group = input()
        if not take_group:
            break
        else:
            init_groups.append(take_group)
    return init_groups


class Groups:
    def __init__(self):
        self.name = ''
        self.students = []
        self.teachers = []
        self.preceptor = ""

    def __str__(self):
        return self.name

    def write(self, name):
        self.name = name

    def write_student(self, person):
        self.students.append(person)

    def write_teacher(self, person):
        self.teachers.append(person)

    def write_preceptor(self, person):
        self.preceptor = person

    def read_students(self):
        for student in self.students:
            print(student)

    def read_preceptor(self):
        print(self.preceptor)

    def read_subject(self):
        for teacher in self.teachers:
            print("{}\n{}".format(teacher.subject, teacher))


class Student:
    def __init__(self):
        self.name = ''
        self.group = ''

    def __str__(self):
        return self.name

    def write(self):
        self.name = input()
        self.group = input()
        if self.group not in groups.keys():
            group_init = Groups()
            group_init.write(self.group)
            groups[self.group] = group_init
        groups[self.group].write_student(self)


class Teacher:
    def __init__(self):
        self.name = ""
        self.groups = []
        self.subject = ""

    def __str__(self):
        return self.name

    def write(self):
        self.name = input()
        self.subject = input()
        self.groups = take_groups()
        for group in self.groups:
            if group not in groups.keys():
                group_init = Groups()
                group_init.write(group)
                groups[group] = group_init
            groups[group].write_teacher(self)


class Preceptor:
    def __init__(self):
        self.name = ""
        self.groups = []
        self.show = True

    def __str__(self):
        if self.show:
            self.show = False
            return self.name
        else:
            return ""

    def write(self):
        self.name = str(input())
        self.groups = take_groups()
        for group in self.groups:
            if group not in groups.keys():
                group_init = Groups()
                group_init.write(group)
                groups[group] = group_init
            groups[group].write_preceptor(self)


students = []
teachers = []
preceptors = []
groups = {}

status = True

while status:
    take_data = str(input())
    if take_data == "wychowawca":
        preceptor = Preceptor()
        preceptor.write()
        preceptors.append(preceptor)
    elif take_data == "nauczyciel":
        teacher = Teacher()
        teacher.write()
        teachers.append(teacher)
    elif take_data == "uczen":
        student = Student()
        student.write()
        students.append(student)
    elif take_data == "koniec":
        status = False
    else:
        print("Przerwanie")
        break

else:
    pass
arg = sys.argv[1]
if len(arg) > 2:
    for person in preceptors:
        if arg == person.name:
            for group in person.groups:
                groups[group].read_students()

    for person in teachers:
        if arg == person.name:
            for group in person.groups:
                preceptor = str(groups[group].preceptor)
                if preceptor:
                    pass
                    print(preceptor)

    for person in students:
        if arg == person.name:
            groups[person.group].read_subject()

else:
    if arg in groups.keys():
        groups[arg].read_preceptor()
        groups[arg].read_students()
