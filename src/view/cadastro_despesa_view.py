import flet as ft
from datetime import datetime
from src.model.categoria import Categoria
from src.model.despesas import Despesa
class CadastroDespesaView(ft.View):
    def __init__(self,pagina : ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/cadastrodespesa"
        self.bgcolor = "#000000"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value="TELA DE CADASTRO DE DESPESAS",
                         size=20)

        self.campo_descricao = ft.TextField(label="Descrição")
        self.campo_valor = ft.TextField(label="Valor")
        self.campo_data = ft.TextField(label="Data")

        opcoes_categoria = []
        categorias = Categoria().recuperar()

        for categoria in categorias:
            opcao = ft.DropdownOption(key=categoria.get("id_categoria"),
                              text=categoria.get("nome_categoria"))
            opcoes_categoria.append(opcao)

        self.campo_categoria = ft.Dropdown(options=opcoes_categoria)

        botao_cadastrar = ft.Button(content="Cadastrar",
                                    on_click=self.cadastrar_despesa)

        self.controls=[titulo,
                       self.campo_descricao,
                       self.campo_valor,
                       self.campo_data,
                       self.campo_categoria]

    def cadastrar_despesa(self):
        descricao = self.campo_descricao.value
        valor = self.campo_valor.value
        data = self.campo_data.value
        data_convertida = datetime.strptime(data, "%d/%m/%Y").date()
        id_categoria = self.campo_categoria.value

        Despesa().incluir(self.dados_usuario, id_categoria, descricao, valor, data_convertida)