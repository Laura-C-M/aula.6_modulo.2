# Abrindo um arquivo em modo de leitura e escrita
with open('lusiadas.txt', 'r+') as arquivo:
    # Movendo o cursor para a posição 10
    arquivo.seek(10)

    # Lendo a partir da posição 10
    conteudo = arquivo.read(20)
    print(conteudo)

    # Movendo o cursor de volta para o início do arquivo
    arquivo.seek(0)

    arquivo.write('Novo conteúdo')
# Abrir um arquivo em modo de leitura
with open('lusiadas.txt', 'r') as arquivo:
    # Ler os primeiros 10 caracteres
    conteudo = arquivo.read(10)
    # Obter a posição atual do cursor
    posicao = arquivo.tell()
    print(f'Posição atual do cursor: {posicao}')
