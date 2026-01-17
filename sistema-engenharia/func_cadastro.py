

from datetime import datetime
import func_auxiliares as aux
import dados as dg

def cadastrar_engenheiro():
    
    aux.limpar_tela()
    print("=" * 50)
    print("CADASTRO DE ENGENHEIRO")
    print("=" * 50)
    
    nome = input("\nNome completo: ").strip()
    if not nome:
        print(" Nome não pode ser vazio!")
        aux.pausar()
        return
    
    especialidade = input("Especialidade: ").strip()
    crea = input("Número do CREA: ").strip()
    
    engenheiro = {
        'id': aux.gerar_id(dg.engenheiros),
        'nome': nome,
        'especialidade': especialidade,
        'crea': crea,
        'tarefas_atribuidas': [],
        'tarefas_concluidas': [],
        'data_cadastro': datetime.now().strftime("%d/%m/%Y")
    }
    
    dg.engenheiros.append(engenheiro) #os dois aquiii
    dg.notificacoes.append(f"Novo engenheiro cadastrado: {nome}") 
    
    print(f"\nEngenheiro cadastrado com sucesso! ID: {engenheiro['id']}")
    aux.pausar()

def cadastrar_tarefa(tipo_usuario='gestor'):
    
    if tipo_usuario != 'gestor':
        print("Acesso negado")
        return False

    aux.limpar_tela()
    print("=" * 50)
    print("CADASTRO DE TAREFA")
    print("=" * 50)
    
    if not dg.engenheiros:
        print("\nNenhum engenheiro cadastrado! Cadastre engenheiros primeiro.")
        aux.pausar()
        return
    
    descricao = input("\nDescrição da tarefa: ").strip()
    if not descricao:
        print("Descrição não pode ser vazia!")
        aux.pausar()
        return
    
    projeto = input("Nome do projeto: ").strip()
    prioridade = input("Prioridade (Alta/Média/Baixa): ").strip()
    
    print("\nData de prazo (DD/MM/YYYY):")
    prazo_str = input("Prazo: ").strip()
    prazo = aux.formatar_data(prazo_str)
    
    if not prazo:
        print("Data inválida!")
        aux.pausar()
        return
    
    print("\n--- Engenheiros Disponíveis ---")
    for eng in dg.engenheiros:
        print(f"ID: {eng['id']} - {eng['nome']} ({eng['especialidade']})")
    
    id_engenheiro = aux.validar_numero("\nID do engenheiro responsável: ")
    
    engenheiro_encontrado = None
    for eng in dg.engenheiros:
        if eng['id'] == id_engenheiro:
            engenheiro_encontrado = eng
            break
    
    if not engenheiro_encontrado:
        print("Engenheiro não encontrado!")
        aux.pausar()
        return
    
    tarefa = {
        'id': aux.gerar_id(dg.tarefas),
        'descricao': descricao,
        'projeto': projeto,
        'prioridade': prioridade,
        'prazo': prazo,
        'prazo_str': prazo_str,
        'status': 'Pendente',
        'id_engenheiro': id_engenheiro,
        'nome_engenheiro': engenheiro_encontrado['nome'],
        'data_criacao': datetime.now().strftime("%d/%m/%Y")
    }
    
    dg.tarefas.append(tarefa)
    engenheiro_encontrado['tarefas_atribuidas'].append(tarefa['id'])
    dg.notificacoes.append(f"Nova tarefa criada: '{descricao}' - Responsável: {engenheiro_encontrado['nome']}")
    
    print(f"\nTarefa cadastrada com sucesso! ID: {tarefa['id']}")
    aux.pausar()

