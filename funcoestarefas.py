
def adicionarTarefa(tarefas, tarefasDic):
    tarefa = input("\nDigite o nome da tarefa para adicionar: ").lower().strip() # Lê a tarefa, transformando em minúsuculas e removendo os espaços iniciais e finais
    if tarefa in tarefas: # Verifica se a tarefa já existe
        print("\nEsta tarefa já existe!.")
    else:
        tarefas.append(tarefa) # Armazena a tarefa lida a lista 'tarefas' que será um dos pârametros usado na hora da chamada da função
        tarefasDic.update({tarefa: "Não Concluída"}) # Armazena a tarefa lida no dicionário 'tarefasDic' já com o valor de 'Não Concluída'
        return print(f"Tarefa '{tarefa}' adicionada a lista de tarefas!") # Retorno confirmando a inclusão da tarefa

def removerTarefa(tarefas, tarefasDic):
    tarefa = input("\nDigite o nome da tarefa para remover: ").lower().strip() # Lê a tarefa, transformando em minúsuculas e removendo os espaços iniciais e finais
    if tarefa in tarefas: # Caso encontre a tarefa lida na lista de tarefas:
        tarefas.remove(tarefa) # Remove tal tarefa da lista 'tarefas'
        tarefasDic.pop(tarefa) # Remove tal tarefa do dicionário 'tarefasDic'
        return print(f"Tarefa '{tarefa}' removida da lista de tarefas!") # Retorno confirmando a exclusão da tarefa
    else: # Caso não encontre a tarefa lida na lista de tarefas:
        return print(f"Tarefa '{tarefa}' não encontrada!") # Retorno confirmando que a tarefa não foi encontrada

def checkTarefa(tarefasDic):
    tarefa = input("\nDigite o nome da tarefa para marcar como conluída: ").lower().strip() # Lê a tarefa a ser buscada, transformando em minúsuculas e removendo os espaços iniciais e finais
    if tarefa in tarefasDic: # Caso encontre a tarefa:
        tarefasDic.update({tarefa: "Concluída"}) # Marque-a como concluída
        return print(f" '{tarefa}' marcada como concluída!") # Retorno confirmando que a tarefa foi concluída
    else: # Caso não encontre a tarefa:
        return print(f"Tarefa '{tarefa}' não encontrada!") # Retorno confirmando que a tarefa não foi confirmada
    

def listarConcluidas(tarefasDic): 
    concluidas = [] # Inicia uma lista vazia para armazenar as tarefas que forem concluídas
    for tarefa, status in tarefasDic.items(): # Para cada tarefa e status  no dicionário 'tarefasDic':
        if status == "Concluída": # Verifica se o status de tal tarefa está como 'Concluída'
            concluidas.append(tarefa) # Caso sim, adiciona a tarefa a lista de tarefas concluídas
    print('------Tarefas Concluídas------')
    for tarefa in concluidas:
        print(tarefa) # Imprime cada tarefa da lista 'concluidas'
    print('------------------------------')

def listarNaoConcluidas(tarefasDic):
    naoConcluidas = [] # Inicia uma lista vazia para armazenar as tarefas que não foram concluídas
    for tarefa, status in tarefasDic.items(): # Para cada tarefa e status no dicionário 'tarefasDic':
        if status == "Não Concluída": # Verifica se o status de tal tarefa está como 'Não Concluída'
            naoConcluidas.append(tarefa) # Caso sim, adiciona a tarefa a lista de tarefas não concluídas
    print('------Tarefas Não Concluídas------')
    for tarefa in naoConcluidas:
        print(tarefa) # Imprime cada tarefa da lista 'naoConcluidas'
    print('------------------------------')