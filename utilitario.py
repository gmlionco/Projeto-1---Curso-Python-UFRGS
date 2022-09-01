"""
Curso: Introdução à programação Python

Projeto 1
Organizar arquivos nas pastas planilhas e documentos
de acordo com a extens˜ao do arquivo

Autor: Guilherme Medeiros Lionço
Data: 01/09/2022
Versão:0.0.1

Arquivo funções - Utilitário
"""

#importação dos pacotes
import os
import shutil

#criação das pastas
def criar_pastas(nome_diretorio: str):
    if os.path.exists(nome_diretorio) == False:
        os.mkdir(nome_diretorio)

#movimentação dos arquivos nas pastas       
def mover_arquivos(arquivos: list):
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
