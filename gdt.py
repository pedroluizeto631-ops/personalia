import tkinter as tk
from tkinter import ttk
import random

# ================== CORES ==================
BG_COLOR = "#0f0f0f"
FG_COLOR = "#eaeaea"
GREEN = "#00c853"
GREEN_HOVER = "#00e676"
BOX_COLOR = "#1c1c1c"

# ================== FUNÇÃO ==================
def gerar_treino():
    resultado.delete("1.0", tk.END)

    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())
        idade = int(idade_entry.get())
        nivel = nivel_var.get()
        tipo = tipo_var.get()
        dias_treino = int(dias_entry.get())
    except:
        resultado.insert(tk.END, "⚠️ Preencha todos os campos corretamente.\n")
        return

    # Configuração segura
    if nivel == "Iniciante":
        series = 3
        reps = "10–12"
        fator = 0.6
    else:
        series = 4
        reps = "8–12"
        fator = 0.9

    if idade < 16:
        fator *= 0.8

    # Bases
    academia = {
        "Peito": [{"nome": "Supino reto", "base": 0.5}],
        "Costas": [{"nome": "Remada", "base": 0.5}],
        "Pernas": [{"nome": "Agachamento", "base": 0.8}],
        "Ombro": [{"nome": "Desenvolvimento", "base": 0.4}],
        "Core": [{"nome": "Prancha", "base": 0.0}]
    }

    calistenia = {
        "Peito": ["Flexão", "Flexão inclinada"],
        "Costas": ["Barra australiana"],
        "Pernas": ["Agachamento livre", "Avanço"],
        "Ombro": ["Pike push-up"],
        "Core": ["Prancha"]
    }

    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

    grupo_anterior = None

    for i in range(dias_treino):
        dia = dias_semana[i]
        grupo = random.choice(list(academia.keys()))
        while grupo == grupo_anterior:
            grupo = random.choice(list(academia.keys()))
        grupo_anterior = grupo

        resultado.insert(tk.END, f"\n📅 {dia} — {grupo}\n")

        if tipo == "Academia":
            ex = random.choice(academia[grupo])
            if ex["base"] == 0:
                carga = "Peso corporal"
            else:
                carga = f"{int(peso * ex['base'] * fator)} kg (estimado)"

            resultado.insert(
                tk.END,
                f"• {ex['nome']}\n  Séries: {series} | Reps: {reps}\n  Carga: {carga}\n"
            )

        else:
            ex = random.choice(calistenia[grupo])
            resultado.insert(
                tk.END,
                f"• {ex}\n  Séries: {series} | Reps: {reps}\n  Foco: técnica e controle\n"
            )

        resultado.insert(tk.END, "-" * 40 + "\n")

# ================== JANELA ==================
janela = tk.Tk()
janela.title("Personal Trainer Inteligente")
janela.geometry("720x600")
janela.configure(bg=BG_COLOR)

# ================== TÍTULO ==================
titulo = tk.Label(
    janela,
    text="🏋️ Personal Trainer Inteligente",
    bg=BG_COLOR,
    fg=GREEN,
    font=("Arial", 18, "bold")
)
titulo.pack(pady=15)

# ================== FORM ==================
form = tk.Frame(janela, bg=BG_COLOR)
form.pack()

def criar_input(texto):
    frame = tk.Frame(form, bg=BG_COLOR)
    frame.pack(pady=4)
    tk.Label(frame, text=texto, bg=BG_COLOR, fg=FG_COLOR, width=18, anchor="w").pack(side="left")
    entry = tk.Entry(frame, bg=BOX_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
    entry.pack(side="left")
    return entry

peso_entry = criar_input("Peso (kg)")
altura_entry = criar_input("Altura (m)")
idade_entry = criar_input("Idade")
dias_entry = criar_input("Dias de treino")

# ================== SELECTS ==================
nivel_var = tk.StringVar(value="Iniciante")
tipo_var = tk.StringVar(value="Academia")

def criar_select(label, var, options):
    frame = tk.Frame(form, bg=BG_COLOR)
    frame.pack(pady=4)
    tk.Label(frame, text=label, bg=BG_COLOR, fg=FG_COLOR, width=18, anchor="w").pack(side="left")
    menu = ttk.Combobox(frame, textvariable=var, values=options, state="readonly", width=17)
    menu.pack(side="left")

criar_select("Nível", nivel_var, ["Iniciante", "Intermediário"])
criar_select("Tipo de treino", tipo_var, ["Academia", "Calistenia"])

# ================== BOTÃO ==================
btn = tk.Button(
    janela,
    text="GERAR TREINO",
    bg=GREEN,
    fg="black",
    font=("Arial", 12, "bold"),
    width=25,
    command=gerar_treino,
    activebackground=GREEN_HOVER
)
btn.pack(pady=15)

# ================== RESULTADO ==================
resultado = tk.Text(
    janela,
    bg=BOX_COLOR,
    fg=FG_COLOR,
    insertbackground=FG_COLOR,
    height=16,
    width=85
)
resultado.pack(pady=10)

janela.mainloop()
