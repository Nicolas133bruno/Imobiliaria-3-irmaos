import sqlite3
import re

# Connect to the database
conn = sqlite3.connect('imobiliaria.db')
cursor = conn.cursor()

# Get all CPF values from Usuario table
cursor.execute('SELECT id_usuario, cpf FROM Usuario')
rows = cursor.fetchall()

print("CPF values in the database (cleaned):")
for row in rows:
    cpf_clean = re.sub(r'\D', '', row[1])
    print(f'ID: {row[0]}, CPF: {row[1]}, Clean: {cpf_clean}')

conn.close()