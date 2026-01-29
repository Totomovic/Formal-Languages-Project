class RegexNode:
    pass

class Symbol(RegexNode):
    def __init__(self, value):
        self.value = value

class Union(RegexNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Concat(RegexNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Star(RegexNode):
    def __init__(self, node):
        self.node = node
