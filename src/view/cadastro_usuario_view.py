import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/cadastro"

        self.bgcolor = "#000000"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="Cadastro de usuário",
                         size=20,
                         color="#ffffff")
        self.campo_usuario = ft.TextField(label="Usuário",
                                     bgcolor="#ffffff")
        self.campo_senha = ft.TextField(label="Senha",
                                   password=True,
                                   can_reveal_password=True,
                                   bgcolor="#ffffff")
        
        botao_cadastrar = ft.Button(content="CADASTRAR",
                                    width=250,
                                    on_click=self.cadastrar)
        
        botao_voltar = ft.Button(content="Volte para o login",
                                 width=250)
        
        self.controls = [titulo,
                         self.campo_usuario,
                         self.campo_senha,
                         botao_cadastrar,
                         botao_voltar]
                
    def cadastrar(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value
        Usuario().cadastrar(usuario,senha)

        if usuario == "" or senha == "":
            self.pagina.show_dialog(ft.SnackBar(content="Preencha todos os campos!", bgcolor="#babaca"))
            return

        resultado = Usuario().cadastrar(usuario,senha)

        if resultado == True:
            #SNACKBAR MOSTRANDO QUE DEU CERTO
            self.pagina.show_dialog(ft.SnackBar(content="Cadastro efetuado com sucesso!", bgcolor="#21CA21"))

        else:
            self.pagina.show_dialog(ft.SnackBar(content="Erro ao cadastrar. Entre em contato com o administrador", bgcolor="#FF0000"))

