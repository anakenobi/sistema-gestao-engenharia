
import func_auxiliares as aux
import dados as dg

def calcular_soma_lista(lista):
    
    soma = 0
    for valor in lista:
        soma += valor
    return soma

def calcular_custo_total():
    
    if not dg.consumo_semanal or not dg.materiais:
        return 0
    
    lista_materiais = list(dg.materiais.keys())
    custo_total = 0
    
    for i, material in enumerate(lista_materiais):
        total_consumido = 0
        
        for semana in dg.consumo_semanal:
            if i < len(semana):
                total_consumido += semana[i]
        
        custo_total += total_consumido * dg.materiais[material]['preco']
    
    return custo_total

def calcular_divisao_recursos():
    
    aux.limpar_tela()
    print("=" * 50)
    print("Divisão de recursos")
    print("=" * 50)
    
    total_recursos = aux.validar_numero("\nTotal de recursos disponíveis: ", 'float')
    num_equipes = aux.validar_numero("Número de equipes: ")
    
    if num_equipes == 0:
        print("Número de equipes deve ser maior que zero!")
        aux.pausar()
        return
    
    por_equipe = total_recursos / num_equipes
    resto = total_recursos - (por_equipe * num_equipes)
    
    print(f"\nResultado - Divisão")
    print(f"Cada equipe recebe: {por_equipe:.2f} unidades")
    print(f"Resto (sobra): {resto:.2f} unidades")
    
    aux.pausar()

def exibir_custo_total():
    """Exibe o custo total do projeto"""
    aux.limpar_tela()
    print("=" * 50)
    print("CUSTO TOTAL DO PROJETO")
    print("=" * 50)
    custo = calcular_custo_total()
    print(f"\nCusto total de materiais: R$ {custo:.2f}")
    aux.pausar()