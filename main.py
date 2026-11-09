import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView

def main(pagina:ft.Page):
    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)

    def roteamento(e=None):
        pagina.view.clear()

        if pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == "/login":
            pagina.views.append(tela_login_usuario)

        pagina.update()

    pagina.on_route_change == roteamento
    roteamento()

    pagina.views.append(tela_cadastro_usuario)
    
ft.run(main)