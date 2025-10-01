"""
5. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""





a = int(input("Kérlek adj meg egy számot 1-10-ig: "))

for i in range(11):
    print(a, "x", i, "=", i*a)