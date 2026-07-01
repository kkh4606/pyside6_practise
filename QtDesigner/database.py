import sqlite3

conn = sqlite3.connect("employee.db")

cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY , name TEXT, employment_date TEXT, department TEXT, position TEXT, annual_salary REAL,job_description TEXT )"""
)
