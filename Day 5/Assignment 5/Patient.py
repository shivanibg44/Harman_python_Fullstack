import sqlite3

conn = sqlite3.connect("Hospital.db")
conn.execute(''' CREATE TABLE IF NOT EXISTS PATIENTS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT,
                ADDRESS TEXT,
                PHNO TEXT,
                EMAIL_ID TEXT,
                PINCODE INTEGER
);''')
print("Table Creation Successful")

getName = input("Enter the Name- ")
getAdd = input("Enter Address- ")
getPhno = input("Enter Phone Number- ")
getEmail = input("Enter the Email- ")
getPincode = input("Enter the Pincode- ")

conn.execute("INSERT INTO PATIENTS(NAME,ADDRESS,PHNO,EMAIL_ID,PINCODE) VALUES ('"+getName+"','"+getAdd+"','"+getPhno+"','"+getEmail+"','"+getPincode+"')")
print("Entry Created successfully")
conn.commit()
conn.close()
