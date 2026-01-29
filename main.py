from regex_parser import RegexParser
from nfa import NFA
from dfa import DFA
from simulator import simulate_dfa

regex = "(a|b)*abb"
string = "aababb"

parser = RegexParser(regex)
ast = parser.parse()

nfa = NFA.from_regex(ast)
dfa = DFA.from_nfa(nfa)

accepted, path = simulate_dfa(dfa, string)

print("Regex:", regex)
print("Stringa:", string)
print("Risultato:", "ACCETTATA" if accepted else "RIFIUTATA")
print("Numero stati DFA:", len(dfa.transitions))
