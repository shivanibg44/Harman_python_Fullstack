import sqlite3

conn = sqlite3.connect("Hospital.db")
getID = input("Enter the Patient id- ")
conn.execute("DELETE FROM PATIENTS WHERE ID="+getID)
conn.commit()
print("Entry Deleted successfully")
cursor = conn.execute("SELECT * FROM PATIENTS")
print("UPDATED RECORD")
for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Address-", i[2])
    print("Phone Number-", i[3])
    print("Email-", i[4])
    print("Pincode-", i[5])
    print("------------------------------------------------------")