
from datetime import datetime
import func_auxiliares as aux
import dados as dg

def verificar_estoque_baixo():
    
    alertas = []
    
    for nome, dados in dg.materiais.items(): #dicionarios
        if dados['estoque'] <= dados['estoque_minimo']:
            alerta = f"ALERTA: {nome.upper()} está com estoque baixo! (Atual: {dados['estoque']:.2f} {dados['unidade']})"
            alertas.append(alerta)
            
            if alerta not in dg.notificacoes:
                dg.notificacoes.append(alerta)
    
    if alertas:
        print("\n" + "=" * 50)
        print("ALERTAS DE ESTOQUE")
        print("=" * 50)
        for alerta in alertas:
            print(alerta)
        print("=" * 50)

def verificar_tarefas_proximas():
    
    tarefas_proximas = []
    data_atual = datetime.now()
    
    for tarefa in dg.tarefas:
        if tarefa['status'].lower() != 'concluída':
            dias_restantes = (tarefa['prazo'] - data_atual).days
            
            if 0 <= dias_restantes <= 7:
                tarefas_proximas.append(tarefa)
                
                msg = f"⏰ Tarefa '{tarefa['descricao']}' vence em {dias_restantes} dia(s)!"
                if msg not in dg.notificacoes:
                    dg.notificacoes.append(msg)
    
    return tarefas_proximas

def visualizar_notificacoes():
    
    aux.limpar_tela()
    print("=" * 50)
    print("NOTIFICAÇÕES")
    print("=" * 50)
    
    if not dg.notificacoes:
        print("\nNenhuma notificação no momento.")
    else:
        print()
        for i, notif in enumerate(dg.notificacoes):
            print(f"{i + 1}. {notif}")
    
    aux.pausar()

def limpar_notificacoes():

    confirmacao = input("\nConfirma limpeza de todas as notificações? (s/n): ")
    if confirmacao.lower() == 's':
        dg.notificacoes.clear()
        print("Notificações limpas!")
    else:
        print("Operação cancelada.")
    
    aux.pausar()