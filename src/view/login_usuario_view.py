import flet as ft
from src.model.usuario_model import Usuario

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.bgcolor = "#000000"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="TELA DE LOGIN, VOU CONSTRUIR ELA DEPOIS",
                         size=20,
                         color="#ffffff")

        self.controls=[titulo]