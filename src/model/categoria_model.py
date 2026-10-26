from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(categoria:str, login:int) -> int:
        co, cu = Conexao().conectar()

        if co == None:
            print("Erro ao conectar.")
            return None

        try:
            cu.execute("""
                        INSERT INTO tb_categoria
                        (categoria, login)
                        VALUES (%s, %s);
                        """,
                        [categoria, login])  
            
            id_categoria = cu.lastrowid

            co.commit()
            co.close()
            
            return id_categoria

        except Exception as e:
            print(f"Erro ao inserir: {e}")
            return None