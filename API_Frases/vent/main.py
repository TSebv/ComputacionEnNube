import json
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="API REST DE FRASES CELEBRES")

DATA_FILE = Path("frases.json")

# Esquema de datos de Pydantic
class FraseBase (BaseModel):
    autor: str = Field(..., min_length=1)
    frase: str = Field(..., min_length=1)

class FraseCreate(FraseBase):
  pass 

class FraseUpdate(FraseBase):
   autor: Optional[str] = Field(None, min_length=1)
   frase: Optional[str] = Field(None, min_length=1)

class Frase(FraseBase):
   id: int

# Funciones auxiliares para I/O del JSON

def cargar_frases() -> List[Frase]:
   if not DATA_FILE.exists():
      return[]
   try:
      with open(DATA_FILE, "r", encoding="utf-8") as f:
       frases = []
       data = json.load(f)
       for d in data:
          frases.append(Frase(**d))
       return frases
    except json.JSONDecodeError:
      return []  