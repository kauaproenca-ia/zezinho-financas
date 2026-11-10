import flet as ft
from src.model.usuario import Usuario
from src.view.cadastro_usuario_view import CadastroUsuarioView

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/login"

        self.title = "                                                                                                                                                                                       Zezinho Finanças"
        self.bgcolor = "#000000"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"
        self.width = 750
        self.height = 750

        logo = ft.Image(
        src="logo.jpg",
        width=250,
        height=250,
        
    )

        titulo = ft.Text(value="Acesse a sua conta!",
                         size=20,
                         color="#ffffff")
        
        self.campo_login = ft.TextField(label="Login",
                                     bgcolor="#ffffff")
        
        self.campo_senha = ft.TextField(label="Senha",
                                   password=True,
                                   can_reveal_password=True,
                                   bgcolor="#ffffff")
        
        botao_entrar = ft.Button(content="Entrar",
                                    width=250,
                                    on_click=self.entrar)
        
        botao_cadastro = ft.Button(content="Cadastre-se",
                                 width=250,
                                 on_click=self.ir_para_cadastro)
        
        self.controls = [logo,
                         titulo,
                         self.campo_login,
                         self.campo_senha,
                         botao_entrar,
                         botao_cadastro]
 

    async def entrar(self, e):
            usuario = self.campo_login.value
            senha = self.campo_senha.value
    
            resultado = Usuario().verificar(usuario,senha)
    
            if resultado:
                self.pagina.show_dialog(ft.SnackBar(content="Login efetuado com sucesso!", bgcolor="#21CA21"))
                self.pagina.session.store.set("usuario_logado", resultado)
                self.pagina.navigate("/principal")
            else:
                self.pagina.show_dialog(ft.SnackBar(content="Erro ao logar. Entre em contato com o administrador", bgcolor="#FF0000"))

    def ir_para_cadastro(self, e):
        self.pagina.navigate("/cadastro")