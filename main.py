import pymysql
from flask import Flask, jsonify, request

app = Flask (__name__) 

## Estabelecendo a conexão com o banco de dados MySQL

db_host = 'localhost'
db_user = 'root'
db_password = '32441503'
db_nome = 'facul'

def connecta_db():
    db = pymysql.connect(host = db_host, user = db_user, password = db_password, db = db_nome)
    return db

## CREATE 
#  Cadastro dos Alunos:

@app.route('/novoAluno', methods=['POST'])
def novoAluno():
    dadosRecebidos = request.get_json()
    nome = dadosRecebidos['nome']
    email = dadosRecebidos['email']
    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"INSERT INTO alunos (nome, email) VALUES ('{nome}', '{email}')"
    cursor.execute(sql)
    banco.commit()
    banco.close()
    
    response = {
        'status': "success",
        'message': "Aluno cadastrado com sucesso!", "codigo": 200
    }
    return jsonify(response)

# Cadastro dos Cursos:

@app.route('/novoCurso', methods=['POST'])
def novoCurso():
    dadosRecebidos = request.get_json()
    titulo = dadosRecebidos['titulo']
    descricao = dadosRecebidos['descricao']
    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"INSERT INTO cursos (titulo, descricao) VALUES ('{titulo}', '{descricao}')"
    cursor.execute(sql)
    banco.commit()
    banco.close()
    
    response = {
        'status': "success",
        'message': "Curso cadastrado com sucesso!", "codigo": 200
    }
    return jsonify(response)




## READ 
# - Listagem dos Alunos:

@app.route('/lerAluno', methods=['GET'])
def lerAluno():
    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"SELECT * FROM alunos"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    banco.close()

    listagemAlunos = []

    for aluno in resultado:
        listagemAlunos.append(
            {
                'idAluno': aluno[0],
                'nome': aluno[1],
                'email': aluno[2]
            }
        )

    return jsonify(listagemAlunos)

#  Listagem dos Cursos:

@app.route('/lerCurso', methods=['GET'])
def lerCurso():
    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"SELECT * FROM cursos"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    banco.close()

    listagemCursos = []

    for curso in resultado:
        listagemCursos.append(
            {
                'idCurso': curso[0],
                'titulo': curso[1],
                'descricao': curso[2]
            }
        )

    return jsonify(listagemCursos)

## Ver detalhes do Aluno especifico:

@app.route('/detalhesAluno/<int:id>', methods=['GET'])
def detalhesAluno(id):
    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"SELECT * FROM alunos WHERE idAluno = {id}"
    cursor.execute(sql)
    resultado = cursor.fetchone()
    banco.close()

    if resultado:
        aluno = {
            'idAluno': resultado[0],
            'nome': resultado[1],
            'email': resultado[2]
        }
        return jsonify(aluno)
    else:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    
## Ver detalhes do Curso especifico:

@app.route('/detalhesCurso/<int:id>', methods=['GET'])
def detalhesCurso(id):
    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"SELECT * FROM cursos WHERE idCurso = {id}"
    cursor.execute(sql)
    resultado = cursor.fetchone()
    banco.close()

    if resultado:
        aluno = {
            'idCurso': resultado[0],
            'titulo': resultado[1],
            'descricao': resultado[2]
        }
        return jsonify(aluno)
    else:
        return jsonify({'message': 'Curso não encontrado'}), 404

    
## UPDATE 
# Atualizar dados do Aluno:

@app.route('/atualizarAluno/', methods=['PUT'])
def atualizarAluno():
    dadosRecebidos = request.get_json()
    idAluno = dadosRecebidos['idAluno']
    novo_nome = dadosRecebidos['nome']
    novo_email = dadosRecebidos['email']

    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"UPDATE alunos SET nome = '{novo_nome}', email = '{novo_email}' WHERE idAluno = {idAluno}"
    cursor.execute(sql)
    banco.commit()
    banco.close()

    response = {
        'status': "success",
        'message': "Aluno atualizado com sucesso!", "codigo": 200
    }
    return jsonify(response)

# Atualizar dados do Curso:

@app.route('/atualizarCurso/', methods=['PUT'])
def atualizarCurso():
    dadosRecebidos = request.get_json()
    idCurso = dadosRecebidos['idCurso']
    novo_titulo = dadosRecebidos['titulo']
    nova_descricao = dadosRecebidos['descricao']

    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"UPDATE cursos SET titulo = '{novo_titulo}', descricao = '{nova_descricao}' WHERE idCurso = {idCurso}"
    cursor.execute(sql)
    banco.commit()
    banco.close()

    response = {
        'status': "success",
        'message': "Curso atualizado com sucesso!", "codigo": 200
    }
    return jsonify(response)

## DELETE 
# Deletar Aluno:

@app.route('/removerAluno/', methods=['DELETE'])
def removerAluno():
    dadosRecebidos = request.get_json()
    idAluno = dadosRecebidos['idAluno']

    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"DELETE FROM alunos WHERE idAluno = {idAluno};"
    resultado = cursor.execute(sql)
    banco.commit()
    banco.close()

    if resultado:
        response = {
            'status': "success",
            'message': "Aluno removido com sucesso!", "codigo": 200
        }
    else:
        response = {
            'status': "error",
            'message': "Aluno não encontrado!", "codigo": 404
        }
    return jsonify(response)

# Deletar Curso:

@app.route('/removerCurso/', methods=['DELETE'])
def removerCurso():
    dadosRecebidos = request.get_json()
    idCurso = dadosRecebidos['idCurso']

    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"DELETE FROM cursos WHERE idCurso = {idCurso};"
    resultado = cursor.execute(sql)
    banco.commit()
    banco.close()

    if resultado:
        response = {
            'status': "success",
            'message': "Curso removido com sucesso!", "codigo": 200
        }
    else:
        response = {
            'status': "error",
            'message': "Curso não encontrado!", "codigo": 404
        }
    return jsonify(response)


## Matricular aluno em um curso:

@app.route('/matricularAluno/', methods=['POST'])
def matricularAluno():
    dadosRecebidos = request.get_json()
    idAluno = dadosRecebidos['idAluno']
    idCurso = dadosRecebidos['idCurso']

    banco = connecta_db()
    cursor = banco.cursor()

    sql = f"INSERT INTO matricula (idAluno_FK, idCurso_FK) VALUES ({idAluno}, {idCurso})"
    cursor.execute(sql)
    banco.commit()
    banco.close()

    response = {
        'status': "success",
        'message': "Aluno matriculado com sucesso!", "codigo": 200
    }
    return jsonify(response)
  

if __name__ == '__main__':
    app.run(debug=True)
