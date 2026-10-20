from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:
        co, cu = Conexao().conectar()
        cu.execute("""
                    INSERT INTO tb_usuarios (usuario, senha)
                    VALUES (%s, %s)
                    """,
                    [login, senha])