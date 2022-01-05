from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import csv
from csv import writer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

clienteFile = '../db/cliente.csv'

@app.route('/cliente/inserir', methods=['POST'])
def inserirCliente():
    cliente = json.loads(request.data)
    inserirClienteCsv(cliente)
    return { 'message': 'Cliente salvo com sucesso' }


@app.route('/cliente/listar', methods=['GET'])
def listarCliente():
    clientes = listarClienteCsv()
    return json.dumps(clientes)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/cliente/deletar/<nroLinha>', methods=['DELETE'])
def deletarCliente(nroLinha):
    clientes = listarClienteCsv()
    novosClientes = []       

    i = 0
    for cliente in clientes:        
        if int(nroLinha) != i:
            novosClientes.append(cliente)
        i = i + 1

    reinserirClienteCsv(novosClientes)
    return { 'message': 'Cliente deletado com sucesso' }


def listarClienteCsv():
    clientes = []
    with open(clienteFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                clientes.append({ 
                    'nome': linha[0], 
                    'telefone': linha[1], 
                    'email': linha[2],
                    'cpf': linha[3]
                })
            count += 1

    return clientes


def inserirClienteCsv(cliente):
    novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"], cliente["cpf"]]
    with open(clienteFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirClienteCsv(clientes):
    linhas = []
    linhas.append(["nome", "telefone", "email", "cpf"]) #é necessário inserir novamente o cabeçalho da planilha

    for cliente in clientes:
        novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"], cliente["cpf"]]
        linhas.append(novaLinha)

    with open(clienteFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()
