import pymssql

conn = pymssql.connect(
    server='169.254.119.77',
    user='aktanbek',
    password='Arzymamat5',
    database='AdventureWorks2022',
    as_dict=True
)
cursor = conn.cursor()
cursor.execute('SELECT TOP 10 * FROM person.person')
records = cursor.fetchall()
print(records)
conn.close()
