# agente_financeiro_inteligente
# 💡 Agente Financeiro Inteligente

O Agente Financeiro Inteligente é um chatbot em Python que funciona como um educador financeiro interativo. O usuário cria seu próprio perfil, adiciona seus gastos e depois conversa com o agente, que analisa os dados e responde de forma educativa com base no objetivo financeiro definido.

⚠️ Projeto educacional. Não recomenda investimentos específicos.

---

## 🎯 Objetivo

- Criar um agente financeiro interativo via terminal (CLI)
- Permitir que o usuário crie seu próprio perfil (nome, renda e objetivo)
- Permitir cadastro de gastos reais pelo usuário
- Analisar automaticamente despesas (total e maior categoria)
- Responder perguntas sobre finanças de forma educativa

---

## 🧠 Como funciona

O sistema funciona em etapas:

1. O usuário informa seu nome, renda e objetivo financeiro
2. O usuário cadastra suas categorias de gastos e valores
3. O sistema calcula automaticamente:
   - Total de gastos
   - Maior categoria de gasto
4. O usuário interage com o agente via terminal
5. O agente responde com base nos dados inseridos e regras simples de lógica

---

## 💬 Exemplo de uso

### ▶️ Cadastro do usuário
Digite seu nome: João  
Digite sua renda mensal: 3000  
Qual seu objetivo financeiro? guardar dinheiro  

---

### ▶️ Cadastro de gastos
Categoria do gasto: moradia  
Valor gasto: 1200  

Categoria do gasto: alimentacao  
Valor gasto: 600  

Categoria do gasto: transporte  
Valor gasto: 300  

Categoria do gasto: lazer  
Valor gasto: 400  

Categoria do gasto: ok  

---

### ▶️ Interação com o agente

Usuário: gastos  

Agente:  
📊 Resumo financeiro de João:  
- Renda: R$ 3000  
- Total gasto: R$ 2500  
- Maior gasto: moradia (R$ 1200)  

💡 Seu objetivo é "guardar dinheiro", então tentar reduzir moradia pode ajudar bastante.

---

Usuário: investir  

Agente:  
📊 Investimentos básicos:  
- Tesouro Direto  
- CDB  
- Fundos de investimento  

💡 Sempre avalie risco antes de investir.

---

Usuário: economizar  

Agente:  
💡 Dica personalizada:  
Como seu objetivo é "guardar dinheiro", reduzir a categoria de maior gasto pode ajudar bastante.

---

## 💡 Tecnologias usadas

- Python  
- Lógica condicional (if/else)  
- Entrada de dados via terminal (input)  
- Estruturas de dados (dicionários)  
- Processamento simples de texto  

---

## 🚀 Próximas melhorias

- Interface gráfica com Streamlit  
- Integração com IA (Ollama ou GPT)  
- Salvamento de dados em JSON/CSV  
- Gráficos de gastos  
- Memória de conversa do usuário  
