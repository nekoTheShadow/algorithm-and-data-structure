def f(a):
    print(f'--- Aさんが{a}歳の場合 ---')
    lo = 20
    hi = 36
    while hi-lo > 1:
        mi = (lo+hi)//2        
        if a < mi:
            msg = 'Yes'
            hi = mi
        else:
            msg = 'No'
            lo = mi
        print(f'{mi}未満ですか? ---> {msg}')
    print(f'答え {lo}歳')

for a in range(20, 36):
    f(a)

# --- Aさんが20歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> Yes
# 22未満ですか? ---> Yes
# 21未満ですか? ---> Yes
# 答え 20歳
# --- Aさんが21歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> Yes
# 22未満ですか? ---> Yes
# 21未満ですか? ---> No
# 答え 21歳
# --- Aさんが22歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> Yes
# 22未満ですか? ---> No
# 23未満ですか? ---> Yes
# 答え 22歳
# --- Aさんが23歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> Yes
# 22未満ですか? ---> No
# 23未満ですか? ---> No
# 答え 23歳
# --- Aさんが24歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> No
# 26未満ですか? ---> Yes
# 25未満ですか? ---> Yes
# 答え 24歳
# --- Aさんが25歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> No
# 26未満ですか? ---> Yes
# 25未満ですか? ---> No
# 答え 25歳
# --- Aさんが26歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> No
# 26未満ですか? ---> No
# 27未満ですか? ---> Yes
# 答え 26歳
# --- Aさんが27歳の場合 ---
# 28未満ですか? ---> Yes
# 24未満ですか? ---> No
# 26未満ですか? ---> No
# 27未満ですか? ---> No
# 答え 27歳
# --- Aさんが28歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> Yes
# 30未満ですか? ---> Yes
# 29未満ですか? ---> Yes
# 答え 28歳
# --- Aさんが29歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> Yes
# 30未満ですか? ---> Yes
# 29未満ですか? ---> No
# 答え 29歳
# --- Aさんが30歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> Yes
# 30未満ですか? ---> No
# 31未満ですか? ---> Yes
# 答え 30歳
# --- Aさんが31歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> Yes
# 30未満ですか? ---> No
# 31未満ですか? ---> No
# 答え 31歳
# --- Aさんが32歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> No
# 34未満ですか? ---> Yes
# 33未満ですか? ---> Yes
# 答え 32歳
# --- Aさんが33歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> No
# 34未満ですか? ---> Yes
# 33未満ですか? ---> No
# 答え 33歳
# --- Aさんが34歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> No
# 34未満ですか? ---> No
# 35未満ですか? ---> Yes
# 答え 34歳
# --- Aさんが35歳の場合 ---
# 28未満ですか? ---> No
# 32未満ですか? ---> No
# 34未満ですか? ---> No
# 35未満ですか? ---> No
# 答え 35歳