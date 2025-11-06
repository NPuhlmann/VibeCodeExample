# Vibe Coding Training Example

Dieses Repository enthält ein Beispielprojekt für **Vibe Coding** Schulungen. Es demonstriert, wie man schnell und effektiv funktionierende Prototypen mit modernen Web-Technologien entwickelt.

## Was ist Vibe Coding?

Vibe Coding ist ein Ansatz zur schnellen Prototypenentwicklung, bei dem der Fokus auf:
- **Funktionalität über Perfektion** liegt
- **Klare, verständliche Strukturen** verwendet werden
- **Schnelles Iterieren** statt langes Planen im Vordergrund steht
- **Aussagekräftige Namen** und minimale, aber hilfreiche Dokumentation genutzt werden

## Projekt: Team Mood Tracker

Das Beispielprojekt ist ein **Team Mood Tracker** - eine Anwendung zum Erfassen und Visualisieren von Team-Stimmungen.

### Features

- 😊 Mood Eingabe mit Emojis
- 📊 Live Dashboard mit Echtzeit-Visualisierung
- 📈 Balkendiagramme und Pie Charts
- 📝 Historie aller Einträge mit Timestamps
- 🔄 Auto-Refresh alle 2 Sekunden

### Tech Stack

- **Backend**: FastAPI mit JSON-Datenspeicherung
- **Frontend**: Streamlit mit Plotly Charts
- **Package Manager**: uv
- **Python**: 3.11+

## Installation & Startup

### Voraussetzungen

- Python 3.11 oder höher
- [uv](https://github.com/astral-sh/uv) Package Manager

### 1. Repository klonen

```bash
git clone https://github.com/NPuhlmann/VibeCodeExample.git
cd VibeCodeExample/test
```

### 2. Dependencies installieren

```bash
uv sync
```

### 3. Backend starten

Öffne ein Terminal und starte das FastAPI Backend:

```bash
uv run uvicorn backend.main:app --reload
```

Das Backend läuft auf: **http://localhost:8000**
API Dokumentation: **http://localhost:8000/docs**

### 4. Frontend starten

Öffne ein **zweites Terminal** im selben Verzeichnis und starte das Streamlit Frontend:

```bash
uv run streamlit run frontend/app.py
```

Das Frontend öffnet sich automatisch im Browser auf: **http://localhost:8501**

## Projektstruktur

```
VibeCodeExample/
├── LICENSE                  # MIT License
├── README.md               # Diese Datei
├── intial_prompt.md        # Original Prompt für die Entwicklung
└── test/                   # Hauptprojekt
    ├── pyproject.toml      # Dependencies
    ├── uv.lock             # Locked Dependencies
    ├── README.md           # Detaillierte Projektdokumentation
    ├── backend/
    │   ├── main.py         # FastAPI Backend
    │   └── moods.json      # Datenspeicher (wird automatisch erstellt)
    └── frontend/
        └── app.py          # Streamlit Frontend
```

## Verwendung

1. **Stimmung eingeben**:
   - Gib deinen Namen ein
   - Wähle ein Emoji (😞 😐 😊 😄 🚀)
   - Klicke auf "Absenden"

2. **Dashboard anschauen**:
   - Balkendiagramm zeigt Anzahl pro Stimmung
   - Pie Chart zeigt prozentuale Verteilung
   - Statistiken und letzte 10 Einträge werden angezeigt

3. **API nutzen**:
   - Besuche http://localhost:8000/docs für interaktive API-Dokumentation
   - GET /moods - Alle Stimmungen abrufen
   - POST /moods - Neue Stimmung hinzufügen

## Für Schulungen

Dieses Projekt eignet sich hervorragend für:
- **Vibe Coding Workshops**: Zeigt den schnellen Prototyping-Ansatz
- **FastAPI Einführungen**: Einfaches REST API Beispiel
- **Streamlit Demos**: Interaktives Dashboard-Design
- **Full-Stack Übungen**: Integration von Backend und Frontend

### Erweiterungsideen für Übungen

- 🔐 Authentifizierung hinzufügen
- 💾 SQLite/PostgreSQL statt JSON verwenden
- 📱 Responsive Design verbessern
- 📧 E-Mail-Benachrichtigungen bei schlechter Stimmung
- 📊 Erweiterte Statistiken und Zeitreihen-Analysen
- 🌐 Multi-Team Support
- 🎨 Customizable Emojis und Themes

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## Kontakt

Für Fragen zu Schulungen oder dem Projekt:
- GitHub: [@NPuhlmann](https://github.com/NPuhlmann)

---

**Happy Vibe Coding! 🚀**
