import flet as ft


def main(page: ft.Page):
    page.title = "calculadora de IMC"
    page.bgcolor = "#03e4f4"
    
    txtPeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("tu IMC es de: ")
    
    img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    btncalcular=ft.ElevatedButton(text = "calcular")
    btnlimpiar=ft.ElevatedButton(text ="limpiar")
    
    page.add(
        ft.Column(
            controls=[
                txtPeso,txtAltura,lblIMC
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btncalcular,btnlimpiar
            ],alignment="CENTER")
    )
    
    
    
    
    
ft.app(main,view=ft.AppView.WEB_BROWSER)