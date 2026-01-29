from collections import defaultdict
from syntax_tree import Symbol, Union, Concat, Star

class NFA:
    def __init__(self):
        self.transitions = defaultdict(lambda: defaultdict(set))
        self.start = None
        self.accept = None
        self.state_id = 0

    def new_state(self):
        s = self.state_id
        self.state_id += 1
        return s

    @staticmethod
    def from_regex(node):
        nfa = NFA()
        start, accept = nfa._build(node)
        nfa.start = start
        nfa.accept = accept
        return nfa

    def _build(self, node):
        if isinstance(node, Symbol):
            s = self.new_state()
            f = self.new_state()
            self.transitions[s][node.value].add(f)
            return s, f

        if isinstance(node, Union):
            s = self.new_state()
            f = self.new_state()
            ls, lf = self._build(node.left)
            rs, rf = self._build(node.right)
            self.transitions[s]['ε'].update({ls, rs})
            self.transitions[lf]['ε'].add(f)
            self.transitions[rf]['ε'].add(f)
            return s, f

        if isinstance(node, Concat):
            ls, lf = self._build(node.left)
            rs, rf = self._build(node.right)
            self.transitions[lf]['ε'].add(rs)
            return ls, rf

        if isinstance(node, Star):
            s = self.new_state()
            f = self.new_state()
            ns, nf = self._build(node.node)
            self.transitions[s]['ε'].update({ns, f})
            self.transitions[nf]['ε'].update({ns, f})
            return s, f