def cadastrar_material():
    
    aux.limpar_tela()
    print("=" * 50)
    print("CADASTRO DE MATERIAL")
    print("=" * 50)
    
    nome = input("\nNome do material: ").strip().lower()
    if not nome:
        print("Nome não pode ser vazio!")
        aux.pausar()
        return
    
    if nome in dg.materiais:
        print(f"\nMaterial '{nome}' já existe!")
        print(f"Estoque atual: {dg.materiais[nome]['estoque']} unidades")
        print(f"Preço atual: R$ {dg.materiais[nome]['preco']:.2f}")
        
        opcao = input("\nDeseja atualizar? (s/n): ").lower()
        if opcao != 's':
            return
    
    preco = aux.validar_numero("Preço unitário (R$): ", 'float')
    estoque = aux.validar_numero("Quantidade em estoque: ")
    unidade = input("Unidade de medida (kg, m³, un, etc): ").strip()
    estoque_minimo = aux.validar_numero("Estoque mínimo (alerta): ")
    
    dg.materiais[nome] = {
        'preco': preco,
        'estoque': estoque,
        'unidade': unidade,
        'estoque_minimo': estoque_minimo
    }
    
    print(f"\nMaterial '{nome}' cadastrado/atualizado com sucesso!")
    aux.pausar()

def cadastrar_coordenadas():
    """Cadastra coordenadas fixas da planta"""
    aux.limpar_tela()
    print("=" * 50)
    print("CADASTRO DE COORDENADAS DA PLANTA")
    print("=" * 50)
    
    qtd = aux.validar_numero("\nQuantos pontos deseja cadastrar? ")
    
    coords_temp = []
    for i in range(qtd):
        print(f"\n--- Ponto {i + 1} ---")
        x = aux.validar_numero(f"Coordenada X: ", 'float')
        y = aux.validar_numero(f"Coordenada Y: ", 'float')
        descricao = input(f"Descrição do ponto: ").strip()
        coords_temp.append((x, y, descricao))
    
    dg.coordenadas_planta = tuple(coords_temp) 
    print(f"\n{len(dg.coordenadas_planta)} coordenadas cadastradas!")
    aux.pausar()

def criar_planta_matriz():
    
    aux.limpar_tela()
    print("=" * 50)
    print("CRIAR LAYOUT DA PLANTA (MATRIZ)")
    print("=" * 50)
    
    linhas = aux.validar_numero("\nNúmero de linhas (altura): ")
    colunas = aux.validar_numero("Número de colunas (largura): ")
    
    dg.planta_obra = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        dg.planta_obra.append(linha)
    
    print(f"\nPlanta {linhas}x{colunas} criada!")
    
    if dg.coordenadas_planta:
        print("\nDeseja marcar as coordenadas cadastradas? (s/n): ", end='')
        if input().lower() == 's':
            for coord in dg.coordenadas_planta:
                x, y = coord
                x_int = int(x)
                y_int = int(y)
                
                if 0 <= y_int < linhas and 0 <= x_int < colunas:
                    dg.planta_obra[y_int][x_int] = 'X'
    
    aux.pausar()

def registrar_consumo_semanal():
    
    import notificacoes
    
    aux.limpar_tela()
    print("=" * 50)
    print("REGISTRO DE CONSUMO SEMANAL")
    print("=" * 50)
    
    if not dg.materiais:
        print("\nNenhum material cadastrado!")
        aux.pausar()
        return
    
    semanas = aux.validar_numero("\nNúmero de semanas a registrar: ")
    lista_materiais = list(dg.materiais.keys())
    
    print("\n--- Materiais disponíveis ---")
    for i, mat in enumerate(lista_materiais):
        print(f"{i + 1}. {mat}")
    
    dg.consumo_semanal = []
    
    for semana in range(semanas):
        print(f"\n--- Semana {semana + 1} ---")
        consumo_semana = []
        
        for material in lista_materiais:
            consumo = aux.validar_numero(f"Consumo de {material} ({dg.materiais[material]['unidade']}): ", 'float')
            consumo_semana.append(consumo)
            dg.materiais[material]['estoque'] -= consumo
        
        dg.consumo_semanal.append(consumo_semana)
    
    print("\nConsumo semanal registrado!")
    notificacoes.verificar_estoque_baixo()
    aux.pausar()