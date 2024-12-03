import pyodbc

def connect_to_db():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=JUANP\SQLEXPRESS;'
        r'DATABASE=practicas_pro;'
        r'Trusted_Connection=yes;'
    )
    return conn