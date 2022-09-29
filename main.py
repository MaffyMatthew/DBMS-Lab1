from db import *

command = input('Введите команду: ')
in_base = False
students, variants, IDs = {}, {}, {}

while command != 'exit':
    command.split()

    if command == 'create':                                 # Создание БД v
        if in_base:
            saveDB(students, variants, IDs)
            os.chdir("C://Users/matve/PycharmProjects/DataBase")

        name = input("Введите имя Базы данных: ")
        students, variants, IDs = createDB(name, {}, ['var1', 'var2', 'var3', 'var4', 'var5'])
        in_base = True

    elif command == 'open':                                 # Открытие БД v
        if in_base:
            saveDB(students, variants, IDs)
            os.chdir("C://Users/matve/PycharmProjects/DataBase")

        name = input("Введите имя Базы данных: ")
        students, variants, IDs = openDB(name)
        in_base = True

    elif command == 'fill' and in_base:                     # v
        IDs = fillDB(students, variants, IDs)

    elif command == 'print students' and in_base:           # Вывод списка студентов v
        printTable(students)

    elif command == 'print variants' and in_base:                       # Вывод списка вариантов v
        printTable(variants)

    elif command == 'print IDs' and in_base:                            # Вывод таблицы ID-шников v
        printTable(IDs)

    elif command == 'print info':                                       # v
        printInfo(students, variants, IDs)

    elif command == 'print students with vars' and in_base:             # Вывод студентов с вариантами v
        printStudentVarTable(students, variants, IDs)

    elif command == 'add student' and in_base:                          # Добавление студента v
        student = input('Введите имя студента: ')
        addStudent(student, students, variants, IDs)

    elif command == 'add variant' and in_base:                          # Добавление варианта v
        variant = input('Введите название варианта: ')
        addVariant(variant, variants)

    elif command == 'delete student' and in_base:                       # Удаление студента v
        studentID = input('Введите ID студента: ')
        deleteStudent(studentID, students, IDs)

    elif command == 'delete variant' and in_base:                       # Удаление варианта v
        variantID = input('Введите ID варианта: ')
        variants, IDs = deleteVariant(variantID, variants, students)

    elif command == 'edit student' and in_base:                         # Редактирование студента по ID v
        studentID = input('Введите ID студента: ')
        editStudent(studentID, students)

    elif command == 'edit variant' and in_base:                         # Редакатирование варианта по ID v
        variantID = input('Введите ID варианта: ')
        editVariant(variantID, variants)

    elif command == 'give student var':                                 # v
        giveVariant(IDs)

    elif command == 'save' and in_base:                                 # Сохранение БД v
        saveDB(students, variants, IDs)

    elif command == 'upload' and in_base:                               # Загрузка сохранённой версии v
        students, variants, IDs = uploadDB()

    elif command == 'create backup' and in_base:                        # v
        createBackUp(name, students, variants, IDs)

    elif command == 'upload backup' and in_base:                        # v
        students, variants, IDs = uploadBackUp(name)

    else:
        print('Unknown command')

    command = input('Введите команду: ')

if in_base:
    saveDB(students, variants, IDs)
