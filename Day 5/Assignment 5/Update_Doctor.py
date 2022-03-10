import sqlite3
conn = sqlite3.connect("Hospital.db")
getPhno = input("Enter the Phone Number= ")
getName = input("Enter the Name- ")
getEmail = input("Enter the Email- ")
getQuali = input("Enter the Qualification- ")
getAdd = input("Enter Address- ")


cursor = conn.execute("UPDATE DOCTORS SET NAME='"+getName+"',EMAIL_ID='"+getEmail+"',QUALIFICATION='"+getQuali+"',ADDRESS='"+getAdd+"' WHERE PHNO='"+getPhno+"'")
conn.commit()
print("Entry Updated successfully")
cursor = conn.execute("SELECT * FROM DOCTORS WHERE PHNO='"+getPhno+"'")
print("UPDATED RECORD")
for i in cursor:
    print("Name-", i[0])
    print("Email-", i[1])
    print("Qualification-", i[2])
    print("Address-", i[3])
    print("Phone Number-", i[4])
    print("------------------------------------------------------")