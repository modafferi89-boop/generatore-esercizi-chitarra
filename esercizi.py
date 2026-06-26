import streamlit as st
import random

# Il tuo database
database_esercizi = {
    "Scale": [
        {"nome": "Scala di Do Maggiore (3 ottave)", "difficolta": 2, "durata": 10},
        {"nome": "Scala cromatica (a terzine)", "difficolta": 3, "durata": 5},
    ],
    "Arpeggi": [
        {"nome": "Mauro Giuliani - Esercizio 1", "difficolta": 1, "durata": 15},
    ],
    "Tecnica": [
        {"nome": "Legati ascendenti/discendenti", "difficolta": 2, "durata": 8},
    ]
}

st.title("🎸 Generatore Esercizi Chitarra")
livello = st.slider("Seleziona difficoltà massima", 1, 5, 3)

if st.button("Genera Scheda"):
    tempo_totale = 0
    for categoria, lista in database_esercizi.items():
        filtrati = [ex for ex in lista if ex['difficolta'] <= livello]
        if filtrati:
            scelto = random.choice(filtrati)
            st.write(f"**{categoria}**: {scelto['nome']} ({scelto['durata']} min)")
            tempo_totale += scelto['durata']
    st.success(f"Durata totale: {tempo_totale} minuti")
