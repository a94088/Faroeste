"""Funções da aplicação Faroeste: gestão da biblioteca musical,
das playlists e gravação dos dados em JSON."""
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
        try:
            with open(FICHEIRO_DADOS, "r", encoding="utf-8") as f:
                dados = json.load(f)
            if isinstance(dados, dict):
                return dados.get("biblioteca", list(biblioteca_padrao)), dados.get("playlists", {})
        except (json.JSONDecodeError, OSError):
            print("Aviso: 'dados.json' vazio ou inválido. A carregar dados padrão.")
    return list(biblioteca_padrao), {}

def guardar_dados():
    """Grava a biblioteca e as playlists no ficheiro dados.json."""
    with open(FICHEIRO_DADOS, "w", encoding="utf-8") as f:
        json.dump(
            {"biblioteca": biblioteca, "playlists": playlists},
            f,
            ensure_ascii=False,
            indent=4,
        )


biblioteca, playlists = carregar_dados()


def biblioteca_musicas():
    """Mostra todas as músicas da biblioteca (título, artista, género e ano)."""
    if not biblioteca:
        print("\nBiblioteca vazia")
        return

    print("\n--- BIBLIOTECA FAROESTE ---")
    for m in biblioteca:
        print(m["Título"], "-", m["Artista"], "-", m["Género"], "-", m["Ano"])


def inserir_musica():
    """Pede título, artista, género e ano e adiciona a música à biblioteca.
Valida campos vazios, o ano (1900-2100) e impede músicas duplicadas
(mesmo título e artista)."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            break
        print("O título não pode estar vazio.")

    while True:
        artista = input("Artista: ").strip()
        if artista:
            break
        print("O artista não pode estar vazio.")

    for m in biblioteca:
        if (
            m.get("Título", "").strip().lower() == titulo.lower()
            and m.get("Artista", "").strip().lower() == artista.lower()
        ):
            print(f"A música '{m['Título']}' de '{m['Artista']}' já existe na biblioteca!")
            return

    while True:
        genero = input("Género: ").strip()
        if genero:
            break
        print("O género não pode estar vazio.")

    while True:
        ano_texto = input("Ano: ").strip()
        try:
            ano = int(ano_texto)
            if 1900 <= ano <= 2100:
                break
            print("Indica um ano entre 1900 e 2100.")
        except ValueError:
            print("O ano tem de ser um número inteiro (ex.: 2026).")

    biblioteca.append({
        "Título": titulo,
        "Artista": artista,
        "Género": genero,
        "Ano": ano,
    })
    guardar_dados()
    print("Música adicionada!")


def remover_musica():
    """Remove da biblioteca a música com o título indicado
(sem distinguir maiúsculas/minúsculas) e guarda as alterações."""
    titulo = input("Título da música a remover: ")

    for m in biblioteca:
        if m["Título"].lower() == titulo.lower():
            biblioteca.remove(m)
            guardar_dados()
            print("Música removida!")
            return

    print("Música não encontrada!")


def pesquisar_musica():
    """Pesquisa músicas cujo título ou artista contenham o texto indicado
(sem distinguir maiúsculas/minúsculas) e mostra os resultados."""
    procura = input("Procurar: ").strip().lower()
    if not procura:
        print("Escreve um título ou artista para pesquisar.")
        return

    encontrou = False
    for m in biblioteca:
        if (
            procura in m.get("Título", "").lower()
            or procura in m.get("Artista", "").lower()
        ):
            print(
                m["Título"], "-", m["Artista"], "-", m["Género"], "-", m["Ano"]
            )
            encontrou = True

    if not encontrou:
        print("Nenhuma música encontrada.")

def criar_playlist():
    """Cria uma playlist e adiciona músicas existentes na biblioteca.
Pede confirmação se o nome já existir, não permite repetir músicas
na mesma playlist e termina quando se escreve '0'."""
    while True:
        nome = input("Nome da playlist: ").strip()
        if nome:
            break
        print("O nome da playlist não pode estar vazio.")

    if nome in playlists:
        resposta = input(f"A playlist '{nome}' já existe. Queres substituí-la? (s/n): ").strip().lower()
        if resposta != "s":
            print("Operação cancelada.")
            return

    playlists[nome] = []

    while True:
        titulo = input("Título da música a adicionar (ou '0' para terminar): ").strip()
        if titulo == "0":
            break
        if not titulo:
            continue

        encontrada = None
        for m in biblioteca:
            if m.get("Título", "").strip().lower() == titulo.lower():
                encontrada = m
                break

        if not encontrada:
            print("Música não encontrada na biblioteca!")
            continue

        ja_na_playlist = any(
            item.get("Título", "").strip().lower() == encontrada.get("Título", "").strip().lower()
            and item.get("Artista", "").strip().lower() == encontrada.get("Artista", "").strip().lower()
            for item in playlists[nome]
        )

        if ja_na_playlist:
            print(f"'{encontrada['Título']}' já está na playlist '{nome}'!")
        else:
            playlists[nome].append(encontrada)
            print(f"'{encontrada['Título']}' adicionada à playlist '{nome}'!")

    guardar_dados()
    print(f"Playlist '{nome}' guardada com sucesso!")


def ver_playlists():
    """Mostra todas as playlists e as músicas de cada uma."""
    if not playlists:
        print("Ainda não existem playlists.")
        return

    for nome, musicas in playlists.items():
        print(f"\n--- Playlist: {nome} ---")
        for m in musicas:
            print(m["Título"], "-", m["Artista"])


def ver_artistas():
    """Mostra cada artista e o número de músicas que tem na biblioteca."""
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
    """Mostra a apresentação do projeto Faroeste."""
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
    """Mostra o total de músicas e playlists, o género mais comum
e as músicas mais antiga e mais recente."""
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