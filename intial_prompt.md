Du bist ein hilfsbereiter Programmierer, der mir hilft, schnell ein Team Mood Tracker 
Projekt umzusetzen. Ich habe 45-60 Minuten Zeit und möchte folgende Tech-Stack verwenden:

**Stack:**
- Frontend: Streamlit (Python)
- Backend: FastAPI (Python)
- Datenbank: Lokale JSON-Datei
- Package Manager: uv

**Projektanforderungen:**

1. **Projektstruktur:** Erstelle eine klare Folder-Struktur mit separaten Ordnern für Backend 
   und Frontend

2. **Backend (FastAPI):**
   - GET /moods → gibt alle gespeicherten Stimmungen zurück
   - POST /moods → speichert eine neue Stimmung (Name + Emoji/Wert)
   - Die Daten werden in einer moods.json Datei lokal gespeichert
   - CORS muss aktiviert sein für Streamlit-Kommunikation

3. **Frontend (Streamlit):**
   - Ein einfaches Formular mit Name-Input und Emoji-Auswahl (5 Optionen: 😞 😐 😊 😄 🚀)
   - Button zum Absenden, der die Daten zum Backend sendet
   - Ein Live-Dashboard mit Balkendiagramm/Pie-Chart der aktuellen Stimmungen
   - Auto-Refresh alle 2 Sekunden um neue Einträge zu zeigen

4. **Fehlererkennung & UX:**
   - Kurze Fehlermeldungen wenn Backend nicht erreichbar ist
   - Success-Message nach erfolgreichem Speichern
   - Leere Datenbank wird elegant angezeigt

5. **Setup-Anweisungen:**
   - Gib mir die kompletten pyproject.toml für uv
   - Alle notwendigen Befehle zum Starten (Backend + Frontend)
   - Kurze Beschreibung von jedem Schritt

**Vibe Coding Fokus:**
- Priorität: Funktionalität über Perfektion
- Der Code sollte verständlich und gut strukturiert sein
- Verwende aussagekräftige Variablennamen
- Schreibe kurze Kommentare bei komplexeren Stellen

Bitte gib mir den kompletten, produktionsfähigen Code für beide Teile, 
die pyproject.toml Datei und die genauen Schritte zum Starten.
