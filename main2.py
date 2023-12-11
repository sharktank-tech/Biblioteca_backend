from flask import Flask, request, jsonify
import os

app = Flask(__name__)

obras = []


# Home
@app.route('/')
def home():
  return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      flex-direction: column;
      justify-content: center;
      height: 100vh;
      margin: 0;
      background: rgb(85,13,173);
      background: radial-gradient(circle, rgba(85,13,173,1) 45%, rgba(156,89,182,1) 100%);
    
        }

        .mensagem {
            font-size: 30px;
            text-align: center;
        }

            a {
            font-size: 20px;
            text-align: center;
            color: #009BFF;
            text-decoration: none;
            }

    </style>
        
    </style>
    <title>Biblioteca Back-End</title>
</head>
<body>
    <div class="mensagem">
        Biblioteca Back-End
    </div>

    <a href="/obras">Obras</a>

</body>
</html>
'''

# [POST] /obras
@app.route('/obras', methods=['POST'])
def cadastrar_obra():
    data = request.json
    nova_obra = {
        'id': len(obras) + 1,
        'titulo': data['titulo'],
        'editora': data['editora'],
        'foto': data['foto'],
        'autores': data['autores']
    }
    obras.append(nova_obra)
    return jsonify(nova_obra), 201

# [GET] /obras
@app.route('/obras', methods=['GET'])
def listar_obras():
    return jsonify(obras)

# [PUT] /obras/<id>
@app.route('/obras/<int:id>', methods=['PUT'])
def atualizar_obra(id):
    data = request.json
    for obra in obras:
        if obra['id'] == id:
            obra['titulo'] = data['titulo']
            obra['editora'] = data['editora']
            obra['foto'] = data['foto']
            obra['autores'] = data['autores']
            return jsonify(obra)
    return 'Obra não encontrada', 404

# [DELETE] /obras/<id>
@app.route('/obras/<int:id>', methods=['DELETE'])
def deletar_obra(id):
    for obra in obras:
        if obra['id'] == id:
            obras.remove(obra)
            return '', 204
    return 'Obra não encontrada', 404

if __name__ == '__main__':
    # Defina a porta como a fornecida pelo ambiente ou use a porta 5000 como padrão
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
