import json
import os

FICHEIRO_DADOS = "dados.json"

biblioteca_padrao = [
    {"Título": "O Ensaio", "Artista": "Valete", "Género": "Hip-Hop", "Ano": 2006},
    {"Título": "Cafeína", "Artista": "Plutónio", "Género": "Afro", "Ano": 2019},
    {"Título": "Cromossoma", "Artista": "Plutónio", "Género": "Trap", "Ano": 2026},
]


def carregar_dados():
    if os.path.exists(FICHEIRO_DADOS):
        with open(FICHEIRO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return dados.get("biblioteca", []), dados.get("playlists", {})
    return list(biblioteca_padrao), {}


def guardar_dados():
    with open(FICHEIRO_DADOS, "w", encoding="utf-8") as f:
        json.dump(
            {"biblioteca": biblioteca, "playlists": playlists},
            f,
            ensure_ascii=False,
            indent=4,
        )


biblioteca, playlists = carregar_dados()


def biblioteca_musicas():
    if not biblioteca:
        print("\nBiblioteca vazia")
        return

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
        "Ano": ano,
    })
    guardar_dados()
    print("Música adicionada!")


def remover_musica():
    titulo = input("Título da música a remover: ")

    for m in biblioteca:
        if m["Título"].lower() == titulo.lower():
            biblioteca.remove(m)
            guardar_dados()
            print("Música removida!")
            return

    print("Música não encontrada!")


def pesquisar_musica():
    procura = input("Procurar: ").lower()

    for m in biblioteca:
        if procura in m["Título"].lower() or procura in m["Artista"].lower():
            print(m["Título"], "-", m["Artista"], "-", m["Género"], "-", m["Ano"])


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

    guardar_dados()


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

def sobre_nos():
    print("\n=== SOBRE NÓS - FAROESTE ===")
    print(
        "A Faroeste é uma biblioteca de músicas pensada para organizar "
        "faixas, descobrir artistas e criar playlists."
    )
    print(
        "Acreditamos numa comunidade aberta: qualquer pessoa pode entrar e "
        "adicionar as suas músicas a qualquer momento."
    )

def estatisticas_biblioteca():
    if not biblioteca:
        print("\nBiblioteca vazia.")
        return

    generos = {}
    for m in biblioteca:
        g = m.get("Género", "").strip()
        if g:
            generos[g] = generos.get(g, 0) + 1

    if generos:
        genero_top = max(generos, key=generos.get)
        genero_info = f"{genero_top} ({generos[genero_top]})"
    else:
        genero_info = "Sem género"

    com_ano = []
    for m in biblioteca:
        try:
            com_ano.append((int(m["Ano"]), m))
        except (KeyError, TypeError, ValueError):
            pass

    print("\n=== ESTATÍSTICAS - FAROESTE ===")
    print(f"- Total de músicas: {len(biblioteca)}")
    print(f"- Total de playlists: {len(playlists)}")
    print(f"- Género mais comum: {genero_info}")

    if com_ano:
        antiga = min(com_ano, key=lambda x: x[0])[1]
        recente = max(com_ano, key=lambda x: x[0])[1]
        print(f"- Música mais antiga: {antiga['Título']} - {antiga['Artista']} ({antiga['Ano']})")
        print(f"- Música mais recente: {recente['Título']} - {recente['Artista']} ({recente['Ano']})")