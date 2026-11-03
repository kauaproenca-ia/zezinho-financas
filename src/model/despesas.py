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
    def recuperar_todos(login:int) -> list:
        co, cu = Conexao().conectar()
    
        if not co:
            print("Erro ao conectar.")
            return None

        try:
            cu.execute("""
                        SELECT id_despesa, login, valor, data_despesa, descricao, id_categoria
                        FROM tb_despesas
                        WHERE login = %s;
                        """ [login])
            
            despesas = cu.fetchall()
            co.close()
            return despesas

        except Exception as erro:
            print(f"Erro ao recuperar dados: {erro}")
            return None
        

        
    @staticmethod
    def excluir(id_despesa:int) -> bool:
        co, cu = Conexao().conectar()

        if not co:
            print("Erro ao conectar")
            return False

        try:
            cu.execute("""
                        DELETE FROM tb_despesa
                        WHERE id_despesa = %s;
                        """, 
                        [id_despesa])

            co.commit()
            co.close()
            return True

        except Exception as erro:
            print(f"Erro ao excluir: {erro}")
            return False
        
    @staticmethod
    def alterar(id_despesa:int, login:int, id_categoria:int, data:str, descricao:str, valor:int) -> bool:
        co, cu = Conexao().conectar()

        if co == None:
            print("Erro ao conectar.")
            return False

        try:
            cu.execute("""
                        UPDATE tb_despesas SET
                            id_categoria = %s,
                            descricao = %s,
                            valor = %s,
                            data_despesa = %s
                        WHERE
                            id_despesa = %s
                            AND id_usuario = %s;
                        """,
                        [id_categoria, descricao, valor, data, id_despesa, login])  

            co.commit()
            co.close()
            
            return True

        except Exception as e:
            print(f"Erro ao inserir: {e}")
            return False