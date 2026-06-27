import streamlit as st
import random

# Database Ministeriale Completo e Corretto
database_didattico = {
    "Corsi Propedeutici": {
        "Scale": [{"nome": f"Scala di {t} (1 ottava)", "rif": "1.a",
                   "spiegazione": "Controllo dell'appoggio e indipendenza del pollice."} for t in
                  ["Do M", "Sol M", "Re M", "La M", "Mi M", "Fa M", "La m", "Mi m"]],
        "Legati": [
            {"nome": "Legati ascendenti 1-2, 2-3 (1ª corda)", "rif": "2.a",
             "spiegazione": "Hammer-on: colpisci la corda con la punta del dito, mantenendo il dito fermo."},
            {"nome": "Legati discendenti 4-3, 3-2 (1ª corda)", "rif": "2.a",
             "spiegazione": "Pull-off: esercita una leggera trazione laterale per far vibrare la nota inferiore."},
        ],
        "Repertorio": [{"nome": "M. Giuliani - Op. 48 n. 6", "rif": "2.b",
                        "spiegazione": "Studio di arpeggio: stabilità della mano destra."},
                       {"nome": "F. Sor - Studio Op. 60 n. 1", "rif": "2.c",
                        "spiegazione": "Fraseggio: cerca la continuità del suono."}]
    },
    "Corsi Pre-Accademici": {
        "Scale": [{"nome": "Scale magg/min (1 ottava)", "rif": "Base",
                   "spiegazione": "Primo approccio alla corretta postura del polso."}],
        "Legati": [
            {"nome": "Esercizi di legatura elementari", "rif": "Base",
             "spiegazione": "Coordinazione base per una chiara articolazione delle note."},
            {"nome": "Legati su corde vuote (hammer-on)", "rif": "Base",
             "spiegazione": "Precisione assoluta sul tasto."}
        ],
        "Repertorio": [{"nome": "Giuliani - Op. 48 n. 6", "rif": "Studi",
                        "spiegazione": "Pulizia del suono nelle formule di arpeggio semplici."}]
    },
    "I LIVELLO": {
        "Scale": [{"nome": "Scale per terze, seste, ottave e decime", "rif": "1.b",
                   "spiegazione": "Lavoro avanzato sulla micro-intrinsecità della mano sinistra."}],
        "Legati": [
            {"nome": "Legati a 3 note (cromatismo 1-2-3)", "rif": "1.a",
             "spiegazione": "Articolazione tripla: sincronizzazione fondamentale."},
            {"nome": "Legati con estensione 1-4", "rif": "1.a",
             "spiegazione": "Gestione della tensione: rilascia la pressione dopo l'emissione."}
        ],
        "Repertorio": [
            {"nome": "H. Villa-Lobos - Studio n. 1", "rif": "1.b", "spiegazione": "Estensione e fraseggio moderno."},
            {"nome": "M. Legnani - Capriccio n. 1", "rif": "3.a", "spiegazione": "Agilità: pulizia di ogni legame."}]
    },
    "II LIVELLO": {
        "Scale": [{"nome": "Scale estensione massima", "rif": "1.a",
                   "spiegazione": "Gestione della tastiera ad alta velocità."}],
        "Legati": [
            {"nome": "Legati su note doppie (terze legate)", "rif": "1.b",
             "spiegazione": "Coordinazione: le due dita devono scendere simultaneamente."},
            {"nome": "Legati in contesti polifonici (Bach)", "rif": "1.b",
             "spiegazione": "Focus sulla melodia: articola solo la voce superiore."}
        ],
        "Repertorio": [{"nome": "Castelnuovo-Tedesco - Capriccio Diabolico", "rif": "1.d",
                        "spiegazione": "Virtuosismo: il legato come parte della frase."},
                       {"nome": "Turina - Fandanguillo", "rif": "1.d",
                        "spiegazione": "Dinamica: alterna legati dolci a staccato."}]
    }
}

st.title("🎸 Vincenzo Modafferi Accademy Trainer - Ufficiale")

percorso = st.selectbox("Livello Accademico:", list(database_didattico.keys()))
durata_totale = st.select_slider("Durata sessione (minuti):", options=[15, 30, 45, 60, 90, 120])
problema = st.text_area("Difficoltà riscontrata:", placeholder="Es: legati nel II livello, scale per terze...")

if st.button("Genera Programma di Studio"):
    dati = database_didattico[percorso]

    # Selezione singola garantita
    scala = random.choice(dati["Scale"])
    legato = random.choice(dati["Legati"])
    brano = random.choice(dati["Repertorio"])

    t = {"scala": int(durata_totale * 0.25), "legato": int(durata_totale * 0.25), "rep": int(durata_totale * 0.50)}

    st.subheader(f"Piano: {percorso}")
    if problema: st.warning(f"Focus: {problema}")

    for nome, ex, tempo in [("Scale", scala, t["scala"]), ("Studio/Legati", legato, t["legato"]),
                            ("Repertorio", brano, t["rep"])]:
        st.write(f"### 📍 {nome} ({tempo} min)")
        st.write(f"✅ **{ex['nome']}** | *Rif: {ex['rif']}*")
        st.info(f"💡 **Spiegazione Intelligente:** {ex['spiegazione']}")

    st.success("Programma generato con focus didattico completo.")
