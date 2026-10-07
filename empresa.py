import flet as ft
import random
import datetime

class EmpresaGame:
    def __init__(self):
        self.nome = "Minha Corp"
        self.saldo = 5000.00
        self.lucro_mes = 0
        self.gastos_mes = 1200
        self.nivel = 1
        self.funcionarios = 2
        self.historico_lucro = [800, 1200, 950, 1500, 1100, 1800]
        self.upgrades = [
            {"nome": "Marketing Digital", "preco": 1000, "bonus": 500, "comprado": False, "icone": "📢"},
            {"nome": "Mais Funcionários", "preco": 2500, "bonus": 1200, "comprado": False, "icone": "👥"},
            {"nome": "Máquina Nova", "preco": 4000, "bonus": 2500, "comprado": False, "icone": "⚙️"},
            {"nome": "Filial", "preco": 8000, "bonus": 5000, "comprado": False, "icone": "🏢"},
        ]
        self.chat_msgs = [
            {"nome": "Ana - Financeiro", "msg": "Chefe, o lucro subiu esse mês! 📈", "hora": "09:32"},
            {"nome": "Carlos - Vendas", "msg": "Precisamos investir em marketing", "hora": "10:15"},
        ]

def main(page: ft.Page):
    page.title = "Empresa Tycoon"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0f172a"
    page.padding = 0
    page.window_width = 400
    page.window_height = 800

    game = EmpresaGame()

    # --- TELAS ---
    saldo_text = ft.Text(f"R$ {game.saldo:,.2f}", size=28, weight="bold", color="#22c55e")
    lucro_text = ft.Text(f"+ R$ {game.lucro_mes}", color="#22c55e")
    gasto_text = ft.Text(f"- R$ {game.gastos_mes}", color="#ef4444")

    # Grafico simples com barras
    def build_grafico():
        barras = []
        max_val = max(game.historico_lucro) if game.historico_lucro else 1
        for i, valor in enumerate(game.historico_lucro[-6:]):
            altura = (valor / max_val) * 80 + 20
            barras.append(
                ft.Column([
                    ft.Container(height=altura, width=35, bgcolor="#3b82f6", border_radius=8, 
                                 content=ft.Text(f"{valor}", size=8, color="white", text_align="center")),
                    ft.Text(f"M{i+1}", size=10, color="grey")
                ], horizontal_alignment="center")
            )
        return ft.Row(barras, alignment
