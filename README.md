# Formal Languages Project – Regex → ε-NFA → DFA

## Descrizione
Tool educativo per studiare linguaggi regolari e automi finiti.  
Partendo da un'espressione regolare, il programma costruisce:

- AST (albero sintattico) della regex  
- ε-NFA tramite algoritmo di Thompson  
- DFA tramite subset construction  
- Simulazione del DFA per verificare se una stringa appartiene al linguaggio  
- Stampa degli stati (`q0`, `q1`, …) e delle transizioni, con indicazione degli stati accettanti

## Funzionalità
- Inserimento interattivo di regex e stringhe  
- Stampa dettagliata degli stati e transizioni del DFA  
- Verifica automatica dell’appartenenza della stringa al linguaggio

## Tecnologie
- Python 3  

## Esempio di utilizzo
```bash
python main.py

### Input
Inserisci la regex: (a|b)*abb
Inserisci la stringa da testare: aababb
### Output
Regex: (a|b)*abb
Stringa: aababb
Risultato: ACCETTATA
Numero stati DFA: 6
q0 = {...}
q1 = {...} (accettante)
...
