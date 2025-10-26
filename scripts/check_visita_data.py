import sqlite3
from datetime import date

# Connect to the database
conn = sqlite3.connect('imobiliaria.db')
cursor = conn.cursor()

# Get all Visita data
cursor.execute('SELECT id_visita, data_visita, hora_visita, status_visita FROM Visita')
rows = cursor.fetchall()

print("Visita data in the database:")
for row in rows:
    visita_date = date.fromisoformat(row[1]) if row[1] else None
    is_past = visita_date < date.today() if visita_date else False
    hora_length = len(row[2]) if row[2] else 0
    hora_format_ok = hora_length <= 5
    
    print(f'ID: {row[0]}, Data: {row[1]} (past: {is_past}), Hora: "{row[2]}" (length: {hora_length}, format_ok: {hora_format_ok}), Status: {row[3]}')

conn.close()