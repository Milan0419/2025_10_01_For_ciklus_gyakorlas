'''1. Összegszámítás
Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.'''

szam = int(input("Adj meg egy egész számot, és a program kiszámítja az addig tartó egész számok összegét: "))
alap = 0

for i in range(szam):
    alap += i

print(f"A számok összege: {alap}")