matn = "salom dunyo"
natija = {}

for harf in matn:
    if harf != " ":
        natija[harf] = natija.get(harf, 0) + 1

print(natija)
