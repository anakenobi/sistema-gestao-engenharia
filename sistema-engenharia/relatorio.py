
from datetime import datetime
import func_auxiliares as aux
import dados as dg
import calculos
import notificacoes

def relatorio_consumo_por_semana():
    
    aux.limpar_tela()
    print("=" * 50)
    print("Relatório - Consumo por semana")
    print("=" * 50)
    
    if not dg.consumo_semanal:
        print("\nNenhum consumo registrado!")
        aux.pausar()
        return
    
    lista_materiais = list(dg.materiais.keys())
    
    print()
    for i, semana in enumerate(dg.consumo_semanal):
        total_semana = calculos.calcular_soma_lista(semana)
        print(f"Semana {i + 1}: {total_semana:.2f} unidades totais")
        
        for j, consumo in enumerate(semana):
            if j < len(lista_materiais):
                print(f"  - {lista_materiais[j]}: {consumo:.2f} {dg.materiais[lista_materiais[j]]['unidade']}")
        print()
    
    aux.pausar()

def relatorio_consumo_por_material():
    
    aux.limpar_tela()
    print("=" * 50)
    print("Relatório - Consumo por material")
    print("=" * 50)
    
    if not dg.consumo_semanal:
        print("\n Nenhum consumo registrado!")
        aux.pausar()
        return
    
    lista_materiais = list(dg.materiais.keys())
    
    print()
    for i, material in enumerate(lista_materiais):
        total_material = 0
        
        for semana in dg.consumo_semanal:
            if i < len(semana):
                total_material += semana[i]
        
        print(f"{material.upper()}: {total_material:.2f} {dg.materiais[material]['unidade']}")
    
    aux.pausar()

def relatorio_geral_projeto():
    
    aux.limpar_tela()
    print("=" * 50)
    print("Retório Geral do Projeto")
    print("=" * 50)
    
    print(f"\n Estatíticas Gerais")
    print(f"Engenheiros cadastrados: {len(dg.engenheiros)}")
    print(f"Tarefas totais: {len(dg.tarefas)}")
    print(f"Materiais cadastrados: {len(dg.materiais)}")
    print(f"Coordenadas da planta: {len(dg.coordenadas_planta)}")
    
    pendentes = 0
    em_andamento = 0
    concluidas = 0
    
    for tarefa in dg.tarefas:
        status = tarefa['status'].lower()
        if 'pendente' in status:
            pendentes += 1
        elif 'andamento' in status:
            em_andamento += 1
        elif 'concluida' in status:
            concluidas += 1
    
    print(f"\nStatus por tarefa")
    print(f"Pendentes: {pendentes}")
    print(f"Em Andamento: {em_andamento}")
    print(f"Concluídas: {concluidas}")
    
    if dg.materiais and dg.consumo_semanal:
        custo = calculos.calcular_custo_total()
        print(f"\nCusto total de materiais: R$ {custo:.2f}")
    
    print(f"\n  Tarefas para os próximos 7 dias")
    tarefas_proximas = notificacoes.verificar_tarefas_proximas()
    
    if tarefas_proximas:
        for tarefa in tarefas_proximas:
            dias_restantes = (tarefa['prazo'] - datetime.now()).days
            print(f"  - {tarefa['descricao']} ({dias_restantes} dias)")
    else:
        print("  Nenhuma tarefa próxima do prazo.")
    
    aux.pausar()