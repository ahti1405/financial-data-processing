import pymssql

with pymssql.connect(server='192.168.0.100\SQLEXPRESS',
                     port='1433',
                     database='TRN',
                     user='aktanbek',
                     password='Arzymamat5',
                    timeout=600) as conn:
    print("Connection established successfully.")

    cursor = conn.cursor()
    cursor.execute('SELECT 1 AS test_column')
    result = cursor.fetchone()
    print("Query executed successfully:", result)
