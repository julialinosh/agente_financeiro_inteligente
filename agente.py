
import re

# =========================
# PERFIL DO USUÁRIO (DINÂMICO)
# =========================

print("💡 Bem-vindo ao Agente Financeiro Inteligente!
")

nome = input("Digite seu nome: ")
renda = float(input("Digite sua renda mensal: "))
objetivo = input("Qual seu objetivo financeiro? ")

perfil = {
    "nome": nome,
    "renda_mensal": renda,
    "objetivo": objetivo
}

# =========================
# TRANSAÇÕES DO USUÁRIO
# =========================

print("
💰 Agora vamos cadastrar seus gastos.")
print("Digite 'ok' para parar.
")

transacoes = {}

while True:
    categoria = input("Categoria do gasto (ou 'ok'): ")

    if categoria.lower() == "ok":
        break

    valor = float(input("Valor gasto: "))

    if categoria in transacoes:
        transacoes[categoria] += valor
    else:
        transacoes[categoria] = valor

# =========================
# FUNÇÕES AUXILIARES
# =========================

def calcular_gastos():
    maior_categoria = max(transacoes, key=transacoes.get)
    maior_valor = transacoes[maior_categoria]
    total = sum(transacoes.values())
    return maior_categoria, maior_valor, total


# =========================
# AGENTE
# =========================

def responder(pergunta):
    pergunta_lower = pergunta.lower()

    if len(transacoes) > 0:
        maior_categoria, maior_valor, total = calcular_gastos()
    else:
        maior_categoria, maior_valor, total = "nenhum", 0, 0

    # =========================
    # INVESTIMENTOS
    # =========================
    if any(p in pergunta_lower for p in ["invest", "aplicar", "cdb", "tesouro", "fundos"]):

        return (
            f"📊 Análise para {perfil['nome']}:
"
            f"Seu objetivo é '{perfil['objetivo']}'.

"
            "💡 Investimentos básicos:
"
            "- Tesouro Direto
"
            "- CDB
"
            "- Fundos de investimento

"
            "Sempre avalie risco antes de investir."
        )

    # =========================
    # GASTOS
    # =========================
    elif any(p in pergunta_lower for p in ["gasto", "analise", "quanto", "dinheiro"]):

        return (
            f"📊 Resumo financeiro de {perfil['nome']}:
"
            f"- Renda: R$ {perfil['renda_mensal']}
"
            f"- Total gasto: R$ {total}
"
            f"- Maior gasto: {maior_categoria} (R$ {maior_valor})

"
            f"💡 Seu objetivo é '{perfil['objetivo']}', "
            f"tente otimizar {maior_categoria}."
        )

    # =========================
    # ECONOMIA
    # =========================
    elif any(p in pergunta_lower for p in ["economizar", "poupar", "guardar"]):

        return (
            f"💡 Dica para {perfil['nome']}:
"
            f"Como seu objetivo é '{perfil['objetivo']}', "
            f"reduzir {maior_categoria} pode ajudar bastante."
        )

    # =========================
    # FALLBACK
    # =========================
    else:
        return (
            "🤖 Posso te ajudar com:
"
            "- investimentos
"
            "- análise de gastos
"
            "- economia

"
            "Tente perguntar de outra forma 😊"
        )


# =========================
# LOOP DE CONVERSA
# =========================

print("
💡 Agente Financeiro Inteligente iniciado!")
print("Agora você pode conversar com o agente.
")

while True:

    pergunta = input("👉 Você: ")

    if pergunta.lower() == "sair":
        print("Agente: Até mais! 👋")
        break

    resposta = responder(pergunta)
    print("Agente:", resposta)
