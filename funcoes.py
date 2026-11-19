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
    titulo = input("Título da música a remover: ")

    for m in biblioteca:
        if m["Título"].lower() == titulo.lower():
            biblioteca.remove(m)
            print("Música removida!")
            return

    print("Música não encontrada!")