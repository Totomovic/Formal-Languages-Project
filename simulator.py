def simulate_dfa(dfa, string):
    state = dfa.start
    path = [state]
    for char in string:
        if char not in dfa.transitions[state]:
            return False, path
        state = dfa.transitions[state][char]
        path.append(state)
    return state in dfa.accepting, path
