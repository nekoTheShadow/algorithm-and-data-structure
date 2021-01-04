# コード4.9をPythonに書き換えたもの
def func(i, w, a):
    if i == 0:
        return w == 0
    
    if func(i-1, w, a): return True
    if func(i-1, w-a[i-1], a): return True
    return False

# コード4.9をメモ化したもの
memo = {}
def memorized_func(i, w, a):
    key = (i, w)
    if key in memo:
        return memo[key]

    if i == 0:
        memo[key] = w == 0
    elif memorized_func(i-1, w, a) or memorized_func(i-1, w-a[i-1], a):
        memo[key] = True
    else:
        memo[key] = False
    return memo[key]

n = 4
a = [3, 2, 6, 5]
w = 14
print(func(n, w, a)) #=> True
print(memorized_func(n, w, a)) #=> True