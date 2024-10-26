import pymssql

conn = pymssql.connect(server="192.168.86.3", port="1433", user="aktanbek", password="Arzymamat5", database="AdventureWorks2022")
cursor = conn.cursor()
cursor.execute("SELECT 1")
print("Connection successful") if cursor.fetchone() else print("Connection failed")
conn.close()

