import z3

def digit(vars):
    return sum(var * (10**i) for i, var in enumerate(reversed(vars)))


def solve(question):
    solver = z3.Solver()

    # 文字列questionを評価する
    rows = []
    for i, line in enumerate(question.split('\n')):
        if line == '' or  line.startswith('-'): 
            continue
        
        row = []
        for j, ch in enumerate(line):
            if ch == 'x':
                v = z3.Int(f'{i}_{j}')
                if len(row) == 0:
                    solver.add(1 <= v, v <= 9)
                else:
                    solver.add(0 <= v, v <= 9)
                row.append(v)
            
            if ch.isdigit():
                row.append(int(ch))

        rows.append(row)


    # 計算途中の制約
    for i, v in enumerate(reversed(rows[1])):
        solver.add(digit(rows[0])*v == digit(rows[2+i]))

    # answerの制約
    solver.add(digit(rows[0])*digit(rows[1]) == digit(rows[-1]))

    assert solver.check() == z3.sat

    # pretty printの準備
    answers = []
    model = solver.model()
    for i, line in enumerate(question.split('\n')):
        answer = []
        for j, ch in enumerate(line):
            if ch == 'x':
                answer.append(model.eval(z3.Int(f'{i}_{j}')))
            else:
                answer.append(ch)
        answers.append(answer)

    # pretty print
    for answer in answers:
        line = ''.join(map(str, answer))
        if line != '':
            print(line)
