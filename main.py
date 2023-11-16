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
        
        # Exibindo os dados recebidos do servidor
        print(dados.json())

    def deletar(self):
        # Lógica para deletar um livro
        livro_id = input("ID do livro a ser deletado: ")        
        url_delete = f"{self.url}/{livro_id}"
        response = requests.delete(url_delete)

    def atualizar(self):
        # Lógica para atualizar um livro
        pass
        # Continuar....

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
