from collections import defaultdict, deque

class DFA:
    def __init__(self):
        self.transitions = {}
        self.start = None
        self.accepting = set()

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

        start = epsilon_closure({nfa.start})
        queue = deque([start])
        dfa = DFA()
        dfa.start = start
        dfa.transitions[start] = {}

        while queue:
            current = queue.popleft()
            for state in current:
                for symbol in nfa.transitions[state]:
                    if symbol == 'ε':
                        continue
                    targets = set()
                    for t in nfa.transitions[state][symbol]:
                        targets |= epsilon_closure({t})
                    targets = frozenset(targets)
                    if current not in dfa.transitions:
                        dfa.transitions[current] = {}
                    dfa.transitions[current][symbol] = targets
                    if targets not in dfa.transitions:
                        dfa.transitions[targets] = {}
                        queue.append(targets)

        for state in dfa.transitions:
            if nfa.accept in state:
                dfa.accepting.add(state)

        return dfa
