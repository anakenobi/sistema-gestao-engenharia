
##Funções de visualização


import func_auxiliares as aux
import dados as dg

def visualizar_tarefas_engenheiro():
    
    aux.limpar_tela()
    print("=" * 50)
    print("MINHAS TAREFAS")
    print("=" * 50)
    
    if not dg.engenheiros:
        print("\nNenhum engenheiro cadastrado!")
        aux.pausar()
        return
    
    print("\n--- Engenheiros ---")
    for eng in dg.engenheiros:
        print(f"ID: {eng['id']} - {eng['nome']}")
    
    id_eng = aux.validar_numero("\nSeu ID: ")
    
    engenheiro = None
    for eng in dg.engenheiros:
        if eng['id'] == id_eng:
            engenheiro = eng
            break
    
    if not engenheiro:
        print("Engenheiro não encontrado!")
        aux.pausar()
        return
    
    print(f"\n--- Tarefas de {engenheiro['nome']} ---")
    
    tarefas_encontradas = []
    for tarefa in dg.tarefas:
        if tarefa['id_engenheiro'] == id_eng:
            tarefas_encontradas.append(tarefa)
    
    if not tarefas_encontradas:
        print("Nenhuma tarefa atribuída.")
    else:
        for tarefa in tarefas_encontradas:
            print(f"\nID: {tarefa['id']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Projeto: {tarefa['projeto']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Prazo: {tarefa['prazo_str']}")
            print(f"Status: {tarefa['status']}")
            print("-" * 40)
    
    print(f"\n--- Histórico de Tarefas Concluídas ---")
    if not engenheiro['tarefas_concluidas']:
        print("Nenhuma tarefa concluída.")
    else:
        for id_tarefa in engenheiro['tarefas_concluidas']:
            for tarefa in dg.tarefas:
                if tarefa['id'] == id_tarefa:
                    print(f"✓ {tarefa['descricao']} - {tarefa['projeto']}")
    
    aux.pausar()

def visualizar_coordenadas():
    
    aux.limpar_tela()
    print("=" * 50)
    print("COORDENADAS DA PLANTA")
    print("=" * 50)
    
    if not dg.coordenadas_planta:
        print("\nNenhuma coordenada cadastrada!")
        aux.pausar()
        return
    
    print("\n--- Pontos Cadastrados ---")
    for i, coord in enumerate(dg.coordenadas_planta):
        x, y, descricao = coord
        print(f"{i + 1}. ({x:.2f}, {y:.2f}) - {descricao}")
    
    aux.pausar()

def visualizar_planta():
    
    aux.limpar_tela()
    print("=" * 50)
    print("LAYOUT DA PLANTA")
    print("=" * 50)
    
    if not dg.planta_obra:
        print("\nPlanta não criada!")
        aux.pausar()
        return
    
    print("\nLegenda: . = vazio | X = ponto marcado\n")
    
    for linha in dg.planta_obra:
        for celula in linha:
            print(celula, end=' ')
        print()
    
    aux.pausar()

def visualizar_materiais():
    
    aux.limpar_tela()
    print("=" * 50)
    print("MATERIAIS CADASTRADOS")
    print("=" * 50)
    
    if not dg.materiais:
        print("\n Nenhum material cadastrado!")
        aux.pausar()
        return
    
    print()
    for nome, dados in dg.materiais.items():
        print(f"Material: {nome.upper()}")
        print(f"  Preço: R$ {dados['preco']:.2f}/{dados['unidade']}")
        print(f"  Estoque: {dados['estoque']:.2f} {dados['unidade']}")
        print(f"  Estoque mínimo: {dados['estoque_minimo']}")
        
        if dados['estoque'] <= dados['estoque_minimo']:
            print("  ESTOQUE BAIXO!")
        
        print("-" * 40)
    
    aux.pausar()

def visualizar_todas_tarefas():
    
    aux.limpar_tela()
    print("=" * 50)
    print("TODAS AS TAREFAS")
    print("=" * 50)
    
    if not dg.tarefas:
        print("\n Nenhuma tarefa cadastrada!")
    else:
        for tarefa in dg.tarefas:
            print(f"\nID: {tarefa['id']} | {tarefa['projeto']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Responsável: {tarefa['nome_engenheiro']}")
            print(f"Status: {tarefa['status']} | Prazo: {tarefa['prazo_str']}")
            print("-" * 40)
    
    aux.pausar()



##edições de tarefas

