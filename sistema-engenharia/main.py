
import func_auxiliares as aux
import func_cadastro as cadastros 
import func_tarefas as tarefas
import relatorio as relatorios
import busca 
import calculos
import notificacoes

def menu_engenheiro():
    
    while True:
        aux.limpar_tela()
        print("=" * 50)
        print("==Menu Engenheiro==")
        print("=" * 50)
        print("\n1. Visualizar minhas tarefas")
        print("2. Visualizar coordenadas da planta")
        print("3. Visualizar layout da planta")
        print("4. Visualizar materiais")
        print("5. Buscar projeto/tarefa")
        print("6. Ver notificações")
        print("0. Voltar ao menu principal")
        
        opcao = aux.validar_numero("\nEscolha uma opção: ")
        
        if opcao == 1:
            tarefas.visualizar_tarefas_engenheiro()
        elif opcao == 2:
            tarefas.visualizar_coordenadas()
        elif opcao == 3:
            tarefas.visualizar_planta()
        elif opcao == 4:
            tarefas.visualizar_materiais()
        elif opcao == 5:
            busca.buscar_projeto()
        elif opcao == 6:
            notificacoes.verificar_tarefas_proximas()
            notificacoes.visualizar_notificacoes()
        elif opcao == 0:
            break

def menu_gestor():
    while True:
        aux.limpar_tela()
        print("=" * 50)
        print("==Menu Gestor==")
        print("=" * 50)
        print("\n=== CADASTROS ===")
        print("1. Cadastrar engenheiro")
        print("2. Atribuir tarefa")
        print("3. Cadastrar material")
        print("4. Cadastrar coordenadas da planta")
        print("5. Criar layout da planta (matriz)")
        
        print("\n=== GESTÃO ===")
        print("6. Editar tarefa")
        print("7. Remover tarefa")
        print("8. Registrar consumo semanal")
        
        print("\n=== CONSULTAS ===")
        print("9. Visualizar todas as tarefas")
        print("10. Visualizar materiais")
        print("11. Visualizar coordenadas")
        print("12. Visualizar planta")
        print("13. Buscar projeto/tarefa")
        
        print("\n=== RELATÓRIOS ===")
        print("14. Relatório de consumo por semana")
        print("15. Relatório de consumo por material")
        print("16. Relatório geral do projeto")
        print("17. Calcular custo total")
        print("18. Divisão de recursos")
        
        print("\n=== NOTIFICAÇÕES ===")
        print("19. Ver notificações")
        print("20. Limpar notificações")
        
        print("\n0. Voltar ao menu principal")
        
        opcao = aux.validar_numero("\nEscolha uma opção: ")
        
        if opcao == 1:
            cadastros.cadastrar_engenheiro()
        elif opcao == 2:
            cadastros.cadastrar_tarefa()
        elif opcao == 3:
            cadastros.cadastrar_material()
        elif opcao == 4:
            cadastros.cadastrar_coordenadas()
        elif opcao == 5:
            cadastros.criar_planta_matriz()
        elif opcao == 6:
            tarefas.editar_tarefa()
        elif opcao == 7:
            tarefas.remover_tarefa()
        elif opcao == 8:
            cadastros.registrar_consumo_semanal()
        elif opcao == 9:
            tarefas.visualizar_todas_tarefas()
        elif opcao == 10:
            tarefas.visualizar_materiais()
        elif opcao == 11:
            tarefas.visualizar_coordenadas()
        elif opcao == 12:
            tarefas.visualizar_planta()
        elif opcao == 13:
            busca.buscar_projeto()
        elif opcao == 14:
            relatorios.relatorio_consumo_por_semana()
        elif opcao == 15:
            relatorios.relatorio_consumo_por_material()
        elif opcao == 16:
            relatorios.relatorio_geral_projeto()
        elif opcao == 17:
            calculos.exibir_custo_total()
        elif opcao == 18:
            calculos.calcular_divisao_recursos()
        elif opcao == 19:
            notificacoes.verificar_tarefas_proximas()
            notificacoes.verificar_estoque_baixo()
            notificacoes.visualizar_notificacoes()
        elif opcao == 20:
            notificacoes.limpar_notificacoes()
        elif opcao == 0:
            break

def menu_principal():
    """Menu principal do sistema"""
    while True:
        aux.limpar_tela()
        print("=" * 50)
        print("SISTEMA DE GESTÃO DE PROJETOS DE ENGENHARIA")
        print("=" * 50)
        print("\n1. Acessar como Engenheiro")
        print("2. Acessar como Gestor")
        print("0. Sair do sistema")
        
        opcao = aux.validar_numero("\nEscolha uma opção: ")
        
        if opcao == 1:
            menu_engenheiro()
        elif opcao == 2:
            menu_gestor()
        elif opcao == 0:
            aux.limpar_tela()
            print("\nObrigado por usar o Sistema de Gestão de Projetos!")
            print("Até logo!\n")
            break

if __name__ == "__main__":
    menu_principal()