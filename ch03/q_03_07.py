s = input()

def f(stmt, x):
    if x == len(s):
        return eval(stmt)
    return f(stmt+s[x], x+1) + f(stmt+"+"+s[x], x+1)

print(f(s[0], 1))

#=> https://atcoder.jp/contests/abc045/submissions/18427864