import requests
import json

class Biblioteca:
    def __init__(self, url):
        self.url = url

    def adicionar(self):
        # Dados do livro a ser adicionado
        titulo = input("Título: ")
        editora = input("Editora: ")
        foto = input("Foto (link): ")
        autores = input("Autor(es): ")

        # Estruturando os dados do livro corretamente
        dados_livro = {
            "titulo": titulo,
            "editora": editora,
            "foto": foto,
            "autores": autores.split(",")  # Convertendo para uma lista de autores
        }

        # Fazendo a solicitação POST usando o parâmetro json
        response = requests.post(self.url, json=dados_livro)

        # Exibe a resposta do servidor
        print(response.text)

    def ver(self):
        # Fazendo a solicitação GET para obter dados
        dados = requests.get(self.url)
        

        # Pedindo ao usuário para inserir o ID ou nome do livro
        livro = input("Digite o ID ou nome do livro que deseja ver: ")

        # Verificando se o usuário forneceu um ID ou nome
        if livro:
            # Convertendo a resposta em JSON para um formato Python
            dados_json = dados.json()

            # Procurando o livro pelo ID ou nome
            livro_encontrado = None
            for livro_atual in dados_json:
                if str(livro_atual.get("id")) == livro or livro_atual.get("titulo") == livro:
                    livro_encontrado = livro_atual
                    break

            # Exibindo o livro encontrado ou uma mensagem se não encontrado
            if livro_encontrado:
                print("Detalhes do livro:")
                print(f"ID: {livro_encontrado.get('id')}")
                print(f"Título: {livro_encontrado.get('titulo')}")
                print(f"Editora: {livro_encontrado.get('editora')}")
                print(f"Autores: {', '.join(livro_encontrado.get('autores'))}")
                print(f"Foto: {livro_encontrado.get('foto')}")
            else:
                print("Livro não encontrado.")
        else:
            # Exibindo todos os dados se nenhum ID ou nome for fornecido
            print(dados.text)
        

    def deletar(self):
        # Lógica para deletar um livro
        livro_id = input("ID do livro a ser deletado: ")        
        url_delete = f"{self.url}/{livro_id}"
        response = requests.delete(url_delete)
        print(f"ID do livro a ser deletado {livro_id}")

    def atualizar(self):
        # Lógica para atualizar um livro
        livro_id = input("ID do livro a ser atualizado")

        # Dados a serem atualizados
        novo_titulo = input("Novo titulo: ")
        editora = input("Editora: ")
        foto = input("Foto: ")
        autores = input("Autor(es): ")

        # Estruturando os dados atualizados do livro corretamente
        dados_atualizados = {
            "titulo": novo_titulo,
            "editora": editora,
            "foto": foto,
            "autores": autores.split(",")  # Convertendo para uma lista de autores
        }

        # Fazendo a solicitação PUT usando o parâmetro json
        url_atualizar = f"{self.url}/{livro_id}"
        response = requests.put(url_atualizar, json=dados_atualizados)


# URL da rota de cadastro de obras
url = "https://biblioteca-back-end.danilocs1.repl.co/obras"

# Instanciando a classe Biblioteca
biblioteca = Biblioteca(url)

# Obtendo a opção do usuário
op = input("1 - Adicionar\n2 - Ver\n3 - Deletar\n4 - Atualizar\n: ")

# Executando a opção selecionada
if op == "1":
    biblioteca.adicionar()
elif op == "2":
    biblioteca.ver()
elif op == "3":
    biblioteca.deletar()
elif op == "4":
    biblioteca.atualizar()
