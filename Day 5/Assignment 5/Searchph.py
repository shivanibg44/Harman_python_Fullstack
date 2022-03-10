import sqlite3
conn = sqlite3.connect("Hospital.db")
getPhno = input("Enter the Phone Number= ")
cursor = conn.execute("SELECT * FROM DOCTORS WHERE PHNO='"+getPhno+"'")
for i in cursor:
    print("Name-", i[0])
    print("Email-", i[1])
    print("Qualification-", i[2])
    print("Address-", i[3])
    print("Phone Number-", i[4])
    print("------------------------------------------------------")