nums = [3, 1, 4, 1, 5, 3, 3]
natija = {}

for i in nums:
    natija[i] = natija.get(i,0)+1

print(natija)
