from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir(login:int, id_categoria:int, descricao:str, valor:float, data:str) -> int:
        co, cu = Conexao().conectar()

        if not co:
            print("ERRO AO CONECTAR")
            return None
        
        try:
            cu.execute("""
                        INSERT INTO tb_despesas (login, valor, data_despesa, descricao, id_categoria)
                        VALUES (%s, %s, %s, %s, %s);
                        """
                        , [login, valor, data, descricao, id_categoria])
            id_despesa = cu.lastrowid
            co.commit()
            co.close()

            return id_despesa
        
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return None
        
    @staticmethod
    def recuperar(login:int) -> list:
        co, cu = Conexao().conectar()
    
        if not co:
            print("Erro ao conectar.")
            return None

        try:
            cu.execute("""
                        SELECT id_categoria, login, nome_categoria
                        FROM tb_categorias
                        WHERE login = %s;
                        """ [login])
            
            categorias = cu.fetchall()
            co.close()
            return categorias

        except Exception as erro:
            print(f"Erro ao recuperar dados: {erro}")
            return None