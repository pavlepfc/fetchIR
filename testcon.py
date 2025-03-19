import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SQL-SERV-2022\\DBSERVER2022;"
    "DATABASE=finireg;"
    "UID=irfin;"
    "PWD=Potvrda2025"
)
try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")