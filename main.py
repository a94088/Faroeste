biblioteca = [
    {"Título": "O Ensaio", "Artista": "Valete", "Género": "Hip-Hop", "Ano": 2006},
    {"Título": "Cafeína", "Artista": "Plutónio", "Género": "Afro", "Ano": 2019},
    {"Título": "Cromossoma", "Artista": "Plutónio", "Género": "Trap", "Ano": 2026},
]

def biblioteca_musicas():
    if not biblioteca:
        print("\nBiblioteca vazia")
        return
    
def biblioteca_musicas():
    print("\n--- BIBLIOTECA FAROESTE ---")
    for m in biblioteca:
        print(m["Título"], "-", m["Artista"], "-", m["Género"], "-", m["Ano"])


def inserir_musica():
    titulo = input("Título: ")
    artista = input("Artista: ")
    genero = input("Género: ")
    ano = input("Ano: ")

    biblioteca.append({
        "Título": titulo,
        "Artista": artista,
        "Género": genero,
        "Ano": ano
    })
    print("Música adicionada!")

def remover_musica():
    if not biblioteca:
        print("\nBiblioteca vazia. Não há músicas para remover.")
        return
    print("\n--- REMOVER MÚSICA ---")
    for i, m in enumerate(biblioteca, start=1):
        print(f"{i}. {m['Título']} - {m['Artista']}")

    escolha = input("Escolhe o número ou o título da música a remover (0 para cancelar): ").strip()
    if escolha == "0":
        print("Remoção cancelada.")
        return

    # Tenta remover pelo número da lista
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(biblioteca):
            removida = biblioteca.pop(indice)
            print(f"Música '{removida['Título']}' removida com sucesso!")
            return
        print("Número inválido!")
        return

    # Caso contrário, tenta remover pelo título (ignorando maiúsculas/minúsculas)
    for i, m in enumerate(biblioteca):
        if m["Título"].lower() == escolha.lower():
            removida = biblioteca.pop(i)
            print(f"Música '{removida['Título']}' removida com sucesso!")
            return

    print("Música não encontrada na biblioteca.")


while True:
    print("\n=== MENU FAROESTE ===")
    print("1 - Ver biblioteca")
    print("2 - Inserir música")
    print("0 - Sair")

    opcao = input("Escolhe uma opção: ")

    if opcao == "1":
        biblioteca_musicas()
    elif opcao == "2":
        inserir_musica()
    elif opcao == "3":
        remover_musica()
    elif opcao == "0":
        print("A sair...")
        break
    else:
        print("Opção inválida!")