nome_ficheiro = input("Escolhe um nome para um ficheiro (sem extensão): ")

ficheiro = open(f"{nome_ficheiro}.txt", "w")
print(f"Ficheiro {nome_ficheiro}.txt criado e aberto com sucesso!")

ficheiro.close()