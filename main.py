import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.cadastro_categoria_view import CadastroCategoriaView
from src.view.tela_principal_view import PrincipalView
from src.view.cadastro_despesa_view import CadastroDespesaView

def main(pagina: ft.Page):
    pagina.title = "                                                                                                                                                                                       Zezinho Finanças"

    def navegacao(e):
        item_clicado = e.control.selected_index

        if item_clicado == 0:
            pagina.navigate("/cadastrocategoria")
        elif item_clicado == 1:
            pagina.navigate("/cadastrodespesa")
        elif item_clicado == 2:
            pagina.navigate("/todasdespesas")
        elif item_clicado == 3:
            pagina.navigate("/despesascategoria")
        elif item_clicado == 4:
            pagina.navigate("/login")

    barra_navegacao = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CIRCLE, label="Categoria"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Adicionar Despesa"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_ALERT_ROUNDED, label="Todas as despesas"),
            ft.NavigationBarDestination(icon=ft.Icons.SIGNAL_CELLULAR_ALT_SHARP, label="Despesas por categoria"),
            ft.NavigationBarDestination(icon=ft.Icons.EXIT_TO_APP, label="Sair"),
        ],
        on_change=navegacao
    )

    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == "/cadastro":
            tela_cadastro_usuario = CadastroUsuarioView(pagina)
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == "/login":
            tela_login_usuario = LoginUsuarioView(pagina)
            pagina.views.append(tela_login_usuario)

        elif pagina.route == "/cadastrocategoria":
            tela_cadastro_categoria = CadastroCategoriaView(pagina)
            tela_cadastro_categoria.navigation_bar = barra_navegacao
            pagina.views.append(tela_cadastro_categoria)

        elif pagina.route == "/principal":
            tela_principal = PrincipalView(pagina)
            tela_principal.navigation_bar = barra_navegacao
            pagina.views.append(tela_principal)

        elif pagina.route == "/cadastrodespesa":
            tela_cadastro_despesa = CadastroDespesaView(pagina)
            tela_cadastro_categoria.navigation_bar = barra_navegacao
            pagina.views.append(tela_cadastro_despesa)
        
        pagina.update()

    pagina.on_route_change = roteamento
    roteamento()
    
    pagina.navigate("/login")

ft.run(main)