import flet as ft

def main(page: ft.page):
    # NOTE: acao efeito on_change
    def acao(e):
        result.value = texto.value
        page.update()
        
    # NOTE: Configuração da janela
    page.title = "Meu flat app"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # NOTE: Declaraçõa de variaveis
    texto = ft.TextField(label="Digite um texto: ", on_change=acao)
    result = ft.Text(size=30)

    # NOTE: Conteúdo da janela 
    page.add(
        texto,
        result
    )

    # NOTE: Atualização do app
    page.update()

# NOTE: Executa a aplicação
ft.app(main)