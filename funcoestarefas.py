
def adicionarTarefa(tarefas, tarefasDic):
    tarefa = input("\nDigite o nome da tarefa para adicionar: ").lower().strip()
    tarefas.append(tarefa)
    tarefasDic.update({tarefa: "Não Concluída"})
    return print(f"Tarefa '{tarefa}' adicionada a lista de tarefas!")

def removerTarefa(tarefas, tarefasDic):
    tarefa = input("\nDigite o nome da tarefa para remover: ").lower().strip()
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        tarefasDic.pop(tarefa)
        return print(f"Tarefa '{tarefa}' removida da lista de tarefas!")
    else:
        return print(f"Tarefa '{tarefa}' não encontrada!")

def checkTarefa(tarefasDic):
    tarefa = input("\nDigite o nome da tarefa para marcar como conluída: ").lower().strip()
    if tarefa in tarefasDic:
        tarefasDic.update({tarefa: "Concluída"})
        return print(f" '{tarefa}' marcada como concluída!")
    else:
        return print(f"Tarefa '{tarefa}' não encontrada!")
    

def listarConcluidas(tarefasDic, concluidas):
    for tarefa, status in tarefasDic.items():
        if status == "Concluída":
            concluidas.append(tarefa)
    return print(concluidas)

def listarNaoConcluidas(tarefasDic, naoConcluidas):
    for tarefa, status in tarefasDic.items():
        if status == "Não Concluída":
            naoConcluidas.append(tarefa)
    return print(naoConcluidas)