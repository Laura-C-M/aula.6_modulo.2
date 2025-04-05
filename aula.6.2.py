def criar_ficheiro():
    nome_ficheiro = input("Escolhe um nome para o ficheiro (sem extensão): ")
    nome_ficheiro_completo = f"{nome_ficheiro}.txt"
    with open(nome_ficheiro_completo, "w") as ficheiro:
        ficheiro.write("")  # Cria um ficheiro vazio
    print(f"Ficheiro {nome_ficheiro_completo} criado com sucesso!")

def inserir_frase():
    nome_ficheiro = input("Digite o nome do ficheiro (sem extensão): ")
    nome_ficheiro_completo = f"{nome_ficheiro}.txt"
    frase = input("Digite a frase que deseja inserir: ")
    with open(nome_ficheiro_completo, "a") as ficheiro:
        ficheiro.write(frase + "\n")
    print(f"Frase inserida no ficheiro {nome_ficheiro_completo} com sucesso!")

def menu():
    while True:
        print("\nMenu:")
        print("1. Criar Ficheiro")
        print("2. Inserir Frase")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_ficheiro()
        elif escolha == "2":
            inserir_frase()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()