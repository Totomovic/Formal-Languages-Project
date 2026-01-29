from regex_parser import RegexParser
from nfa import NFA
from dfa import DFA
from simulator import simulate_dfa 


def print_dfa_states(dfa):
    state_names = {}
    for i, state in enumerate(dfa.transitions.keys()):
        state_names[state] = f"q{i}"

    print("\nStati DFA:")
    for state, name in state_names.items():
        acc = " (accettante)" if state in dfa.accepting else ""
        print(f"{name} = {set(state)}{acc}")

    print("\nTransizioni:")
    for state, name in state_names.items():
        for symbol, target in dfa.transitions[state].items():
            print(f"{name} --{symbol}--> {state_names[target]}")

regex = input("Inserisci la regex: ")
string = input("Inserisci la stringa da testare: ")


parser = RegexParser(regex)
ast = parser.parse()

nfa = NFA.from_regex(ast)
dfa = DFA.from_nfa(nfa)

accepted, path = simulate_dfa(dfa, string)

print("Regex:", regex)
print("Stringa:", string)
print("Risultato:", "ACCETTATA" if accepted else "RIFIUTATA")
print("Numero stati DFA:", len(dfa.transitions))
print_dfa_states(dfa)
 
