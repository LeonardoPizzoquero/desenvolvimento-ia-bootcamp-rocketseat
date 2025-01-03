from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib
import os

# Criar uma instância do FastAPI
app = FastAPI()


# Criar uma classe que terá os dados do request body para a API
class request_body(BaseModel):
    horas_estudo: float


# Carregar o modelo de regressão linear
modelo = joblib.load(os.path.join(os.path.dirname(__file__), "modelo_pontuacao.pkl"))

@app.post("/predict")
def predict(data: request_body):
    horas_estudo = [[data.horas_estudo]]

    y_pred = modelo.predict(horas_estudo)[0].astype(int)

    return {
        "pontuacao": y_pred.tolist(),
    }
