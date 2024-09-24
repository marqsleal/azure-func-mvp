import logging
import azure.functions as func
import requests
import json
import os

# Endpoint e chave da API do Cognitive Services (local.settings.json)
TEXT_ANALYTICS_ENDPOINT = os.getenv("TEXT_ANALYTICS_ENDPOINT")
TEXT_ANALYTICS_KEY = os.getenv("TEXT_ANALYTICS_KEY")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Recebendo texto para análise de sentimentos.')

    try:
        # Pega o corpo da requisição
        req_body = req.get_json()
        text = req_body.get('text')

        if not text:
            return func.HttpResponse(
                "Por favor, forneça um texto para análise.",
                status_code=400
            )
        
        # Faz a análise de sentimentos usando a API do Cognitive Services
        sentiment = analyze_sentiment(text)

        if sentiment is None:
            return func.HttpResponse(
                "Erro ao processar a análise de sentimentos.",
                status_code=500
            )

        # Retorna o resultado em JSON
        result = {
            "text": text,
            "sentiment": sentiment
        }
        return func.HttpResponse(json.dumps(result), mimetype="application/json", status_code=200)
    
    except ValueError:
        return func.HttpResponse(
             "Erro no formato da requisição. Envie um JSON válido.",
             status_code=400
        )

def analyze_sentiment(text):
    """Chama a API de análise de sentimentos do Azure"""
    url = f"{TEXT_ANALYTICS_ENDPOINT}/text/analytics/v3.0/sentiment"
    headers = {
        'Ocp-Apim-Subscription-Key': TEXT_ANALYTICS_KEY,
        'Content-Type': 'application/json'
    }
    body = {
        "documents": [
            {
                "id": "1",
                "language": "pt",
                "text": text
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        sentiments = response.json()
        return sentiments['documents'][0]['sentiment']
    else:
        logging.error(f"Erro na API de análise de sentimentos: {response.status_code} - {response.text}")
        return None
