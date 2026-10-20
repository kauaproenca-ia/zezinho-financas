from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(categoria:str, login:str) -> int:
        co, cu = Conexao().conectar

        if not co:
            print("ERRO AO TENTAR CONECTAR")
            return None

        cu.execute("""
                    INSERT INTO tb_categorias (nome_categoria, login, id_categoria)
                    VALUES (%s, %s, %s)
                    """,
                    [categoria, login])

        co.commit()
        co.close()
        return