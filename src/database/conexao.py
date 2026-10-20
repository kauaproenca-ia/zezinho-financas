import mysql.connector

class Conexao:
    def __init__(self):
        pass

    @staticmethod
    def conectar():
        try:
            #Criar a conexão com o banco de dados MySQL
            conexao = mysql.connector.connect(host="localhost",
                                            port=3306,
                                            user="root",
                                            password="root",
                                            database="zezinho_financas")
            cursor = conexao.cursor(dictionary=True)

            return conexao, cursor
        except Exception as erro:
            print(f"ERRO: {erro}")
            return None, None #11111111111  