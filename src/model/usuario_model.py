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
        
        try:
            cu.execute("""
                        INSERT INTO tb_usuarios (usuario, senha)
                        VALUES (%s, %s)
                        """,
                        [login, senha])
            
            co.commit()
            co.close()

            return True
        
        except Exception as erro:
        
            print(f"ERRO AO INSERIR: {erro}")
            return False

    @staticmethod
    def verificar(login:str, senha:str) -> dict:
        co, cu = Conexao().conectar()
    
        if not co:
            print("ERRO AO TENTAR CONECTAR")
            return None

        cu.execute("""
                    SELECT usuario, senha FROM tb_usuarios
                    WHERE usuario = %s
                    AND senha = %s;
                    """,
                    [login, senha])
        
        resultado = cu.fetchone()

        co.close()

        return resultado