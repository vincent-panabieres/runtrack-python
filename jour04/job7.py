L = [8, 24, 48, 2, 16]

compteur = 0

for nombre in L:
    if nombre % 3 == 0:
        compteur += 1

print(f"Il y a {compteur} multiples de 3 dans la liste.")