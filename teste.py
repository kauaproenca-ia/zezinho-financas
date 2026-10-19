from src.database.conexao import Conexao

conexao, cursor = Conexao().conectar()

print(conexao)