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

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("login")

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

        self.atualizar_lista_categorias()
        
        self.controls = [titulo,
                         linha,
                         titulo_lista,
                         coluna_lista_categorias]

    def cadastrar_categoria(self):
        nome_categoria = self.campo_nome_categoria.value

        resultado = Categoria().adicionar(nome_categoria, self.id_usuario)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(content="Cadastro efetuado com sucesso!", bgcolor="#21CA21"))

        else:
            self.pagina.show_dialog(ft.SnackBar(content="Erro ao incluir", bgcolor="#FF0000"))

        self.atualizar_lista_categorias()

    def atualizar_lista_categorias(self):
        categorias = Categoria().recuperar(self.id_usuario)

        for categoria in categorias:
            nome_categoria = categoria.get("nome_categoria")
            texto = ft.Text(value=nome_categoria)
            self.lista_categorias.append(texto)

            self.pagina.update()