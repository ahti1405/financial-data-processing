import pymssql

with pymssql.connect(server='localhost\SQLEXPRESS',
                     port='1433',
                     database='TRN',
                     user='aktanbek',
                     password='Arzymamat5',
                     as_dict=True,
                    timeout=60) as conn:
    print("Connection established successfully.")

    cursor = conn.cursor()
    cursor.execute('SELECT 1 AS test_column')
    result = cursor.fetchone()
    print("Query executed successfully:", result)
