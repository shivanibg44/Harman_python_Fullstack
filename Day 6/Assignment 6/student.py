import sqlite3 as s
from prettytable import PrettyTable
connection = s.connect("Student.db")

listoftables = connection.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENTDATA'").fetchall()

if listoftables != []:
    print("Table already exist")
else:
    connection.execute(''' CREATE TABLE STUDENTDATA(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    STUDENT_NAME TEXT,
                    ROLL_NUMBER INTEGER,
                    ADMISSION_NUMBER INTEGER,
                    EXAM_NAME TEXT,
                    ENGLISH_MARK INTEGER,
                    MATHS_MARK INTEGER,
                    PHYSICS_MARK INTEGER,
                    CHEMISTRY_MARK INTEGER,
                    BIO_MARK INTEGER
    ) ''')
    print("Table created Successfully")


while True:
    print("Select an option from the menu")
    print("1.Insert a Student Data ")
    print("2.View All Students ")
    print("3.Search a Student using Partial name ")
    print("4.Search a Student using either admission number or roll number ")
    print("5.Update a Student data with admission number ")
    print("6.Delete a Student data with admission number ")
    print("7.Display physics topper details ")
    print("8.Display count of total number of students ")
    print("9.Display average mark of students in english ")
    print("10.Display student details who scored less than average in maths ")
    print("11.Display student details who scored more than average in chemistry ")
    print("12.Exit ")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        getSname = input("Enter Student Name: ")
        getRno = input("Enter Roll Number: ")
        getAno = input("Enter Admission Number: ")
        getExamname = input("Enter Exam Name: ")
        getEng = input("Enter English Mark: ")
        getMath = input("Enter Maths Mark ")
        getPhy = input("Enter Physics Mark: ")
        getChem = input("Enter Chemistry Mark: ")
        getBio = input("Enter Biology Mark: ")

        connection.execute(" INSERT INTO STUDENTDATA(STUDENT_NAME, ROLL_NUMBER, ADMISSION_NUMBER, EXAM_NAME, \
                    ENGLISH_MARK, MATHS_MARK, PHYSICS_MARK, CHEMISTRY_MARK, BIO_MARK) VALUES('" + getSname + "'," + getRno + ",\
                    " + getAno + ",'" + getExamname + "'," + getEng + "," + getMath + "," + getPhy + "," + getChem + "," + getBio + ")")
        connection.commit()
        print("Inserted Successfully")





    elif choice == 2:
        result = connection.execute("SELECT * FROM STUDENTDATA ORDER BY ROLL_NUMBER")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)


    elif choice == 3:
        getSname = input("Enter Student Name (Single Letter or multiple letters): ")

        result = connection.execute("SELECT * FROM STUDENTDATA WHERE STUDENT_NAME LIKE '%" + getSname + "%'")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)

    elif choice == 4:
        getAno = input("Enter Admission number: ")
        getRno = input("Enter Roll number: ")

        result = connection.execute(
            "SELECT * FROM STUDENTDATA WHERE ADMISSION_NUMBER=" + getAno + " OR ROLL_NUMBER=" + getRno)
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)


    elif choice == 5:
        getAno = input("Enter Admission Number ")

        getNsname = input("Enter New Student Name: ")
        getNrno = input("Enter New Roll Number: ")
        getNano = input("Enter New Admission Number: ")
        getNexamname = input("Enter New Exam Name: ")
        getNeng = input("Enter New English Mark: ")
        getNmath = input("Enter New Maths Mark ")
        getNphy = input("Enter New Physics Mark: ")
        getNchem = input("Enter New Chemistry Mark: ")
        getNbio = input("Enter New Biology Mark: ")

        result = connection.execute(" UPDATE STUDENTDATA SET STUDENT_NAME='" + getNsname + "', ROLL_NUMBER=" + getNrno + ", \
                    ADMISSION_NUMBER=" + getNano + ", EXAM_NAME='" + getNexamname + "', ENGLISH_MARK=" + getNeng + ",\
                    MATHS_MARK=" + getNmath + ",PHYSICS_MARK=" + getNphy + ",CHEMISTRY_MARK=" + getNchem + ",\
                    BIO_MARK=" + getNbio + " WHERE ADMISSION_NUMBER=" + getAno)
        connection.commit()
        print("Updated Successfully")



    elif choice == 6:
        getAno = input("Enter Admission Number ")

        result = connection.execute("DELETE FROM STUDENTDATA WHERE ADMISSION_NUMBER=" + getAno)
        connection.commit()
        print("Deleted Successfully")


    elif choice == 7:
        result = connection.execute("SELECT * FROM STUDENTDATA WHERE PHYSICS_MARK=\
            (SELECT MAX(PHYSICS_MARK) as physics FROM STUDENTDATA )")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)




    elif choice == 8:
        result = connection.execute("SELECT COUNT(*) as count FROM STUDENTDATA ")
        table = PrettyTable(["Count"])
        for i in result:
            table.add_row([i[0]])
        print(table)


    elif choice == 9:
        result = connection.execute("SELECT AVG(ENGLISH_MARK) as engmark FROM STUDENTDATA ")
        table = PrettyTable(
            ["Average English Mark"])
        for i in result:
            table.add_row([i[0]])
        print(table)



    elif choice == 10:
        result = connection.execute(
            "SELECT * FROM STUDENTDATA WHERE MATHS_MARK<(SELECT AVG(MATHS_MARK) as mmark FROM STUDENTDATA )")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)





    elif choice == 11:
        result = connection.execute(
            "SELECT * FROM STUDENTDATA WHERE CHEMISTRY_MARK>(SELECT AVG(CHEMISTRY_MARK) as cmark FROM STUDENTDATA )")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)




    elif choice == 12:
        connection.close()
        break

    else:
        print("ic")


