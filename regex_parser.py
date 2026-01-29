from syntax_tree import Union, Concat, Star, Symbol

class RegexParser:
    def __init__(self, regex):
        self.regex = regex
        self.pos = 0

    def parse(self):
        return self.parse_union()

    def parse_union(self):
        left = self.parse_concat()
        while self.current() == '|':
            self.pos += 1
            right = self.parse_concat()
            left = Union(left, right)
        return left

    def parse_concat(self):
        nodes = []
        while self.current() and self.current() not in ')|':
            nodes.append(self.parse_star())
        if not nodes:
            return None
        node = nodes[0]
        for n in nodes[1:]:
            node = Concat(node, n)
        return node

    def parse_star(self):
        node = self.parse_atom()
        while self.current() == '*':
            self.pos += 1
            node = Star(node)
        return node

    def parse_atom(self):
        if self.current() == '(':
            self.pos += 1
            node = self.parse_union()
            self.pos += 1  # )
            return node
        char = self.current()
        self.pos += 1
        return Symbol(char)

    def current(self):
        if self.pos >= len(self.regex):
            return None
        return self.regex[self.pos]
