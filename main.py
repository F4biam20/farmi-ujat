import flet as ft

def main(page: ft.Page):
    page.title = "FARMI - UJAT"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI - UJAT", size=40),
        center_title=True
    )
    
    # Agregamos el divisor primero (antes de los botones)
    page.add(ft.Divider(color="black"))
    
    # Botón de Interacciones medicamentosas
    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication", size=40, color="black"),
                    ft.Text("Interacciones medicamentosas", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10            
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor=ft.colors.ORANGE_100,
        color="black",
        width=200
    )
    
    # Botón de Alta medicamentos
    btn_alta = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("add_circle", size=40, color="black"),
                    ft.Text("Alta medicamentos", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10            
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor=ft.colors.ORANGE_100,
        color="black",
        width=200
    )
    
    # Botón de Lista medicamentos
    btn_lista = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("list_alt", size=40, color="black"),
                    ft.Text("Lista medicamentos", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10            
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor=ft.colors.ORANGE_100,
        color="black",
        width=200
    )
    
    # Fila para los botones con espaciado entre ellos
    buttons_row = ft.Row(
        controls=[
            btn_interacciones,
            btn_alta,
            btn_lista
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20  # Espacio entre botones
    )
    
    # Contenedor para centrar la fila de botones en la página
    centered_content = ft.Container(
        content=buttons_row,
        margin=ft.margin.only(top=20, bottom=20)  # Margen arriba y abajo
    )
    
    # Agregamos el contenedor centrado a la página después del divisor
    page.add(centered_content)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
