# Faroeste

Aplicação de linha de comandos em Python para gerir uma biblioteca musical(atualmente) e apoiar artistas emergentes.

## Funcionalidades

- **Ver biblioteca** (`1`): lista todas as músicas disponíveis com título, artista, género e ano.
- **Inserir música** (`2`): adiciona uma música nova à biblioteca.
- **Remover música** (`3`): remove uma música pesquisada pelo título (sem distinguir maiúsculas/minúsculas).
- **Pesquisar música** (`4`): procura músicas por título ou artista.
- **Criar playlist** (`5`): cria uma playlist e adiciona músicas à biblioteca.
- **Ver playlists** (`6`): apresenta todas as playlists criadas e as respetivas músicas.
- **Ver artistas** (`7`): apresenta todos os artistas com a respetiva quantidade de músicas presentes na biblioteca.

## Estrutura do projeto

```text
Faroeste/
├── main.py      # Menu principal e controlo de fluxo
└── funcoes.py   # Dados em memória (biblioteca e playlists) e lógica das opções