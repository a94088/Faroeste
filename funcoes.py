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
    
def pesquisar_musica():
    procura = input("Procurar: ").lower()

    for m in biblioteca:
        if procura in m["Título"].lower() or procura in m["Artista"].lower():
            print(m["Título"], "-", m["Artista"], "-", m["Género"], "-", m["Ano"])

    
    
playlists = {}

def criar_playlist():
    nome = input("Nome da playlist: ")
    playlists[nome] = []

    while True:
        titulo = input("Título da música a adicionar (ou '0' para terminar): ")
        if titulo == "0":
            break

        encontrada = False
        for m in biblioteca:
            if m["Título"].lower() == titulo.lower():
                playlists[nome].append(m)
                print(f"'{m['Título']}' adicionada à playlist '{nome}'!")
                encontrada = True
                break

        if not encontrada:
            print("Música não encontrada na biblioteca!")

def ver_playlists():
    if not playlists:
        print("Ainda não existem playlists.")
        return

    for nome, musicas in playlists.items():
        print(f"\n--- Playlist: {nome} ---")
        for m in musicas:
            print(m["Título"], "-", m["Artista"])

def ver_artistas():
    if not biblioteca:
        print("\nAinda não existem artistas na biblioteca.")
        return

    contagem = {}
    for m in biblioteca:
        artista = m["Artista"]
        contagem[artista] = contagem.get(artista, 0) + 1

    print("\n--- ARTISTAS NA FAROESTE ---")
    for artista, total in contagem.items():
        print(f"- {artista} ({total} música{'s' if total > 1 else ''})")