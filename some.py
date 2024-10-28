import pymssql

conn = pymssql.connect(
    server='127.0.0.1',
    user='aktanbek',
    password='Arzymamat5',
    database='AdventureWorks2022',
    tds_version='7.3',
    as_dict=True
)
cursor = conn.cursor()
cursor.execute('SELECT TOP 10 * FROM person.person')
records = cursor.fetchall()
print(records)
conn.close()
