import flet as ft
from src.model.despesas import Despesa

class TodasDespesasView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/todasdespesas"

        self.bgcolor = "#000000"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value="TODAS AS DESPESAS",
                         size=20)
        lista_despesas = []

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="ID DA DESPESA"),
                                                ft.DataColumn(label="DESCRIÇÃO"),
                                                ft.DataColumn(label="VALOR"),
                                                ft.DataColumn(label="CATEGORIA"),
                                                ft.DataColumn(label="DATA")],
                                            rows=lista_despesas)
        
        self.atualizar_lista_despesas()
        self.controls = [titulo, tabela_despesas]

        def atualizar_lista_despesas(self):
            despesas = Despesa().recuperar_todos(self.id_usuario)

            for despesa in despesas:
                id_despesa = str(despesa.get("id_despesa"))
                descricao = str(despesa.get("descricao"))
                valor = str(despesa.get("valor"))
                id_categoria = str(despesa.get("id_categoria"))
                data_despesa = str(despesa.get("data_despesa"))

                linha = ft.DataRow(cells=[
                    ft.DataCell(ft.Text(despesa.get(id_despesa))),
                    ft.DataCell(ft.Text(despesa.get(descricao))),
                    ft.DataCell(ft.Text(despesa.get(valor))),
                    ft.DataCell(ft.Text(despesa.get(id_categoria))),
                    ft.DataCell(ft.Text(despesa.get(data_despesa))),
                ])

                self.lista_despesas.append(linha)

            self.pagina.update()