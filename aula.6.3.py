def criar_ficheiro():
    nome_ficheiro = input("Escolhe um nome para o ficheiro (sem extensão): ")
    with open(f"{nome_ficheiro}.txt", "w") as ficheiro:
        pass  # Cria um ficheiro vazio
    print(f"Ficheiro {nome_ficheiro}.txt criado com sucesso!")


def ler_ficheiro():
    nome_ficheiro = input("Digite o nome do ficheiro (sem extensão): ")
    with open(f"{nome_ficheiro}.txt", "r") as ficheiro:
        conteudo = ficheiro.read()
        print("Conteúdo do ficheiro:")
        print(conteudo)

def menu():
    while True:
        print("\nMenu:")
        print("1. Criar Ficheiro")
        print("2. Ler Ficheiro")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_ficheiro()
        elif escolha == "2":
            ler_ficheiro()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()