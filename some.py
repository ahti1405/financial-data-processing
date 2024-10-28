import pymssql

with pymssql.connect(server='127.0.0.1',
                     database='AdventureWorks2022',
                     user='aktanbek',
                     password='Arzymamat5',
                     as_dict=True) as conn:
    print("Connection established successfully.")

    cursor = conn.cursor()
    cursor.execute('SELECT 1 AS test_column')
    result = cursor.fetchone()
    print("Query executed successfully:", result)
