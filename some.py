import pymssql

# Connect using Windows Authentication
connection = pymssql.connect(server='192.168.0.104',
                             database='TRN',
                             autocommit=True)

# Optional: Set the connection to enforce encryption if needed
# Note: pymssql does not have a built-in parameter for SSL in the connection string.
# This might require custom configurations on the server and client side.

try:
    cursor = connection.cursor()
    cursor.execute('SELECT 1 AS test_column')
    result = cursor.fetchone()
    print("Query executed successfully:", result)
finally:
    connection.close()

