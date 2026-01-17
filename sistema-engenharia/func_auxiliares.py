# auxiliares.py
"""
Funções auxiliares do sistema
"""

import os
from datetime import datetime

def limpar_tela():
   
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    
    input("\nPressione Enter para continuar...")

def gerar_id(lista):
    
    return len(lista) + 1

def validar_numero(mensagem, tipo='int'):
    
    while True:
        try:
            valor = input(mensagem)
            if tipo == 'int':
                return int(valor)
            elif tipo == 'float':
                return float(valor)
        except ValueError:
            print("Valor inválido! Digite um número válido.")

def formatar_data(data_str):
   
    try:
        dia, mes, ano = map(int, data_str.split('/'))
        return datetime(ano, mes, dia)
    except:
        return None