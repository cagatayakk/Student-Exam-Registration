import sqlite3
import os

ROOT_DIR =os.path.dirname(os.path.realpath(__file__))
myPath=os.path.join(ROOT_DIR,'StudentExamRegistration.db')
myPath = r'%s'%myPath

con=sqlite3.connect(myPath)
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
    StudentNumber integer PRIMARY KEY,
    Name text,
    Surname text,
    Class text
) """)

cursor.execute("CREATE TABLE IF NOT EXISTS AllLessons(Lesson TEXT , Teacher TEXT)")

def studentList():
    print("\nStudents List\n")
    cursor.execute("SELECT * FROM Students")
    list_students=cursor.fetchall()
    for student in list_students:
        print(f"Student Number: {student[0]}",' '*(10 - len(str(student[0]))),f"Name: {student[1]}",' '*(10 - len(student[1])),
        f"Surname : {student[2]}",' '*(10 - len(student[2])),f"Class : {student[3]}",' '*(10 - len(student[3])))

def lessonsList():
    print("\nLessons List\n")
    cursor.execute("SELECT * FROM AllLessons")
    list_lesson=cursor.fetchall()
    for lesson in list_lesson:
        print(f"{lesson[0]}",' '*(10 - len(lesson[0])),f"Teacher: {lesson[1]}",' '*(10 - len(lesson[1])))

def addStudent():
    print("\nPlease Enter the following information to add a student.\n")
    try:
        std_num = int(input("Student Number:"))
        name = input("Name     :")
        surname = input("Surname  :")
        std_class = input("Class  :")

        add_command = "INSERT INTO Students VALUES {} "
        data =(std_num,name,surname,std_class)
        cursor.execute(add_command.format(data))
        print(f"Student number {std_num} was successfully added ")
    except:
        print("You entered an incorrect value!!")

def delStudent():
    try:
        std_num = int(input("\nEnter the number of the student you want to delete  :  \n"))
        add_command = "DELETE FROM Students WHERE StudentNumber = {} "
        data =(std_num)
        cursor.execute(add_command.format(data))

        cursor.execute("SELECT * FROM AllLessons")
        list_lessons=cursor.fetchall()
        for lesson in list_lessons:
            add_command="DELETE FROM {} WHERE StudentNumber= {} "
            cursor.execute(add_command.format(lesson[0],std_num))
        print(f"Student number {std_num} was successfully deleted")
    except:
        print("You entered an incorrect value!!")


def addLesson():
    try:        
        lesson = (input("\nPlease enter the name of the lesson you want to add : ")).lower()
        teacher = (input("Please enter teacher's name and surname :  ")).lower()
        add_command = "INSERT INTO AllLessons VALUES {} "
        data =(lesson,teacher)
        cursor.execute(add_command.format(data))

        add_command = """CREATE TABLE IF NOT EXISTS {}(
            FirstExam int,
            SecondExam int,
            PerformanceGrade int,
            Average int,
            StudentNumber integer NOT NULL ,
            FOREIGN KEY(StudentNumber) REFERENCES Students(StudentNumber))"""
        cursor.execute(add_command.format(lesson))
        print(f"{lesson} lesson successfully added")
    except:
        print("You entered an incorrect value!!")

def delLesson():
    try:
        lesson = (input("\nPlease enter the name of the lesson you want to delete :  ")).lower()
        add_command = ("DELETE FROM AllLessons WHERE Lesson = '{}'")
        cursor.execute(add_command.format(lesson))
        
        add_command = ("DROP TABLE {}")
        cursor.execute(add_command.format(lesson))
        print(f"{lesson} lesson successfully deleted")
    except:
        print("You entered an incorrect value!!")


def addNote():
    try:
        std_num = int(input("\nPlease enter Student number  : "))
        lesson=(input("Which lesson would you like to add notes for  : ")).lower() 
        exam1= int(input("Please Enter first Exam   :  "))
        exam2= int(input("Please Enter second Exam  : "))
        perform_grade= int(input("Please Enter performance Grade  : "))
        average = int(round(exam1+exam2+perform_grade)/3)
        add_command = "INSERT INTO {} VALUES {} "
        data =(exam1 ,exam2 ,perform_grade , average , std_num)
        cursor.execute(add_command.format(lesson,data))
        print("Exam results successfully added")
    except:
        print("You entered an incorrect value!!")
 

def showAverages():
    try:
        num = int(input("\n\nPlease enter Student number :  "))

        add_command="SELECT Name,Surname,Class FROM Students WHERE StudentNumber = {} "
        cursor.execute(add_command.format(num))
        list_students=cursor.fetchall()
        print(f"Name: {list_students[0][0]}   Surname: {list_students[0][1]}   Class: {list_students[0][2]}")

        cursor.execute("SELECT * FROM AllLessons")
        list_lessons=cursor.fetchall()
        for lesson in list_lessons:
            try:            
                add_command="SELECT Average FROM {} WHERE StudentNumber= {} "
                cursor.execute(add_command.format(lesson[0],num))
                list_average=cursor.fetchall()
                print(f"{lesson[0]} Average",' '*(9-len(lesson[0])) ,"=", list_average[0][0] )
            except IndexError:
                continue
    except:
        print("You entered an incorrect value!!")


def showExams():
    try:
        num = int(input("\n\nPlease enter Student number :  "))
        add_command="SELECT Name,Surname,Class FROM Students WHERE StudentNumber = {} "
        cursor.execute(add_command.format(num))
        list_students=cursor.fetchall()
        print(f"Name: {list_students[0][0]}   Surname: {list_students[0][1]}   Class: {list_students[0][2]}")

        lesson = (input("\nPlease enter lesson         : ")).lower()
        add_command="SELECT FirstExam,SecondExam,PerformanceGrade,Average FROM {} WHERE StudentNumber = {} "
        cursor.execute(add_command.format(lesson,num))
        list_lesson=cursor.fetchall()
        print(f"1. Exam             : {list_lesson[0][0]}")
        print(f"2. Exam             : {list_lesson[0][1]}")
        print(f"Performance Grage   : {list_lesson[0][2]}")
        print(f"Average             : {list_lesson[0][3]}")
    except IndexError:
        print(f"Student with number {num} has no Note in {lesson}")
    except:
        print("You entered an incorrect value!!")