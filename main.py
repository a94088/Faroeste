
from funcoes import biblioteca_musicas, inserir_musica, remover_musica

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