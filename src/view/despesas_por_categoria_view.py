import flet as ft
from src.model.despesas import Despesa
from src.model.categoria import Categoria

class DespesasPorCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/despesasporcategoria"

        self.bgcolor = "#000000"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value="DESPESAS POR CATEGORIA",
                         size=20)
        
        opcoes_categoria = []

        categorias = Categoria().recuperar(self.id_usuario)

        for categoria in categorias:
            opcao = ft.DropdownOption(key=categoria.get("id_categoria"),
                                      text=categoria.get("nome"))
            opcoes_categoria.append(opcao)

        self.campo_categoria = ft.Dropdown(options=opcoes_categoria,
                                               on_select=atualizar_lista_despesas)

        self.lista_despesas = []

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="ID DA DESPESA"),
                                                ft.DataColumn(label="DESCRIÇÃO"),
                                                ft.DataColumn(label="VALOR"),
                                                ft.DataColumn(label="CATEGORIA"),
                                                ft.DataColumn(label="DATA")],
                                            rows=self.lista_despesas)
        
        self.atualizar_lista_despesas()
        self.controls = [titulo, self.campo_categoria, tabela_despesas]

        def atualizar_lista_despesas(self):
            self.lista_despesas.clear()
            id_categoria = self.campo_categoria.value
            despesas = Despesa().recuperar_por_categoria(self.id_usuario, id_categoria)

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
                    ft.DataCell(ft.IconButton(icon=ft.Icons.DELETE,
                                              key=id_despesa))
                ])

                self.lista_despesas.append(linha)

            self.pagina.update()

        def excluir_despesa(self, botao):
            id_despesa = botao.control.key
            Despesa().excluir(id_despesa)
            self.atualizar_lista_despesas()