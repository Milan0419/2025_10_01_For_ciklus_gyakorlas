"""

3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""


folytatja = True
while folytatja:
    jelszo = input("Kérem adja meg a jelszót: ")
    helyes = ("titok")
    if jelszo == helyes:
        print("Belépés engedélyezve!")
        folytatja = False
    else:
        print("A jelszó helytelen!")
