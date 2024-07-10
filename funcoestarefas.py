
def adicionarTarefa(tarefas, tarefasDic):
    tarefa = input("Digite o nome da tarefa para adicionar: ")
    tarefas.append(tarefa)
    tarefasDic.update({tarefa: "Não Concluída"})

def removerTarefa(tarefas, tarefasDic):
    tarefa = input("Digite o nome da tarefa para remover: ")
    tarefas.remove(tarefa)
    tarefasDic.pop(tarefa)

def checkTarefa(tarefasDic):
    tarefa = input("Digite o nome da tarefa para marcar como conluída: ")
    tarefasDic.update({tarefa: "Concluída"})
    print(tarefasDic)

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