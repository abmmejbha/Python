gens = 10
axiom = 'A'
char_1, rule_1 = 'A','AB'
char_2, rule_2 = 'B','A'


def apply_rules(axiom):
    res = ''
    for chr in axiom:
        if chr == char_1:
            res += char_1
        else:
            res += rule_2
    return res

for gen in range(gens):
    input()
    print(f'generation {gen}: {axiom}')
axiom = apply_rules(axiom)