import flet as ft

def main(page: ft.Page):
    #EVENTO
    def acao(e):
        verificacao = 'é maior de idade' if int(idade.value) >= 18 else 'é menor de idade'
        result.value = f'{nome.value} {verificacao}'
        
        nome.value = ''
        idade.value = ''
        
        page.update()
        
    page.title = 'Maioridade'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    nome = ft.TextField(label='Nome')
    idade = ft.TextField(label='Idade', suffix_text='anos', on_submit=acao)
    result = ft.Text(size=30)
    
    page.add(
        ft.Row(
            [ft.Text('Maioridade', size=40, weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [idade],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton('Calcular maioridade', on_click=acao)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )    
    
    page.update()
    
ft.app(main)
    
    