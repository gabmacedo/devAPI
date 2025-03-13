from flask import Flask, jsonify, request

app = Flask(__name__)

#Lista
alunos = [{"id": 1, "nome": "Gabriel"}, {"id": 2, "nome": "Davi"}, {"id": 3, "nome": "Guilherme"}]
professores = [{"id": 1, "nome": "Caio"}, {"id": 2, "nome": "Odair"}, {"id": 3, "nome": "Fabio"}]
turmas = [{"id": 1, "nome": "S.I"}, {"id": 2, "nome": "ADS"}]

#Rota para obter todos os alunos 000
@app.route('/alunos', methods=['GET'])
def obter_alunos():
    return jsonify(alunos)

#Rota para cadastrar um aluno novo / certificar que o ID é unico 001
@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    novo_aluno = request.get_json()
    for aluno in alunos:
        if aluno["id"] == aluno['id']:
            return jsonify({'erro': 'id já utilizada'}), 400
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

#Rota para buscar um aluno por ID 002
@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno), 200
    return jsonify({'erro': "Aluno não encontrado!"}), 404

#Rota para resetar o server 003
@app.route('/reseta', methods=['POST'])
def resetar_servidor():
    global alunos
    alunos = []
    return jsonify({"mensagem": "Servidor resetado!"}), 200

#Rota para deletar alunos especificos pelo ID 004
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    global alunos
    alunos = [aluno for aluno in alunos if aluno["id"] != id]
    return jsonify({"mensagem": "Aluno deletado!"}), 200

#Rota para editar nome do aluno sem alterar o ID
@app.route('/alunos/<int:id>', methods=['PUT'])
def editar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            dados_atualizados = request.get_json()
            aluno["nome"] = dados_atualizados["nome"]
        return jsonify(aluno), 200
    return jsonify({'erro': "Aluno não encontrado!"}), 404


#Rota para obter todos os professores 00
@app.route('/professores', methods=['GET'])
def obter_professores():
    return jsonify(professores)

#Rota para obter todas as turmas 00
@app.route('/turmas', methods=['GET'])
def obter_turmas():
    return jsonify(turmas)


if __name__ == '__main__':
    app.run(debug=True)

