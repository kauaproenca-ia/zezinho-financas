import flet as ft
from src.model.usuario import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/cadastro"
        self.title = "                                                                                                                                                                                       Zezinho Finanças"
        self.bgcolor = "#000000"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        logo = ft.Image(
        src="logo.jpg",
        width=250,
        height=250,
        
    )

        titulo = ft.Text(value="Cadastro de usuário",
                         size=20,
                         color="#ffffff")
        
        self.login = ft.TextField(label="Login",
                                     bgcolor="#ffffff")
        
        self.campo_senha = ft.TextField(label="Senha",
                                   password=True,
                                   can_reveal_password=True,
                                   bgcolor="#ffffff")
        
        botao_cadastrar = ft.Button(content="Cadastrar",
                                    width=305,
                                    on_click=self.cadastrar,
                                    bgcolor="#089c39",
                                    color="#ffffff")
        
        botao_voltar = ft.Button(content="Já tem uma conta? Volte para o login!",
                                 width=305,
                                 on_click=self.ir_para_login,
                                 bgcolor="#0936ff",
                                 color="#ffffff")
        
        self.controls = [logo,
                         titulo,
                         self.login,
                         self.campo_senha,
                         botao_cadastrar,
                         botao_voltar]
                
    def cadastrar(self, e):
        usuario = self.login.value
        senha = self.campo_senha.value
        if usuario == "" or senha == "":
            self.pagina.show_dialog(ft.SnackBar(content="Preencha todos os campos!", bgcolor="#babaca"))
            return

        resultado = Usuario().cadastrar(usuario,senha)

        if resultado == True:
            #SNACKBAR MOSTRANDO QUE DEU CERTO
            self.pagina.show_dialog(ft.SnackBar(content="Cadastro efetuado com sucesso!", bgcolor="#21CA21"))

        else:
            self.pagina.show_dialog(ft.SnackBar(content="Usuário com esse nome já existente. Escolha outro nome para dar continuidade ao seu cadastro!", bgcolor="#FF0000"))

    def ir_para_login(self, e):
        self.pagina.navigate("/login")