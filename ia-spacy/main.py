from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse
from openai import OpenAI
import spacy

app = FastAPI(title="IA Models + Spacy")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

@app.get("/")
async def root():
    return {"message": "Endpoint Inicial de la API"}

@app.post("/significado-nombre")
async def obtener_significado(nombre: str = Form(...)):
    try:
        respuesta = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "", # Optional. Site title for rankings on openrouter.ai.
            },
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "Eres un experto en etimología de nombres."},
                {"role": "user", "content": f"¿Cuál es el significado del nombre {nombre}?"}
            ]
        )

        significado = respuesta.choices[0].message.content.strip()
        return JSONResponse(content={
            "nombre": nombre,
            "significado": significado
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/analizar-sentimiento")
async def analizar_sentimiento(mensaje: str = Form(...)):
    try:
        respuesta = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "",
                "X-Title": "",
            },
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "Eres un experto en análisis de sentimientos. Analiza el siguiente mensaje y responde únicamente con una de estas etiquetas: positivo, negativo o neutro."},
                {"role": "user", "content": f"Analiza el sentimiento del siguiente mensaje: '{mensaje}'"}
            ]
        )
        sentimiento = respuesta.choices[0].message.content.strip().lower()
        if sentimiento not in ["positivo", "negativo", "neutro"]:
            sentimiento = "neutro"
        return JSONResponse(content={
            "mensaje": mensaje,
            "sentimiento": sentimiento
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/entidades")
async def analizar_entidades(mensaje: str = Form(...)):
    nlp = spacy.load('es_core_news_sm')
    try:
        doc = nlp(mensaje)
        entidades = [
            {"texto": ent.text, "tipo": ent.label_}
            for ent in doc.ents
        ]
        return JSONResponse(content={
            "mensaje": mensaje,
            "entidades": entidades
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)