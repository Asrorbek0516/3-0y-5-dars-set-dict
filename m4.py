from collections import Counter

mevalar = ["olma", "banan", "olma", "uzum", "banan"]
takrorlanishlar_soni = Counter(mevalar)

print(takrorlanishlar_soni)


mevalar = ["olma", "banan", "olma", "uzum", "banan"]
natija = {}

for i in mevalar:
    natija[i] = natija.get(i, 0) + 1

print(natija)