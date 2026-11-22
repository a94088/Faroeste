from funcoes import (
    biblioteca_musicas,
    inserir_musica,
    remover_musica,
    pesquisar_musica,
    criar_playlist,
    ver_playlists,
    ver_artistas,
)

while True:
    print("\n=== MENU FAROESTE ===")
    print("1 - Ver biblioteca")
    print("2 - Inserir música")
    print("3 - Remover música")
    print("4 - Pesquisar música")
    print("5 - Criar playlist")
    print("6 - Ver playlists")
    print("7 - Ver artistas")
    print("0 - Sair")

    opcao = input("Escolhe uma opção: ")

    if opcao == "1":
        biblioteca_musicas()
    elif opcao == "2":
        inserir_musica()
    elif opcao == "3":
        remover_musica()
    elif opcao == "4":
        pesquisar_musica()
    elif opcao == "5":
        criar_playlist()
    elif opcao == "6":
        ver_playlists()
    elif opcao == "7":
        ver_artistas()
    elif opcao == "0":
        print("A sair...")
        break
    else:
        print("Opção inválida!")

    if opcao != "0":
        input("\nCarrega ENTER para voltar ao menu...")