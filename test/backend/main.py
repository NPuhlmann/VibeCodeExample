from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import os
from datetime import datetime

app = FastAPI(title="Team Mood Tracker API")

# CORS aktivieren für Streamlit-Kommunikation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In Production einschränken!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pfad zur JSON-Datei
MOODS_FILE = os.path.join(os.path.dirname(__file__), "moods.json")


class MoodEntry(BaseModel):
    name: str
    mood: str
    timestamp: str = None


class MoodResponse(BaseModel):
    name: str
    mood: str
    timestamp: str


def load_moods() -> List[dict]:
    """Lädt alle Stimmungen aus der JSON-Datei"""
    if not os.path.exists(MOODS_FILE):
        return []

    try:
        with open(MOODS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_moods(moods: List[dict]) -> None:
    """Speichert alle Stimmungen in die JSON-Datei"""
    with open(MOODS_FILE, "w", encoding="utf-8") as f:
        json.dump(moods, f, ensure_ascii=False, indent=2)


@app.get("/")
async def root():
    """Health Check"""
    return {"message": "Team Mood Tracker API is running", "status": "ok"}


@app.get("/moods", response_model=List[MoodResponse])
async def get_moods():
    """Gibt alle gespeicherten Stimmungen zurück"""
    moods = load_moods()
    return moods


@app.post("/moods", response_model=MoodResponse)
async def add_mood(entry: MoodEntry):
    """Speichert eine neue Stimmung"""
    if not entry.name or not entry.name.strip():
        raise HTTPException(status_code=400, detail="Name darf nicht leer sein")

    if not entry.mood:
        raise HTTPException(status_code=400, detail="Mood darf nicht leer sein")

    # Timestamp hinzufügen falls nicht vorhanden
    if not entry.timestamp:
        entry.timestamp = datetime.now().isoformat()

    # Bestehende Moods laden
    moods = load_moods()

    # Neue Mood hinzufügen
    new_mood = {
        "name": entry.name.strip(),
        "mood": entry.mood,
        "timestamp": entry.timestamp
    }
    moods.append(new_mood)

    # Speichern
    save_moods(moods)

    return new_mood


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
