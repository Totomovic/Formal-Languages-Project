def minimize_dfa(dfa):
    states = set(dfa.transitions.keys())
    alphabet = set()
    for s in states:
        alphabet |= set(dfa.transitions[s].keys())

    P = [dfa.accepting, states - dfa.accepting]
    W = [dfa.accepting]

    while W:
        A = W.pop()
        for c in alphabet:
            X = {s for s in states if dfa.transitions[s].get(c) in A}
            for Y in P[:]:
                inter = X & Y
                diff = Y - X
                if inter and diff:
                    P.remove(Y)
                    P.append(inter)
                    P.append(diff)
                    if Y in W:
                        W.remove(Y)
                        W.append(inter)
                        W.append(diff)
                    else:
                        W.append(inter if len(inter) <= len(diff) else diff)

    new_states = {frozenset(p) for p in P}
    return new_states
