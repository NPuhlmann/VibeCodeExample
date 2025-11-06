import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# Konfiguration
st.set_page_config(
    page_title="Team Mood Tracker",
    page_icon="😊",
    layout="wide"
)

# Backend URL
BACKEND_URL = "http://localhost:8000"

# Mood Optionen
MOOD_OPTIONS = {
    "😞": "Sehr schlecht",
    "😐": "Geht so",
    "😊": "Gut",
    "😄": "Sehr gut",
    "🚀": "Fantastisch"
}


def check_backend_health():
    """Prüft ob das Backend erreichbar ist"""
    try:
        response = requests.get(f"{BACKEND_URL}/", timeout=2)
        return response.status_code == 200
    except:
        return False


def get_moods():
    """Holt alle Stimmungen vom Backend"""
    try:
        response = requests.get(f"{BACKEND_URL}/moods", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Fehler beim Laden der Daten: {str(e)}")
        return None


def submit_mood(name, mood):
    """Sendet eine neue Stimmung zum Backend"""
    try:
        payload = {
            "name": name,
            "mood": mood,
            "timestamp": datetime.now().isoformat()
        }
        response = requests.post(f"{BACKEND_URL}/moods", json=payload, timeout=5)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Fehler beim Speichern: {str(e)}")
        return False


def create_bar_chart(mood_counts):
    """Erstellt ein Balkendiagramm"""
    fig = px.bar(
        x=list(mood_counts.keys()),
        y=list(mood_counts.values()),
        labels={"x": "Stimmung", "y": "Anzahl"},
        title="Stimmungsverteilung (Balkendiagramm)",
        color=list(mood_counts.keys()),
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(showlegend=False, height=400)
    return fig


def create_pie_chart(mood_counts):
    """Erstellt ein Kreisdiagramm"""
    fig = go.Figure(data=[go.Pie(
        labels=list(mood_counts.keys()),
        values=list(mood_counts.values()),
        hole=0.3
    )])
    fig.update_layout(
        title="Stimmungsverteilung (Pie Chart)",
        height=400
    )
    return fig


# Haupttitel
st.title("😊 Team Mood Tracker")
st.markdown("---")

# Backend Status prüfen
if not check_backend_health():
    st.error("⚠️ Backend ist nicht erreichbar! Bitte starte das Backend mit: `uv run uvicorn backend.main:app --reload`")
    st.stop()

# Zwei-Spalten Layout
col1, col2 = st.columns([1, 2])

# Linke Spalte: Formular
with col1:
    st.subheader("📝 Wie ist deine Stimmung?")

    with st.form("mood_form", clear_on_submit=True):
        name = st.text_input("Dein Name", placeholder="z.B. Max Mustermann")

        mood = st.radio(
            "Wähle deine Stimmung:",
            options=list(MOOD_OPTIONS.keys()),
            format_func=lambda x: f"{x} {MOOD_OPTIONS[x]}",
            horizontal=False
        )

        submitted = st.form_submit_button("✅ Absenden", use_container_width=True)

        if submitted:
            if not name or not name.strip():
                st.error("❌ Bitte gib einen Namen ein!")
            else:
                if submit_mood(name.strip(), mood):
                    st.success(f"✅ Danke {name}! Deine Stimmung wurde gespeichert.")
                    time.sleep(1)
                    st.rerun()

# Rechte Spalte: Dashboard
with col2:
    st.subheader("📊 Live Dashboard")

    # Daten laden
    moods = get_moods()

    if moods is None:
        st.warning("⚠️ Keine Verbindung zum Backend möglich.")
    elif len(moods) == 0:
        st.info("👋 Noch keine Einträge vorhanden. Sei der Erste!")
    else:
        # Mood-Counts berechnen
        mood_counts = {}
        for entry in moods:
            mood = entry["mood"]
            mood_counts[mood] = mood_counts.get(mood, 0) + 1

        # Charts nebeneinander anzeigen
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.plotly_chart(create_bar_chart(mood_counts), use_container_width=True)

        with chart_col2:
            st.plotly_chart(create_pie_chart(mood_counts), use_container_width=True)

        # Statistik-Box
        st.markdown("### 📈 Statistiken")
        stat_cols = st.columns(4)
        with stat_cols[0]:
            st.metric("Gesamt Einträge", len(moods))
        with stat_cols[1]:
            most_common = max(mood_counts, key=mood_counts.get)
            st.metric("Häufigste Stimmung", most_common)
        with stat_cols[2]:
            unique_people = len(set(entry["name"] for entry in moods))
            st.metric("Teilnehmer", unique_people)
        with stat_cols[3]:
            avg_mood_value = sum(list(MOOD_OPTIONS.keys()).index(entry["mood"]) for entry in moods) / len(moods)
            st.metric("Durchschnitt", f"{avg_mood_value:.1f}/4")

        # Letzte Einträge
        st.markdown("### 📋 Letzte Einträge")
        df = pd.DataFrame(moods)
        df = df.sort_values("timestamp", ascending=False).head(10)
        df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.strftime("%d.%m.%Y %H:%M")
        st.dataframe(
            df[["name", "mood", "timestamp"]],
            use_container_width=True,
            hide_index=True
        )

# Auto-Refresh alle 2 Sekunden
time.sleep(2)
st.rerun()
