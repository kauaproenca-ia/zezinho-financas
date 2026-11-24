import flet as ft
from src.model.categoria import Categoria
class CadastroCategoriaView(ft.View):
    def __init__(self,pagina : ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/cadastrocategoria"
        self.bgcolor = "#000000"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.username = self.dados_usuario.get("login")

        titulo = ft.Text(value="Inclua a sua nova categoria!",
                         color="#ffffff",
                         size=20)

        self.campo_nome_categoria = ft.TextField(label="Nome da categoria",
                                                 color="#000000",
                                                 bgcolor="#ffffff")

        botao_cadastrar = ft.Button(content="Incluir",
                                    width=200,
                                    bgcolor="#089c39",
                                    color="#ffffff",
                                    on_click=self.cadastrar_categoria)

        linha = ft.Row(controls=[
            self.campo_nome_categoria, 
            botao_cadastrar],

            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30
                                                    )

        self.lista_categorias = []
        coluna_lista_categorias = ft.Column(controls=self.lista_categorias)
        titulo_lista = ft.Text(value="Categorias cadastradas",
                               color="#ffffff")

        self.route = "/categoriaview"
        
        self.controls = [titulo,
                         self.campo_nome_categoria,
                         botao_cadastrar,
                         titulo_lista,
                         coluna_lista_categorias]

    def cadastrar_categoria(self):
        nome_categoria = self.campo_nome_categoria.value
        id_usuario = self.dados_usuario.get("id_usuario")
        resultado = Categoria().adicionar(nome_categoria, self.id_usuario)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(content="Cadastro efetuado com sucesso!", bgcolor="#21CA21"))

        else:
            self.pagina.show_dialog(ft.SnackBar(content="Erro ao incluir", bgcolor="#FF0000"))

        self.atualizar_lista_categorias()

    def atualizar_lista_categorias(self):
        self.lista_categorias.clear()
        id_usuario = self.id_usuario.get("id_usuario")
        categorias = Categoria().recuperar(self.id_usuario)

        if categorias:
            for categoria in categorias:
                nome_categoria = categoria.get("nome_categoria")
                texto = ft.Text(value=nome_categoria)
                linha_categoria = ft.Row(controls=[texto,
                                               ft.IconButton(icon=ft.Icons.DELETE,
                                                             key=categoria.get("id_categoria"),
                                                             on_click=self.excluir_categoria)],
                                               alignment="center")
                self.lista_categorias.append(linha_categoria)

        self.pagina.update()

    def excluir_categoria(self, e):
        id_categoria = e.control.key
        Categoria().excluir(id_categoria)

        self.atualizar_lista_categorias()