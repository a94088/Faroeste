# Faroeste

Aplicação de comandos em Python para gerir uma biblioteca musical (atualmente) e apoiar artistas emergentes.

## Funcionalidades

- **Ver biblioteca** (`1`): lista todas as músicas disponíveis com título, artista, género e ano.
- **Inserir música** (`2`): adiciona uma nova música à biblioteca.
- **Remover música** (`3`): remove uma música pesquisada pelo título (sem distinguir maiúsculas/minúsculas).
- **Pesquisar música** (`4`): procura músicas por título ou artista.
- **Criar playlist** (`5`): cria uma playlist e adiciona músicas existentes da biblioteca.
- **Ver playlists** (`6`): apresenta todas as playlists criadas e as respetivas músicas.
- **Ver artistas** (`7`): apresenta todos os artistas com a respetiva quantidade de músicas presentes na biblioteca.
- **Sobre nós** (`8`): informação sobre o projeto.
- **Estatísticas** (`9`): apresenta o total de músicas e playlists, o género mais comum e as músicas mais antiga e mais recente.

## Estrutura do projeto

```text
Faroeste/
├── main.py      # Menu principal 
├── funcoes.py   # Lógica das opções e leitura/escrita em JSON
└── dados.json   # Ficheiro gerado automaticamente para guardar a biblioteca e as playlists