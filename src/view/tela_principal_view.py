import flet as ft

class PrincipalView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/principal"

        dados_usuario = pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login")

        self.bgcolor = "#000000"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        titulo = ft.Text(value=f"Seja Bem-vindo(a), {nome_usuario} !", size=20, color="#ffffff")

        self.route = "/principal"

        self.controls = [titulo]