import pandas as pd
import requests as request
import time 
import os 

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "your_api_key_here")

def gerar_mensagem_ia(nome_lead, produto): 
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-5-nano",   
        "messages": [
            {
                "role": "user",
                "content": f"Olá {nome_lead}, tudo bem? Estou entrando em contato para te apresentar nosso novo produto: {produto}. Gostaria de saber se você tem interesse em conhecer mais sobre ele."
            }
        ],
        "max_tokens": 200
    }
try:
    response = request.post("C:\Users\lukem\OneDrive\Área de Trabalho\ETL_pipiline_vendas\estoque_de_roupas.csv")
    response.raise_for_status()
    message_content = response.json()["choices"][0]["message"]["content"].strip()
    message_content
except request.exceptions.RequestException as e:
    print(f"Erro na requisição para a API: {e}")
    


def enviar_mensagem(email_destinino, assunto, corpo_mensagem):
    # Função fictícia para enviar e-mail
    print(f"Enviando e-mail para: {email_destinino}...\nAssunto: {assunto}\nCorpo da Mensagem: {corpo_mensagem}\n{'-'*40}")
    pass

def pipiline_vendas():
    df_leads = pd.read_csv("leads.csv")
    for index, row in df_leads.iterrows():
        nome_lead = row["nome"]
        email_lead = row["email"]
        produto_interesse = row["produto_interesse"]

        mensagem_ia = gerar_mensagem_ia(nome_lead, produto_interesse)
        if mensagem_ia:
            enviar_mensagem(
                email_destinino=email_lead,
                assunto=f"Apresentação do Produto: {produto_interesse}",
                corpo_mensagem=mensagem_ia
            )
        time.sleep(2)  # Pausa para evitar rate limiting