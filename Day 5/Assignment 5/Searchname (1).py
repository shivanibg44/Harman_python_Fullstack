import sqlite3
conn = sqlite3.connect("Hospital.db")
getName = input("Enter the Name- ")
cursor = conn.execute("SELECT * FROM DOCTORS WHERE NAME='"+getName+"'")
for i in cursor:
    print("Name-", i[0])
    print("Email-", i[1])
    print("Qualification-", i[2])
    print("Address-", i[3])
    print("Phone Number-", i[4])
    print("------------------------------------------------------")