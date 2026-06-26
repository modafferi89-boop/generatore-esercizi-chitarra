import random
import datetime

# 1. Database
database_esercizi = {
    "Scale": [
        {"nome": "Scala di Do Maggiore (3 ottave)", "difficolta": 2, "durata": 10},
        {"nome": "Scala cromatica (a terzine)", "difficolta": 3, "durata": 5},
        {"nome": "Scala di La Minore Armonica", "difficolta": 3, "durata": 8}
    ],
    "Arpeggi": [
        {"nome": "Mauro Giuliani - Esercizio 1", "difficolta": 1, "durata": 15},
        {"nome": "Arpeggio con salto di corda", "difficolta": 4, "durata": 10},
        {"nome": "Arpeggio in stile Tarrega", "difficolta": 5, "durata": 12}
    ],
    "Tecnica": [
        {"nome": "Esercizio per l'indipendenza del 4° dito", "difficolta": 3, "durata": 7},
        {"nome": "Legati ascendenti/discendenti", "difficolta": 2, "durata": 8}
    ]
}


# 2. Funzione che genera la scheda e RESTITUISCE i valori
def genera_scheda_del_giorno(livello_max):
    scheda_creata = []
    tempo_totale = 0

    for categoria, lista in database_esercizi.items():
        esercizi_filtrati = [ex for ex in lista if ex['difficolta'] <= livello_max]
        if esercizi_filtrati:
            scelto = random.choice(esercizi_filtrati)
            riga = f"[{categoria.upper()}] -> {scelto['nome']} ({scelto['durata']} min)"
            scheda_creata.append(riga)
            tempo_totale += scelto['durata']
    return scheda_creata, tempo_totale


# 3. Funzione per salvare su file
def salva_scheda_su_file(scheda, tempo_totale):
    data_oggi = datetime.date.today().strftime("%d-%m-%Y")
    nome_file = f"Scheda_Allenamento_{data_oggi}.txt"

    with open(nome_file, "w", encoding="utf-8") as f:
        f.write(f"SCHEDA DI ALLENAMENTO - {data_oggi}\n")
        f.write("=" * 30 + "\n\n")
        for riga in scheda:
            f.write(riga + "\n")
        f.write(f"\nDurata totale: {tempo_totale} minuti.")
    print(f"\n[INFO] Scheda creata con successo: {nome_file}")


# 4. Esecuzione
if __name__ == "__main__":
    livello = 3
    lista_esercizi, tempo = genera_scheda_del_giorno(livello)

    # Stampa a video per controllo
    for riga in lista_esercizi:
        print(riga)
    print(f"\nDurata totale: {tempo} minuti.")

    # Salva il file
    salva_scheda_su_file(lista_esercizi, tempo)