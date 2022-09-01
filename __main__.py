"""
Curso: Introdução à programação Python

Projeto 1
Organizar arquivos nas pastas planilhas e documentos
de acordo com a extens˜ao do arquivo

Autor: Guilherme Medeiros Lionço
Data: 01/09/2022
Versão:0.0.1

Arquivo principal - Main
"""

print ("Este programa criará as pastas documentos e planilhas e organizará os arquivos.")

import utilitario
import os
import shutil

def main():
    arquivos = os.listdir()
    for diretorio in ['documentos','planilhas']:
        utilitario.criar_pastas(diretorio)    
    utilitario.mover_arquivos(arquivos)

if __name__ == "__main__":
    main()

print ("\nA criação das pastas e a organização dos arquivos foi finalizada.")
