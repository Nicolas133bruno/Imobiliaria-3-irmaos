#!/usr/bin/env python3
"""
Script para criar o banco de dados MySQL da Imobiliária 3 Irmãos
"""
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

def create_database():
    """Cria o banco de dados se não existir"""
    try:
        # Carregar variáveis de ambiente
        load_dotenv("config.env")
        
        # Configurações de conexão
        db_config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '3306'),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'root123'),
        }
        
        # Conectar ao MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Criar banco de dados se não existir
        database_name = os.getenv('DB_NAME', 'imobiliaria_3_irmaos')
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"✅ Banco de dados '{database_name}' criado/verificado com sucesso!")
        
        # Usar o banco de dados
        cursor.execute(f"USE {database_name}")
        
        # Executar script SQL para criar tabelas
        sql_file = "A empresa Imobilária 3irmãos.sql"
        if os.path.exists(sql_file):
            with open(sql_file, 'r', encoding='utf-8') as file:
                sql_script = file.read()
            
            # Executar comandos SQL individualmente
            commands = sql_script.split(';')
            for command in commands:
                command = command.strip()
                if command:
                    try:
                        cursor.execute(command)
                    except Error as e:
                        print(f"⚠️  Aviso ao executar comando: {e}")
            
            print("✅ Tabelas e dados inseridos com sucesso!")
        else:
            print(f"❌ Arquivo SQL não encontrado: {sql_file}")
        
        cursor.close()
        connection.close()
        print("✅ Conexão com MySQL estabelecida com sucesso!")
        
    except Error as e:
        print(f"❌ Erro ao conectar/criar banco de dados: {e}")
        print("📁 O sistema usará SQLite como fallback")

if __name__ == "__main__":
    create_database()