import pymssql
import pytest

# Database connection details
DB_SERVER = "ntmachine.domain.com"  # Change if needed
DB_USER = "aktanbek"  # Your SQL Server username
DB_PASSWORD = "Arzymamat5"  # Your SQL Server password
DB_DATABASE = "AdventureWorks2022"  # Your database name

@pytest.fixture(scope="module")
def db_connection():
    """Establish a database connection."""
    conn = pymssql.connect(server=DB_SERVER, port="1433", user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,  tds_version='8.0')
    yield conn
    conn.close()

@pytest.fixture(scope="module")
def cursor(db_connection):
    """Return a cursor for executing queries."""
    return db_connection.cursor()

# Test cases for [Person].[Address] table
def test_verify_row_count_in_address_table(cursor):
    """Verify the total row count in the [Person].[Address] table."""
    cursor.execute("SELECT COUNT(*) FROM [Person].[Address];")
    row_count = cursor.fetchone()[0]
    assert row_count > 1000, f"Expected row count > 1000, got {row_count}"

def test_check_null_values_in_address_city(cursor):
    """Check that there are no NULL values in the [City] column of the [Person].[Address] table."""
    cursor.execute("SELECT COUNT(*) FROM [Person].[Address] WHERE [City] IS NULL;")
    null_count = cursor.fetchone()[0]
    assert null_count == 0, f"Expected no NULL values, but found {null_count}"

# Test cases for [Production].[Document] table
def test_verify_average_length_of_document_title(cursor):
    """Check the average length of the Title column in the [Production].[Document] table."""
    cursor.execute("SELECT AVG(LEN([Title])) FROM [Production].[Document];")
    avg_length = cursor.fetchone()[0]
    assert avg_length > 5, f"Expected average title length > 5, got {avg_length}"

def test_check_modified_date_range_in_document(cursor):
    """Ensure all ModifiedDate values in [Production].[Document] fall within a valid range."""
    cursor.execute(
        "SELECT COUNT(*) FROM [Production].[Document] WHERE [ModifiedDate] < '2000-01-01' OR [ModifiedDate] > GETDATE();"
    )
    invalid_dates = cursor.fetchone()[0]
    assert invalid_dates == 0, f"Expected no invalid dates, but found {invalid_dates}"

# Test cases for [Production].[UnitMeasure] table
def test_verify_max_length_of_unitmeasure_name(cursor):
    """Verify the maximum length of the Name column in [Production].[UnitMeasure]."""
    cursor.execute("SELECT MAX(LEN([Name])) FROM [Production].[UnitMeasure];")
    max_length = cursor.fetchone()[0]
    assert max_length <= 50, f"Expected max length <= 50, got {max_length}"

def test_verify_unique_unitmeasurecode(cursor):
    """Ensure UnitMeasureCode values are unique."""
    cursor.execute("SELECT COUNT(*) FROM [Production].[UnitMeasure];")
    total_rows = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT UnitMeasureCode) FROM [Production].[UnitMeasure];")
    unique_codes = cursor.fetchone()[0]

    assert total_rows == unique_codes, f"Expected all UnitMeasureCode values to be unique, but found duplicates."
