# MVP Azure Functions - Sentiment Analysis
_Projeto para fins acadêmicos criando um MVP com Azure Functions e Text Analysis do Azure Cognitive Services para realizar analise de sentimentos baseados em texto._

# Configurações do Ambiente Virtual

## Instalando Python3.11:
```bash:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
```
## Criando ambiente virtual:
```bash
python3.11 -m venv --without-pip azure_env
```

## Iniciando ambiente virtual:
```bash
source azure_env/bin/activate
```

## Instalando pip no ambiente virtual:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

## Instalando Azure Functions no ambiente virtual:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

# Configurações locais:

local.settings.json:
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "TEXT_ANALYTICS_ENDPOINT": "https://<seu_endpoint>.cognitiveservices.azure.com/",
    "TEXT_ANALYTICS_KEY": "<sua_chave>"
  }
}
```

# Iniciando MVP

## Inicie o ambiente virtual:
```bash
source azure_env/bin/activate
```

## Iniciando Projeto:
```bash
func init SentimentAnalysis --python
```

## Criando Função HTTP Trigger:
```bash
func new --template "HTTP trigger" --name SentimentAnalysisFunction
```

```bash
func start
```

post -> `http://localhost:7071/api/SentimentAnalysisFunction`
corpo:
```bash
{
  "text": "Hoje é um ótimo dia!"
}
```
