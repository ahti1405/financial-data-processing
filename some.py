import pymssql

try:
    conn = pymssql.connect(server="127.0.0.1", port="1433", user="TestLogin", password="Arzymamat5", database="AdventureWorks2022")
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print("Connection successful") if cursor.fetchone() else print("Connection failed")
    conn.close()
except pymssql.InterfaceError as e:
    print(f"Interface error: {e}")
except pymssql.OperationalError as e:
    print(f"Operational error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
