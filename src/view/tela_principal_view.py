import flet as ft

class PrincipalView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        logo = ft.Image(
        src="logo2.png",
        width=200,
        height=200,
        
    )

        self.pagina = pagina

        self.route = "/principal"

        dados_usuario = pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login")

        self.bgcolor = "#000000"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        titulo = ft.Text(value=f"Seja Bem-vindo(a), {nome_usuario}! \n O que você gostaria de fazer hoje?", 
                         size=20, 
                         color="#ffffff", 
                         text_align=ft.TextAlign.CENTER)

        self.route = "/principal"

        self.controls = [logo, titulo]