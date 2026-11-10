import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.cadastro_categoria_view import CadastroCategoriaView

def main(pagina:ft.Page):

    def navegacao(componente):
        item_clicado = componente.control.selected_index
        if item_clicado == 0:
            pagina.navigate("/cadastrocategoria")
        elif item_clicado == 1:
            pagina.navigate("/")
        elif item_clicado == 2:
            pagina.navigate("/")
        elif item_clicado == 3:
            pagina.navigate("/")
        elif item_clicado == 4:
            pagina.navigate("/login")

    barra_navegacao = ft.NavigationBar(destinations=[ft.NavigationBarDestination(icon=ft.Icons.CIRCLE, label="Categoria"),
                                    ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Adicionar Despesa"),
                                    ft.NavigationBarDestination(icon=ft.Icons.ADD_ALERT_ROUNDED, label="Todas as despesas"),
                                    ft.NavigationBarDestination(icon=ft.Icons.SIGNAL_CELLULAR_ALT_SHARP, label="Despesas por categoria"),
                                    ft.NavigationBarDestination(icon=ft.Icons.EXIT_TO_APP, label="Sair"),
                                ],
                            on_change=navegacao
                        )

    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    tela_login_usuario.navigation_bar = barra_navegacao
    tela_cadastro_categoria = CadastroCategoriaView(pagina)

    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == "/login":
            pagina.views.append(tela_login_usuario)

        elif pagina.route == "/cadastrocategoria":
            pagina.views.append(tela_cadastro_categoria)

        pagina.update()

    pagina.on_route_change == roteamento
    roteamento()

    pagina.views.append(tela_cadastro_usuario)
    
ft.run(main)