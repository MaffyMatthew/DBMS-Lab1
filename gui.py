import shutil
import sys
import os
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from design import Ui_DataBase


class DataBase(QMainWindow):
    in_base = False
    students, variants, IDs = {}, {}, {}

    def __init__(self):
        super(DataBase, self).__init__()
        self.ui = Ui_DataBase()
        self.ui.setupUi(self)

        self.ui.create.clicked.connect(lambda: self.createDB(name=self.ui.dbName.toPlainText()))
        self.ui.open.clicked.connect(lambda: self.openDB(name=self.ui.dbName.toPlainText()))
        self.ui.fill.clicked.connect(lambda: self.fillDB(studentList=self.ui.textFill.toPlainText()))
        self.ui.add_std.clicked.connect(lambda: self.addStudent(student=self.ui.textAdd.toPlainText()))
        self.ui.add_var.clicked.connect(lambda: self.addVariant(variant=self.ui.textAdd.toPlainText()))
        self.ui.delete_std.clicked.connect(lambda: self.deleteStudent(std_id=self.ui.studentID.toPlainText()))
        self.ui.delete_var.clicked.connect(lambda: self.deleteVariant(std_id=self.ui.variantID.toPlainText()))
        self.ui.edit_std.clicked.connect(lambda: self.editStudent(std_id=self.ui.studentID.toPlainText()))
        self.ui.edit_var.clicked.connect(lambda: self.editVariant(var_id=self.ui.variantID.toPlainText()))
        self.ui.giveVar.clicked.connect(lambda: self.giveVariant())
        self.ui.save.clicked.connect(lambda: self.saveDB())
        self.ui.upload.clicked.connect(lambda: self.uploadDB())
        self.ui.createBU.clicked.connect(lambda: self.createBackUp(name=self.ui.dbName.toPlainText()))
        self.ui.uploadBU.clicked.connect(lambda: self.uploadBackUp(name=self.ui.dbName.toPlainText()))
        self.ui.print_std.clicked.connect(lambda: self.printStudents(table=self.students))
        self.ui.print_vars.clicked.connect(lambda: self.printVariants(table=self.variants))
        self.ui.print_IDs.clicked.connect(lambda: self.printIDs(table=self.IDs))
        self.ui.print_all.clicked.connect(lambda: self.printStudentVarTable())
        self.ui.print_info.clicked.connect(lambda: self.printInfo(studentID=self.ui.stdID.toPlainText()))
        self.ui.pushButton.clicked.connect(lambda: self.deleteDB(name=self.ui.dbName.toPlainText()))

    def createDB(self, name):
        if len(name) > 0:
            filename = f"C://Users/matve/PycharmProjects/DataBase/{name}"
            if os.path.exists(filename):
                self.ui.label.setText('Database with this name already exists')
                print('Database with this name already exists')
            else:
                os.mkdir(filename)
                os.chdir(filename)
                os.mkdir(f"C://Users/matve/PycharmProjects/DataBase/{name}/backup")
                self.ui.label.setText(f"Database '{name}' was successfully created\n")
                print(f"Database '{name}' was successfully created\n")

                if self.students != {} and self.variants != {} and self.IDs != {}:
                    self.students, self.variants, self.IDs = {}, {}, {}

                if not os.path.exists(f"C://Users/matve/PycharmProjects/DataBase/{name}/studentsID.txt"):
                    self.createStudentsTable()

                if not os.path.exists(f"C://Users/matve/PycharmProjects/DataBase/{name}/variantsID.txt"):
                    self.createVariantsTable()

                self.createIDTable()
                self.in_base = True
                self.ui.tableWidget.horizontalHeader().setVisible(True)
        else:
            self.ui.label.setText('Enter correct name of database')
            print('Enter correct name of database')

    def openDB(self, name):
        if len(name) > 0:
            filename = f"C://Users/matve/PycharmProjects/DataBase/{name}"
            if os.path.exists(filename):
                os.chdir(filename)
                self.ui.label.setText(f"Database '{name}' was opened\n")
                print(f"Database '{name}' was opened\n")
                self.getStudentsVariantsIDs()
                self.in_base = True
                self.ui.tableWidget.horizontalHeader().setVisible(True)
            else:
                self.ui.label.setText('Database with this name does not exist(')
                print('Database with this name does not exist(')
        else:
            self.ui.label.setText('Enter correct name of database')
            print('Enter correct name of database')

    def createStudentsTable(self):
        file = open("studentsID.txt", 'w', encoding="UTF8")

        for i in range(len(self.students)):
            file.write(f"{i + 1} {self.students[i]}\n")

        self.students = dict(zip(map(str, list(range(1, len(self.students) + 1))), self.students))
        print("studentsID have been successfully created")

        file.close()

    def createVariantsTable(self):
        file = open("variantsID.txt", "w", encoding="UTF8")

        for i in range(len(self.variants)):
            file.write(f"{i + 1} {self.variants[i]}\n")

        self.variants = dict(zip(map(str, list(range(1, len(self.variants) + 1))), self.variants))
        print("variantID have been successfully created")

        file.close()

    def createIDTable(self):
        students = open("studentsID.txt", encoding="UTF8")
        variants = open("variantsID.txt", encoding="UTF8")
        var = list(variants.readlines())
        ID_table = open("IDTable.txt", 'w', encoding="UTF8")
        self.IDs = {}

        for i in list(students.readlines()):
            std_id = int(i.split()[0])
            var_id = random.randint(1, len(var))
            print(f'{std_id} {var_id}', file=ID_table)
            self.IDs[str(std_id)] = str(var_id)

        students.close()
        variants.close()
        ID_table.close()

    def fillDB(self, studentList):
        if self.in_base:
            if len(self.variants) > 0 and len(studentList) > 0:
                if os.path.exists(f"C://Users/matve/PycharmProjects/DataBase/{studentList}"):
                    a = open(f"C://Users/matve/PycharmProjects/DataBase/{studentList}", encoding="UTF8")
                    stds = list(map(lambda x: x.rstrip(), a.readlines()))
                    for i in stds:
                        self.addStudent(i)
                else:
                    self.ui.label.setText('No such file in the directory')
                    print('No such file in the directory')
            else:
                self.ui.label.setText('Add some variants before filling')
                print('Add some variants before filling')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def addStudent(self, student):
        if self.in_base:
            if len(student) > 0:
                if student in self.students.values():
                    self.ui.label.setText('Student with this name already exists!')
                    print('Student with that name already exists!')
                else:
                    if len(self.students) == 0:
                        self.students['1'] = student
                        self.IDs[str(max(list(map(int, list(self.students.keys())))))] = random.\
                            choice(list(self.variants.keys()))
                        self.ui.label.setText(f'{student} was successfully added')
                        print(f'{student} was successfully added')
                    else:
                        self.students[str(max(list(map(int, list(self.students.keys())))) + 1)] = student
                        self.IDs[str(max(list(map(int, list(self.students.keys())))))] = random.\
                            choice(list(self.variants.keys()))
                        self.ui.label.setText(f'{student} was successfully added')
                        print(f'{student} was successfully added')
            else:
                self.ui.label.setText('Enter correct name of student')
                print('Enter correct name of student')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def addVariant(self, variant):
        if self.in_base:
            if len(variant) > 0:
                if variant in self.variants.values():
                    self.ui.label.setText('Variant with this name already exists!')
                    print('Variant with this name already exists!')
                else:
                    if len(self.variants) == 0:
                        self.variants['1'] = variant
                    else:
                        self.variants[str(max(list(map(int, list(self.variants.keys())))) + 1)] = variant
            else:
                self.ui.label.setText('Enter correct name of variant')
                print('Enter correct name of variant')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def remakeIDs(self):
        self.IDs = {}
        for i in self.students.keys():
            self.IDs[i] = random.choice(list(self.variants.keys()))

    def deleteStudent(self, std_id):
        if self.in_base:
            if std_id in self.students:
                del self.students[std_id]
                del self.IDs[std_id]
            else:
                self.ui.label.setText('There is no student with such an ID!')
                print('There is no student with this ID!')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def deleteVariant(self, std_id):
        if self.in_base:
            if std_id in self.variants.keys():
                del self.variants[std_id]
                self.remakeIDs()
            else:
                self.ui.label.setText('There is no variant with such an ID!')
                print('There is no variant with such an ID!')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def editStudent(self, std_id):
        if self.in_base:
            if std_id in self.students.keys():
                student = self.ui.textAdd.toPlainText()
                if len(student) > 0:
                    if student in self.students.values():
                        self.ui.label.setText('Student with that name already exists!')
                        print('Student with that name already exists!')
                    else:
                        self.ui.label.setText(f'{self.students[std_id]} was replaced with {student}')
                        print(f'Student with id {std_id} - {self.students[std_id]}')
                        print(f'{self.students[std_id]} was replaced with {student}')
                        self.students[std_id] = student
                else:
                    self.ui.label.setText('Enter correct name of student')
                    print('Enter correct name of student')
            else:
                self.ui.label.setText('There is no student with this ID')
                print('There is no student with this ID')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def editVariant(self, var_id):
        if self.in_base:
            if var_id in self.variants.keys():
                variant = self.ui.textAdd.toPlainText()
                if len(variant) > 0:
                    if variant in self.variants.values():
                        self.ui.label.setText('Variant with this name already exists!')
                        print('Variant with this name already exists!')
                    else:
                        self.ui.label.setText(f'{self.variants[var_id]} was replaced with {variant}')
                        print(f'Variant with id {var_id} - {self.variants[var_id]}')
                        print(f'{self.variants[var_id]} was replaced with {variant}')

                        self.variants[var_id] = variant
                else:
                    self.ui.label.setText('Enter correct name of variant')
                    print('Enter correct name of variant')
            else:
                self.ui.label.setText('There is no object(s) with such an ID!')
                print('There is no option with such an ID')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def giveVariant(self):
        if self.in_base:
            std_id = self.ui.studentID.toPlainText()
            id_var = self.ui.variantID.toPlainText()
            if len(std_id) > 0 and len(id_var) > 0 and std_id in self.students.keys() and id_var in self.variants. \
                    keys():
                self.IDs[std_id] = id_var
            else:
                self.ui.label.setText('There is no object(s) with such an ID!')
                print('There is no object(s) with such an ID!')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def getStudentsVariantsIDs(self):
        students = open(f"studentsID.txt", encoding="UTF8")
        variants = open(f"variantsID.txt", encoding="UTF8")
        IDs = open(f"IDTable.txt", encoding="UTF8")
        std = list(map(lambda x: x.rstrip().partition(' '), list(students.readlines())))
        var = list(map(lambda x: x.rstrip().partition(' '), list(variants.readlines())))
        std_id = list(map(lambda x: x.rstrip().partition(' '), list(IDs.readlines())))
        students.close()
        variants.close()
        IDs.close()

        self.students, self.variants, self.IDs = {}, {}, {}
        for i in std:
            self.students[i[0]] = i[2]
        for i in var:
            self.variants[i[0]] = i[2]
        for i in std_id:
            self.IDs[i[0]] = i[2]

    def saveDB(self):
        if self.in_base:
            std = open("studentsID.txt", 'w', encoding="UTF8")
            var = open("variantsID.txt", 'w', encoding="UTF8")
            std_id = open("IDTable.txt", 'w', encoding="UTF8")

            for i in self.students.keys():
                std.write(f'{i} {self.students[i]}\n')

            for i in self.variants.keys():
                var.write(f'{i} {self.variants[i]}\n')

            for i in self.IDs.keys():
                std_id.write(f'{i} {self.IDs[i]}\n')

            std.close()
            var.close()
            std_id.close()
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def uploadDB(self):
        if self.in_base:
            self.getStudentsVariantsIDs()
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def createBackUp(self, name):
        if self.in_base:
            os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}/backup")
            self.saveDB()
            os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}")
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def uploadBackUp(self, name):
        if self.in_base:
            os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}/backup")
            self.getStudentsVariantsIDs()
            os.chdir(f"C://Users/matve/PycharmProjects/DataBase/{name}")
            self.saveDB()
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def printVariants(self, table):
        if self.in_base:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(2)
            self.ui.tableWidget.setColumnWidth(0, 15)
            self.ui.tableWidget.setRowCount(len(table))
            self.ui.tableWidget.setHorizontalHeaderLabels(['id', 'name'])
            self.ui.tableWidget.verticalHeader().setVisible(False)
            curr_row = 0
            for i in table.keys():
                item_i = QTableWidgetItem(i)
                self.ui.tableWidget.setItem(curr_row, 0, item_i)
                item_name = QTableWidgetItem(table[i])
                self.ui.tableWidget.setItem(curr_row, 1, item_name)
                curr_row += 1
                print(f'{i:4} {table[i]}')
            print()
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def printStudents(self, table):
        if self.in_base:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setColumnWidth(0, 15)
            self.ui.tableWidget.setColumnWidth(1, 100)
            self.ui.tableWidget.setRowCount(len(table))
            self.ui.tableWidget.setHorizontalHeaderLabels(['id', 'name', 'surname', 'patronymic'])
            self.ui.tableWidget.verticalHeader().setVisible(False)
            curr_row = 0
            for i in table.keys():
                item_i = QTableWidgetItem(i)
                self.ui.tableWidget.setItem(curr_row, 0, item_i)
                a = table[i].split()

                if len(a) > 0:
                    item_name = QTableWidgetItem(a[1])
                    self.ui.tableWidget.setItem(curr_row, 1, item_name)
                if len(a) > 1:
                    item_name = QTableWidgetItem(a[0])
                    self.ui.tableWidget.setItem(curr_row, 2, item_name)
                if len(a) > 2:
                    item_name = QTableWidgetItem(a[2])
                    self.ui.tableWidget.setItem(curr_row, 3, item_name)

                curr_row += 1
                print(f'{i:4} {table[i]}')
            print()
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def printIDs(self, table):
        if self.in_base:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(2)
            self.ui.tableWidget.setColumnWidth(0, 60)
            self.ui.tableWidget.setColumnWidth(1, 60)
            self.ui.tableWidget.setRowCount(len(table))
            self.ui.tableWidget.setHorizontalHeaderLabels(['student ID', 'variant ID'])
            self.ui.tableWidget.verticalHeader().setVisible(False)
            curr_row = 0
            for i in table.keys():
                item_i = QTableWidgetItem(i)
                self.ui.tableWidget.setItem(curr_row, 0, item_i)
                item_name = QTableWidgetItem(table[i])
                self.ui.tableWidget.setItem(curr_row, 1, item_name)
                curr_row += 1
                print(f'{i:4} {table[i]}')
            print()
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def printStudentVarTable(self):
        if self.in_base:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(2)
            self.ui.tableWidget.setColumnWidth(0, 300)
            self.ui.tableWidget.setRowCount(len(self.IDs))
            self.ui.tableWidget.setHorizontalHeaderLabels(['full name', 'variant'])
            self.ui.tableWidget.verticalHeader().setVisible(False)
            curr_row = 0
            for studentID in self.IDs.keys():
                a = QTableWidgetItem(self.students[studentID])
                self.ui.tableWidget.setItem(curr_row, 0, a)

                item_name = QTableWidgetItem(self.variants[self.IDs[studentID]])
                self.ui.tableWidget.setItem(curr_row, 1, item_name)
                curr_row += 1

                print(f'{studentID:4} {self.students[studentID]:35} {self.variants[self.IDs[studentID]]}')
            print()
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def printInfo(self, studentID):
        if self.in_base:
            if len(studentID) > 0 and studentID in self.students.keys():
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setColumnCount(5)
                self.ui.tableWidget.setColumnWidth(0, 15)
                self.ui.tableWidget.setRowCount(1)
                self.ui.tableWidget.setHorizontalHeaderLabels(['id', 'name', 'surname', 'patronymic', 'variant'])
                self.ui.tableWidget.verticalHeader().setVisible(False)

                item_i = QTableWidgetItem(studentID)
                self.ui.tableWidget.setItem(0, 0, item_i)
                a = self.students[studentID].split()

                if len(a) > 0:
                    item_name = QTableWidgetItem(a[1])
                    self.ui.tableWidget.setItem(0, 1, item_name)
                if len(a) > 1:
                    item_name = QTableWidgetItem(a[0])
                    self.ui.tableWidget.setItem(0, 2, item_name)
                if len(a) > 2:
                    item_name = QTableWidgetItem(a[2])
                    self.ui.tableWidget.setItem(0, 3, item_name)

                item_name = QTableWidgetItem(self.variants[self.IDs[studentID]])
                self.ui.tableWidget.setItem(0, 4, item_name)
                # print(f'{id:4} {self.students[studentID]:30} {self.variants[self.IDs[studentID]]}')
            else:
                self.ui.label.setText(f'There is no student with ID {studentID}')
                print(f'There is no student with ID {studentID}')
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')

    def deleteDB(self, name):
        if self.in_base:
            os.chdir(f"C://Users/matve/PycharmProjects/DataBase/")
            shutil.rmtree(f"C://Users/matve/PycharmProjects/DataBase/{name}")
            self.ui.dbName.clear()
            self.ui.tableWidget.horizontalHeader().setVisible(False)
            self.ui.tableWidget.clear()
            self.ui.textAdd.clear()
            self.ui.textFill.clear()
            self.ui.studentID.clear()
            self.ui.variantID.clear()
            self.ui.stdID.clear()
            self.in_base = False
        else:
            self.ui.label.setText('Log in to the database')
            print('Log in to the database')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    db = DataBase()
    db.show()

    sys.exit(app.exec())
