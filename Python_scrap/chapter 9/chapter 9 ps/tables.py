def table(n):
    gentable=""
    for i in range(1,11):
        gentable+= f"{n}X {i}={n*i}\n"

    with open(f"tabels/table_{n}.txt","w")as f:
         f.write(gentable)

for i in range(2,21):
    table(i)
