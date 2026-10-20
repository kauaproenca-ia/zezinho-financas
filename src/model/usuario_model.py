from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:
        co, cu = Conexao().conectar()

        if not co:
            print("ERRO AO TENTAR CONECTAR")
            return False

        cu.execute("""
                    INSERT INTO tb_usuarios (usuario, senha)
                    VALUES (%s, %s)
                    """,
                    [login, senha])
        co.commit()
        co.close()

        return True