import pymssql

with pymssql.connect(server='172.20.32.1',
                     database='AdventureWorks2022',
                     user='aktanbek',
                     password='Arzymamat5'

                     ) as conn:
    print("Connection established successfully.")

    cursor = conn.cursor()
    cursor.execute('SELECT 1 AS test_column')
    result = cursor.fetchone()
    print("Query executed successfully:", result)
