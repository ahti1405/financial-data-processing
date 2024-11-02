import pymssql

with pymssql.connect(server='0.0.0.0',
                     port='1433',
                     database='TRN',
                     user='aktanbek',
                     password='Arzymamat5',
                     as_dict=True) as conn:
    print("Connection established successfully.")

    cursor = conn.cursor()
    cursor.execute('SELECT 1 AS test_column')
    result = cursor.fetchone()
    print("Query executed successfully:", result)
