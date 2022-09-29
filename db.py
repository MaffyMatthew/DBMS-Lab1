import os
import random


def createDB(name, students, variants):
    filename = f"C://Users/matve/PycharmProjects/DataBase/{name}"
    if os.path.exists(filename):
        print('БД с таким именем уже существует')
        return -1, -1, -1
    else:
        os.mkdir(filename)
        os.chdir(filename)
        os.mkdir(f"C://Users/matve/PycharmProjects/DataBase/{name}/backup")
        print(f"БД '{name}' была успешно создана\n")

        if not os.path.exists(f"C://Users/matve/PycharmProjects/DataBase/{name}/studentsID.txt"):
            students = createStudentsTable(students)

        if not os.path.exists(f"C://Users/matve/PycharmProjects/DataBase/{name}/variantsID.txt"):
            variants = createVariantsTable(variants)

        IDs = createIDTable()
        return students, variants, IDs


def openDB(name):
    filename = f"C://Users/matve/PycharmProjects/DataBase/{name}"
    if os.path.exists(filename):
        os.chdir(filename)
        print(f"База данных '{name}' открыта\n")
        return getStudentsVariantsIDs()
    else:
        print('БД с таким именем не существует(')
        return -1, -1, -1


def createStudentsTable(students):
    file = open("studentsID.txt", 'w', encoding="UTF8")

    for i in range(len(students)):
        file.write(f"{i + 1} {students[i]}\n")

    students = dict(zip(map(str, list(range(1, len(students) + 1))), students))
    print("studentsID были успешно созданы")

    file.close()
    printTable(students)
    return students


def createVariantsTable(variants):
    file = open("variantsID.txt", "w", encoding="UTF8")

    for i in range(len(variants)):
        file.write(f"{i + 1} {variants[i]}\n")

    variants = dict(zip(map(str, list(range(1, len(variants) + 1))), variants))
    print("variantsID были успешно созданы")

    file.close()
    printTable(variants)
    return variants


def createIDTable():
    students = open("studentsID.txt", encoding="UTF8")
    variants = open("variantsID.txt", encoding="UTF8")
    var = list(variants.readlines())
    ID_table = open("IDTable.txt", 'w', encoding="UTF8")
    IDs = {}

    for i in list(students.readlines()):
        id = int(i.split()[0])
        var_id = random.randint(1, len(var))
        print(f'{id} {var_id}', file=ID_table)
        IDs[str(id)] = str(var_id)

    students.close()
    variants.close()
    ID_table.close()

    return IDs


def addStudent(student, students, variants, IDs):
    if student in students.values():
        print('Студент с таким именем уже существует!')
    else:
        students[str(max(list(map(int, list(students.keys())))) + 1)] = student
        IDs[str(max(list(map(int, list(students.keys())))))] = random.choice(list(variants.keys()))


def addVariant(variant, variants):
    if variant in variants.values():
        print('Вариант с таким названием уже существует!')
    else:
        variants[str(max(list(map(int, list(variants.keys())))) + 1)] = variant


def remakeIDs(students, variants):
    IDs = {}
    for i in students.keys():
        IDs[i] = random.choice(list(variants.keys()))
    return IDs


def deleteStudent(id, students, IDs):
    del students[id]
    del IDs[id]


def deleteVariant(id, variants, students):
    del variants[id]
    return variants, remakeIDs(students, variants)


def editStudent(id, students):
    if id in students.keys():
        print(f'Студент с id{id} - {students[id]}')
        student = input('Введите новые данные: ')

        if student in students.values():
            print('Студент с таким именем уже существует!')
        else:
            students[id] = student
    else:
        print('Студента с таким ID не существует')


def editVariant(id, variants):
    if id in variants.keys():
        print(f'Вариант с id{id} - {variants[id]}')
        variant = input('Введите новые данные: ')

        if variant in variants.values():
            print('Вариант с таким названием уже существует!')
        else:
            variants[id] = variant
    else:
        print('Варианта с таким ID не существует')


def giveVariant(IDs):
    id = input('Введите ID студента: ')
    id_var = input('Введите ID варианта: ')
    IDs[id] = id_var


def printTable(table):
    for i in table.keys():
        print(f'{i:4} {table[i]}')
    print()


def printStudentVarTable(students, variants, IDs):
    for studentID in IDs.keys():
        print(f'{studentID:4} {students[studentID]:35} {variants[IDs[studentID]]}')
    print()


def printInfo(students, variants, IDs):
    id = input('Введите ID студента: ')
    print(f'{id:4} {students[id]:30} {variants[IDs[id]]}')


def getStudentsVariantsIDs():
    students = open(f"studentsID.txt", encoding="UTF8")
    variants = open(f"variantsID.txt", encoding="UTF8")
    IDs = open(f"IDTable.txt", encoding="UTF8")
    std = list(map(lambda x: x.rstrip().partition(' '), list(students.readlines())))
    var = list(map(lambda x: x.rstrip().partition(' '), list(variants.readlines())))
    id = list(map(lambda x: x.rstrip().partition(' '), list(IDs.readlines())))
    students.close()
    variants.close()
    IDs.close()

    students, variants, IDs = {}, {}, {}
    for i in std:
        students[i[0]] = i[2]
    for i in var:
        variants[i[0]] = i[2]
    for i in id:
        IDs[i[0]] = i[2]

    return students, variants, IDs


def saveDB(students, variants, IDs):
    std = open("studentsID.txt", 'w', encoding="UTF8")
    var = open("variantsID.txt", 'w', encoding="UTF8")
    id = open("IDTable.txt", 'w', encoding="UTF8")

    for i in students.keys():
        std.write(f'{i} {students[i]}\n')

    for i in variants.keys():
        var.write(f'{i} {variants[i]}\n')

    for i in IDs.keys():
        id.write(f'{i} {IDs[i]}\n')

    std.close()
    var.close()
    id.close()


def uploadDB():
    return getStudentsVariantsIDs()


def fillDB(students, variants, IDs):
    studentsList = input('Введите название файла со студентами: ')
    a = open(f"C://Users/matve/PycharmProjects/DataBase/{studentsList}", encoding="UTF8")
    stds = list(map(lambda x: x.rstrip(), a.readlines()))
    for i in stds:
        addStudent(i, students, variants, IDs)
    return IDs


def createBackUp(name, students, variants, IDs):
    os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}/backup")
    saveDB(students, variants, IDs)
    os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}")


def uploadBackUp(name):
    os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}/backup")
    students, variants, IDs = getStudentsVariantsIDs()
    os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}")
    saveDB(students, variants, IDs)
    return students, variants, IDs
