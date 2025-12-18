# 🏋️ Personal Trainer Inteligente

> Um app em **Python + Tkinter** que gera **treinos semanais automáticos**, tanto para **academia** quanto para **calistenia**, pensado para ser **simples, seguro e acessível**.

---

## ✨ Visão geral

Este projeto nasceu da ideia de resolver um problema real:

> Nem todo mundo tem acesso a uma academia, nem todo mundo sabe montar um treino seguro, e muita gente desiste por falta de organização.

O **Personal Trainer Inteligente** gera treinos semanais de forma **aleatória e inteligente**, levando em conta:

* Peso
* Altura
* Idade
* Nível de experiência
* Tipo de treino (Academia ou Calistenia)

Tudo isso com foco em **saúde, progressão consciente e simplicidade**.

---

## 🧠 Como o app funciona (por dentro)

O aplicativo foi desenvolvido usando:

* 🐍 **Python** — linguagem principal
* 🪟 **Tkinter** — interface gráfica (GUI)
* 🎲 **random** — geração aleatória dos treinos

### 🔧 Lógica principal

1. O usuário informa seus dados físicos
2. O app valida os valores (para evitar erros e riscos)
3. Um treino semanal é gerado de forma aleatória
4. O sistema evita repetir o mesmo grupo muscular em dias seguidos
5. O treino é exibido em uma interface **dark mode** com botões verdes

> ⚠️ O app **não prescreve cargas máximas**. Todas as sugestões são **estimativas seguras**, pensadas para evolução gradual.

---

## 🎨 Interface

* 🖤 Fundo escuro (dark mode)
* 💚 Botões verdes
* 🤍 Texto claro e legível
* 📋 Área de resultado com o treino da semana

A interface foi pensada para ser:

* Limpa
* Fácil de usar
* Amigável para iniciantes

---

## 🏋️ Tipos de treino suportados

### 🏢 Academia

* Exercícios com pesos
* Carga estimada com base no peso corporal
* Séries e repetições ajustadas ao nível

### 🏠 Calistenia

* Exercícios com peso do próprio corpo
* Foco em controle, técnica e progressão
* Ideal para quem treina em casa

---

## ⚠️ Aviso IMPORTANTE sobre ALTURA

🚨 **ATENÇÃO** 🚨

O campo **altura** deve ser preenchido em **METROS**, e não em centímetros.

### ✅ Correto

```
1.66
1.70
1.80
```

### ❌ Incorreto

```
166
170
180
```

Se você digitar `166`, o app vai entender que você tem **166 metros** 😅

👉 Sempre use o formato com ponto (`.`).

---

## 🛡️ Segurança e responsabilidade

Este projeto foi feito com foco em:

* Saúde
* Segurança
* Consciência corporal

O aplicativo:

* ❌ Não substitui um profissional
* ❌ Não força cargas perigosas
* ✅ Prioriza técnica e constância

Use o treino como **guia**, não como regra absoluta.

---

## 📁 Estrutura do projeto

```
personal-trainer-inteligente/
│
├── app.py
├── README.md
└── assets/
    └── screenshot.png
```

---

## 🚀 Possíveis evoluções futuras

* 📄 Exportar treino em `.txt` ou `.pdf`
* 📈 Progressão automática semanal
* 🌐 Versão web
* 📱 Versão mobile
* 🎯 Objetivos específicos (força, saúde, estética)

---

## 🙌 Créditos

Projeto criado a partir de uma **ideia original**, com foco em resolver um problema real, usando programação como ferramenta.

> **"Código pode ser aprendido. Pensar soluções é o verdadeiro diferencial."**

---

💚 Sinta-se livre para estudar, modificar e evoluir este projeto.
