#!/usr/bin/env python3
"""
Script para corrigir problemas de encoding no projeto
"""

import os


def fix_encoding_issues():
    """Corrige problemas de encoding em arquivos Python"""

    # Arquivos para corrigir
    files_to_fix = [
        "main.py",
        "database.py",
        "schemas.py",
        "models.py"
    ]

    for file_path in files_to_fix:
        if os.path.exists(file_path):
            print(f"Corrigindo {file_path}...")

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Substituir caracteres especiais
            replacements = {
                'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
                'é': 'e', 'è': 'e', 'ê': 'e',
                'í': 'i', 'ì': 'i', 'î': 'i',
                'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o',
                'ú': 'u', 'ù': 'u', 'û': 'u',
                'ç': 'c',
                'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A',
                'É': 'E', 'È': 'E', 'Ê': 'E',
                'Í': 'I', 'Ì': 'I', 'Î': 'I',
                'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O',
                'Ú': 'U', 'Ù': 'U', 'Û': 'U',
                'Ç': 'C'
            }

            for old, new in replacements.items():
                content = content.replace(old, new)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"OK: {file_path} corrigido")


def main():
    """Função principal"""
    print("CORRIGINDO PROBLEMAS DE ENCODING")
    print("=" * 40)

    fix_encoding_issues()

    print("\nSUCESSO: Problemas de encoding corrigidos!")


if __name__ == "__main__":
    main()
