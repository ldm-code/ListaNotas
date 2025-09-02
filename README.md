# ListaNotas

- Uma aplicação desenvolvida para praticar o uso do SQLAlchemy em aplicacoes com o Flask, visando a interação com bancos de dados relacionais (MySql),e a exibição de notas de alunos.
---

## Tecnologias Utilizadas:

- Python
- Flask
- SQLAlchemy
- HTML
- MySQL:
---
## Funcionalidades:

- Cadastro de alunos com suas respectivas notas.
- rankeamento de alunos por nota.
- Listagem de alunos e suas notas.
- Integração com banco de dados MySQL utilizando SQLAlchemy.
- Interface simples construída com HTML e Flask.
---
## Aviso de Segurança:

- Por questões de segurança, a senha do banco de dados presente neste repositório não é a minha senha real. Ela foi configurada de forma genérica para fins de demonstração e aprendizado.  ao utilizar este projeto, você altera a senha(a variavel 'SUA_SENHA_DO_BANCO') pelo valor correspondente ao seu ambiente de desenvolvimento, garantindo a segurança de suas credenciais.
- Alem disso,e necessario que voce tenha um banco com o nome alunos e que tenha criado uma conexao ao banco em sua IDE.
---
## Estrutura do Projeto:

- ListaNotas/
- ├── manage.py
- ├── templates/
- │   ├── inicio.html
- │   └── notas.html
- └── README.md


- manage.py: Script principal para execução da aplicação.

- templates/: Diretório contendo os arquivos HTML para renderização das páginas.

- inicio.html: Página inicial para cadastro de alunos e notas.

- notas.html: Página para exibição da lista de alunos e suas notas.
