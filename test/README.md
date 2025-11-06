# 😊 Team Mood Tracker

Ein einfaches Team Mood Tracking Tool mit FastAPI Backend und Streamlit Frontend.

## Features

- **Mood Eingabe**: Team-Mitglieder können ihre aktuelle Stimmung mit einem Emoji angeben
- **Live Dashboard**: Echtzeit-Visualisierung mit Balkendiagramm und Pie Chart
- **Historie**: Alle Einträge werden mit Timestamp gespeichert
- **Auto-Refresh**: Dashboard aktualisiert sich alle 2 Sekunden automatisch

## Tech Stack

- **Backend**: FastAPI mit JSON-Datenspeicherung
- **Frontend**: Streamlit mit Plotly Charts
- **Package Manager**: uv
- **Python**: 3.11+

## Projektstruktur

```
team-mood-tracker/
├── pyproject.toml          # Dependencies für Backend & Frontend
├── backend/
│   ├── __init__.py
│   ├── main.py            # FastAPI App
│   └── moods.json         # Datenbank (wird automatisch erstellt)
├── frontend/
│   ├── __init__.py
│   └── app.py             # Streamlit App
└── README.md
```

## Installation & Setup

### 1. Dependencies installieren

```bash
uv sync
```

Dieser Befehl installiert alle notwendigen Packages:
- fastapi
- uvicorn
- streamlit
- pandas
- plotly
- requests

### 2. Backend starten

Öffne ein Terminal und starte das FastAPI Backend:

```bash
uv run uvicorn backend.main:app --reload
```

Das Backend läuft nun auf: **http://localhost:8000**

API Dokumentation verfügbar unter: **http://localhost:8000/docs**

### 3. Frontend starten

Öffne ein **zweites Terminal** und starte das Streamlit Frontend:

```bash
uv run streamlit run frontend/app.py
```

Das Frontend öffnet sich automatisch im Browser auf: **http://localhost:8501**

## Verwendung

1. **Stimmung eingeben**:
   - Gib deinen Namen ein
   - Wähle ein Emoji (😞 😐 😊 😄 🚀)
   - Klicke auf "Absenden"

2. **Dashboard anschauen**:
   - Balkendiagramm zeigt Anzahl pro Stimmung
   - Pie Chart zeigt prozentuale Verteilung
   - Statistiken: Gesamt-Einträge, häufigste Stimmung, Teilnehmer
   - Letzte 10 Einträge werden in einer Tabelle angezeigt

3. **Auto-Refresh**:
   - Das Dashboard aktualisiert sich automatisch alle 2 Sekunden
   - Neue Einträge erscheinen sofort im Dashboard

## API Endpoints

### GET /moods
Gibt alle gespeicherten Stimmungen zurück.

**Response**:
```json
[
  {
    "name": "Max Mustermann",
    "mood": "😊",
    "timestamp": "2025-10-31T10:30:00.123456"
  }
]
```

### POST /moods
Speichert eine neue Stimmung.

**Request Body**:
```json
{
  "name": "Max Mustermann",
  "mood": "😊"
}
```

**Response**:
```json
{
  "name": "Max Mustermann",
  "mood": "😊",
  "timestamp": "2025-10-31T10:30:00.123456"
}
```

## Datenspeicherung

Die Daten werden in `backend/moods.json` gespeichert. Format:

```json
[
  {
    "name": "Max Mustermann",
    "mood": "😊",
    "timestamp": "2025-10-31T10:30:00.123456"
  },
  {
    "name": "Erika Musterfrau",
    "mood": "🚀",
    "timestamp": "2025-10-31T10:35:00.789012"
  }
]
```

## Troubleshooting

### Backend nicht erreichbar
Wenn das Frontend die Meldung "Backend ist nicht erreichbar" zeigt:
1. Stelle sicher, dass das Backend läuft (`uv run uvicorn backend.main:app --reload`)
2. Prüfe ob Port 8000 frei ist
3. Schaue in die Backend-Logs im Terminal

### Port bereits belegt
Wenn ein Port bereits belegt ist:
- **Backend**: `uv run uvicorn backend.main:app --reload --port 8001`
- **Frontend**: `uv run streamlit run frontend/app.py --server.port 8502`

Bei Änderung des Backend-Ports muss auch `BACKEND_URL` in `frontend/app.py` angepasst werden.

## Development

- **Backend Hot-Reload**: Mit `--reload` Flag wird der Server bei Code-Änderungen automatisch neu geladen
- **Frontend Hot-Reload**: Streamlit erkennt Änderungen automatisch und bietet einen "Rerun" Button

## Vibe Coding Prinzipien

- Funktionalität über Perfektion
- Klare, verständliche Struktur
- Aussagekräftige Variablennamen
- Kommentare bei komplexeren Stellen
- Schnell prototypen, iterativ verbessern

Viel Spaß beim Tracken eurer Team-Stimmung! 🚀
