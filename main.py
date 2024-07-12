import flet as ft
import flet_easy as fs

app = fs.FletEasy(route_init="/")


# We add a page
@app.page(route="/", title="FTWindow - Home")
def index_page(data: fs.Datasy):
    page = data.page
    page.adaptive = True
    return ft.View(
        controls=[
            ft.AppBar(title=ft.Text("FTWindow")),
            ft.Text("Home page"),
            ft.FilledButton("Go to Counter", on_click=data.go("/counter")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )


# We add a second page
@app.page(route="/counter", title="Counter")
def counter_page(data: fs.Datasy):
    page = data.page
    page.adaptive = True
    txt_number = ft.TextField(value="0", text_align="right", width=100)
    page.appbar = ft.AppBar(title=ft.Text("FTWindow"))

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    return ft.View(
        controls=[
            ft.AppBar(title=ft.Text("FTWindow")),
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
            ft.FilledButton("Go to Home", on_click=data.go("/")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )


@app.page_404("/FletEasy-404", title="Error 404", page_clear=True)
def page404(data: fs.Datasy):
    return ft.View(
        controls=[
            ft.Text(f"Custom 404 error", size=30),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


app.run()
