from collections import deque

class DFA:
    def __init__(self):
        self.transitions = {}
        self.start = None
        self.accepting = set()
        self.alphabet = set()

    @staticmethod
    def from_nfa(nfa):

        def epsilon_closure(states):
            stack = list(states)
            closure = set(states)
            while stack:
                s = stack.pop()
                for t in nfa.transitions[s].get('ε', []):
                    if t not in closure:
                        closure.add(t)
                        stack.append(t)
            return frozenset(closure)

        # Calcola alfabeto (escluso ε)
        alphabet = set()
        for s in nfa.transitions:
            for c in nfa.transitions[s]:
                if c != 'ε':
                    alphabet.add(c)

        dfa = DFA()
        dfa.alphabet = alphabet

        start = epsilon_closure({nfa.start})
        dfa.start = start
        dfa.transitions[start] = {}

        queue = deque([start])
        visited = {start}

        while queue:
            current = queue.popleft()
            dfa.transitions[current] = {}

            for symbol in alphabet:
                next_states = set()

                for nfa_state in current:
                    for t in nfa.transitions[nfa_state].get(symbol, []):
                        next_states |= epsilon_closure({t})

                if not next_states:
                    continue

                next_states = frozenset(next_states)
                dfa.transitions[current][symbol] = next_states

                if next_states not in visited:
                    visited.add(next_states)
                    queue.append(next_states)

        # Stati accettanti
        for state in dfa.transitions:
            if nfa.accept in state:
                dfa.accepting.add(state)

        return dfa
