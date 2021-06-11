#------------------------------------------------------
#   Fast API
#------------------------------------------------------
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from book_woofer.predict import load_the_model, predict
import os
#------------------------------------------------------
app = FastAPI()
#------------------------------------------------------
model, tokenizer = load_the_model() # Load model function with a robust path
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
#------------------------------------------------------
@app.get("/")
def index():
    return {"ok": True}
#------------------------------------------------------
@app.post("/predict/")
async def prediction(text: str):
    pred =  predict(text, model, tokenizer)
    return {'prediction': [float(i) for i in pred]}
