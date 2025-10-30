import sqlite3

# Connect to the database
conn = sqlite3.connect('imobiliaria.db')
cursor = conn.cursor()

# Get all CPF values from Usuario table
cursor.execute('SELECT id_usuario, cpf FROM Usuario')
rows = cursor.fetchall()

print("CPF values in the database:")
for row in rows:
    print(f'ID: {row[0]}, CPF: {row[1]}')

conn.close()