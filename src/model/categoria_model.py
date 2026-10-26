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
        
    @staticmethod
    def excluir(id_categorias:int) -> bool:
        co, cu = Conexao().conectar()

        if not co:
            print("Erro ao conectar.")
            return False

        try:
            cu.execute("""
                        DELETE FROM tb_categoria
                        WHERE id_categoria = %s;
                        """, 
                        [id_categorias])

            co.commit()
            co.close()
            return True

        except Exception as e:
            print(f"Erro ao excluir: {e}")
            return False