def editar_tarefa():
    
    aux.limpar_tela()
    print("=" * 50)
    print("EDITAR TAREFA")
    print("=" * 50)
    
    if not dg.tarefas:
        print("\nNenhuma tarefa cadastrada!")
        aux.pausar()
        return
    
    print("\n--- Tarefas ---")
    for tarefa in dg.tarefas:
        print(f"ID: {tarefa['id']} - {tarefa['descricao']} ({tarefa['status']})")
    
    id_tarefa = aux.validar_numero("\nID da tarefa a editar: ")
    
    tarefa_encontrada = None
    for tarefa in dg.tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa_encontrada = tarefa
            break
    
    if not tarefa_encontrada:
        print("Tarefa não encontrada!")
        aux.pausar()
        return
    
    print(f"\nEditando: {tarefa_encontrada['descricao']}")
    print("\n1. Alterar descrição")
    print("2. Alterar status")
    print("3. Alterar prioridade")
    print("4. Alterar prazo")
    print("5. Reatribuir engenheiro")
    
    opcao = aux.validar_numero("\nEscolha uma opção: ")
    
    if opcao == 1:
        nova_desc = input("Nova descrição: ").strip()
        if nova_desc:
            tarefa_encontrada['descricao'] = nova_desc
    elif opcao == 2:
        print("\nStatus: Pendente / Em Andamento / Concluída")
        novo_status = input("Novo status: ").strip()
        tarefa_encontrada['status'] = novo_status
        
        if novo_status.lower() == 'concluída':
            for eng in dg.engenheiros:
                if eng['id'] == tarefa_encontrada['id_engenheiro']:
                    if tarefa_encontrada['id'] not in eng['tarefas_concluidas']:
                        eng['tarefas_concluidas'].append(tarefa_encontrada['id'])
    elif opcao == 3:
        nova_prior = input("Nova prioridade (Alta/Média/Baixa): ").strip()
        tarefa_encontrada['prioridade'] = nova_prior
    elif opcao == 4:
        novo_prazo = input("Novo prazo (DD/MM/YYYY): ").strip()
        prazo = aux.formatar_data(novo_prazo)
        if prazo:
            tarefa_encontrada['prazo'] = prazo
            tarefa_encontrada['prazo_str'] = novo_prazo
    elif opcao == 5:
        print("\n--- Engenheiros ---")
        for eng in dg.engenheiros:
            print(f"ID: {eng['id']} - {eng['nome']}")
        
        novo_id = aux.validar_numero("Novo ID do engenheiro: ")
        
        for eng in dg.engenheiros:
            if eng['id'] == novo_id:
                for eng_antigo in dg.engenheiros:
                    if eng_antigo['id'] == tarefa_encontrada['id_engenheiro']:
                        if tarefa_encontrada['id'] in eng_antigo['tarefas_atribuidas']:
                            eng_antigo['tarefas_atribuidas'].remove(tarefa_encontrada['id'])
                
                eng['tarefas_atribuidas'].append(tarefa_encontrada['id'])
                tarefa_encontrada['id_engenheiro'] = novo_id
                tarefa_encontrada['nome_engenheiro'] = eng['nome']
                break
    
    print("\n✅ Tarefa atualizada!")
    aux.pausar()

def remover_tarefa():
    
    aux.limpar_tela()
    print("=" * 50)
    print("REMOVER TAREFA")
    print("=" * 50)
    
    if not dg.tarefas:
        print("\n❌ Nenhuma tarefa cadastrada!")
        aux.pausar()
        return
    
    print("\n--- Tarefas ---")
    for tarefa in dg.tarefas:
        print(f"ID: {tarefa['id']} - {tarefa['descricao']}")
    
    id_tarefa = aux.validar_numero("\nID da tarefa a remover: ")
    
    tarefa_encontrada = None
    indice = -1
    for i, tarefa in enumerate(dg.tarefas):
        if tarefa['id'] == id_tarefa:
            tarefa_encontrada = tarefa
            indice = i
            break
    
    if not tarefa_encontrada:
        print("Tarefa não encontrada!")
        aux.pausar()
        return
    
    confirmacao = input(f"\nConfirma remoção de '{tarefa_encontrada['descricao']}'? (s/n): ")
    
    if confirmacao.lower() == 's':
        for eng in dg.engenheiros:
            if eng['id'] == tarefa_encontrada['id_engenheiro']:
                if id_tarefa in eng['tarefas_atribuidas']:
                    eng['tarefas_atribuidas'].remove(id_tarefa)
        
        dg.tarefas.pop(indice)
        print("Tarefa removida!")
    else:
        print("Operação cancelada.")
    
    aux.pausar()