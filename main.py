from module import *
while True:
    print("""
    Welcome to the Student Exam Registration System. Press q to exit.
     
    (1) Student list       -> Lists students in the database
    (2) Add Student        -> Adds a new student to the database
    (3) Delete Student     -> Deletes the student and all Exam Note from the database
    (4) Lessons list       -> Lists the lessons in the database
    (5) Add Lessons        -> Adds a new lesson to the database
    (6) Delete Lesson      -> Deletes lesson from database
    (7) Exam Note entry    -> Enters a grade for a student from the student table
    (8) Show Averages      -> Shows the averages of the exams of the student whose number is entered
    (9) Show Exam Results  -> Shows all exam results of the student from the desired course
    """)

    secim = input("Enter the number of the operation you want to execute  :  \n").lower()
    if secim == "q" :
        break
    elif secim == "1":
        studentList()
    elif secim == "2":
        addStudent()
    elif secim == "3":
        delStudent()
    elif secim == "4":
        lessonsList()
    elif secim == "5":
        addLesson()
    elif secim == "6":
        delLesson()
    elif secim == "7":
        addNote()
    elif secim == "8" :
        showAverages() 
    elif secim == "9" :
        showExams() 

con.commit()
con.close()
 aa
