import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

#cоздаем таблицу employees
cursor.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department_id INTEGER
)
''')

#cоздаем таблицу departments
cursor.execute('''
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
)
''')

#cоздаем таблицу projects
cursor.execute('''
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    department_id INTEGER
)
''')

#вставляем данные в таблицу employees
employees_data = [
    (1, 'John', 'Doe', 10),
    (2, 'Jane', 'Smith', 20),
    (3, 'Emily', 'Davis', None),
    (4, 'Michael', 'Brown', 30)
]
cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees_data)

#вставляем данные в таблицу departments
departments_data = [
    (10, 'HR'),
    (20, 'IT'),
    (30, 'Marketing'),
    (40, 'Sales')
]
cursor.executemany('INSERT INTO departments VALUES (?, ?)', departments_data)

#вставляем данные в таблицу projects
projects_data = [
    (1, 'Project Alpha', 10),
    (2, 'Project Beta', 20),
    (3, 'Project Gamma', None),
    (4, 'Project Delta', 40)
]
cursor.executemany('INSERT INTO projects VALUES (?, ?, ?)', projects_data)

#выполняем SQL-запрос
query = '''
SELECT 
    e.first_name,
    e.last_name,
    d.department_name,
    p.project_name
FROM 
    employees e
LEFT JOIN 
    departments d ON e.department_id = d.department_id
RIGHT JOIN 
    projects p ON d.department_id = p.department_id
'''

#получаем результаты запроса
df = pd.read_sql_query(query, conn)

#закрываем соединение
conn.close()

#выводим результат
print(df)