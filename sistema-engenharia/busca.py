
import func_auxiliares as aux
import dados as dg

def buscar_projeto():
    
    aux.limpar_tela()
    print("=" * 50)
    print("BUSCAR PROJETO/TAREFA")
    print("=" * 50)
    
    if not dg.tarefas:
        print("\nNenhuma tarefa cadastrada!")
        aux.pausar()
        return
    
    termo = input("\nDigite o nome do projeto ou palavra-chave: ").strip().lower()
    
    if not termo:
        print("Termo de busca vazio!")
        aux.pausar()
        return
    
    resultados = buscar_em_tarefas(termo)
    
    if not resultados:
        print(f"\nNenhum resultado encontrado para '{termo}'")
    else:
        print(f"\n{len(resultados)} resultado(s) encontrado(s):\n")
        
        for tarefa in resultados:
            print(f"{'=' * 50}")
            print(f"ID: {tarefa['id']}")
            print(f"Projeto: {tarefa['projeto']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Responsável: {tarefa['nome_engenheiro']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Prazo: {tarefa['prazo_str']}")
            print(f"Status: {tarefa['status']}")
            print(f"Data de criação: {tarefa['data_criacao']}")
    
    aux.pausar()

def buscar_em_tarefas(termo):
    
    resultados = []
    
    for tarefa in dg.tarefas:
        projeto_lower = tarefa['projeto'].lower()
        descricao_lower = tarefa['descricao'].lower()
        
        if termo in projeto_lower or termo in descricao_lower:
            resultados.append(tarefa)
    
    return resultados