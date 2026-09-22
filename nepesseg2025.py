import os

nepesseg_adatok = []

with open("lakossag_2025.csv", "r", encoding="UTF-8") as forrasfajl:
    forrasfajl.readline()

    for sor in forrasfajl:
        adatok = sor.strip().split(";")

        nepesseg_adat = {
            "megyekod": adatok[0],
            "telepules": adatok[1],
            "tipus": adatok[2],
            "ferfi": int(adatok[3].replace(" ", "")),
            "no": int(adatok[4].replace(" ", ""))
        }

        nepesseg_adatok.append(nepesseg_adat)
        

def menupont_valaszto(menupont):
    match menupont:
        case "1": megye_adatok()
        case "2": telepules_tipus()
        case "x": return
        case _: print("Hibás menüpont!")


def telepules_tipus_menupontok():
    telepules_tipusok = []

    for n in nepesseg_adatok:
        if n["tipus"] in telepules_tipusok:
            continue
        else:
            telepules_tipusok.append(n["tipus"])

    for index, tipus in enumerate(telepules_tipusok):
        print(f"[{index + 1}] {tipus}")

    while True:
        telepules = input("Kérem a település típusának sorszámát: ").strip()

        try:
            sorszam = int(telepules)

            if 1 <= sorszam <= len(telepules_tipusok):
                return telepules_tipusok[sorszam - 1]

            print("Nincs ilyen sorszám!")

        except ValueError:
            print("Kérem, számot adjon meg!")


def megye_adatok():
    while True:
        megyekod_bevitel = input("Kérem a megye kódját (pl: haj - Hajdú-Bihar megye): ").strip()

        megyekod_letezik = False

        for n in nepesseg_adatok:
            if n["megyekod"].lower() == megyekod_bevitel.lower():
                megyekod_letezik = True
                break

        if megyekod_letezik:
            break

        print("Hibás megye kód! Kérem, adjon meg egy létező kódot.")

    telepulesek_szama = 0
    lakosok_szama = 0
    varosok_lakoinak_szama = 0

    for n in nepesseg_adatok:
        if n["megyekod"].lower() == megyekod_bevitel.lower():

            telepulesek_szama += 1

            lakosok_szama += n["ferfi"] + n["no"]

            if (
                n["tipus"].lower() == "város"
                or n["tipus"].lower() == "vármegyei jogú város"
                or n["tipus"].lower() == "vármegye székhely"
                or n["tipus"].lower() == "fővárosi kerület"
            ):
                varosok_lakoinak_szama += n["ferfi"] + n["no"]

    print(f"Települések száma: {telepulesek_szama}")
    print(f"Összes lakos: {lakosok_szama} fő")
    print(
        f"Városok lakosai összesen: "
        f"{varosok_lakoinak_szama} fő"
    )


def telepules_tipus():
    print("Válasszon településtípust!")

    telepules_tipus = telepules_tipus_menupontok()

    try:
        terminal_height = os.get_terminal_size().lines - 6
    except OSError:
        terminal_height = 20

    telepules_adatok = []

    for n in nepesseg_adatok:
        if n["tipus"].lower() == telepules_tipus.lower():
            telepules_adatok.append(f"{n['telepules']} - {n['ferfi'] + n['no']} fő")

    oldalak_szama = (
        len(telepules_adatok) + terminal_height - 1
    ) // terminal_height

    aktualis_oldal = 0

    while True:
        kezdo_index = aktualis_oldal * terminal_height
        veg_index = kezdo_index + terminal_height

        aktualis_oldal_adatok = telepules_adatok[
            kezdo_index:veg_index
        ]

        print("\n" + "-" * 40)

        for elem in aktualis_oldal_adatok:
            print(elem)

        print("-" * 40)

        print(
            f"Oldal: {aktualis_oldal + 1}/{oldalak_szama}"
        )

        if aktualis_oldal == 0:
            print("[N] Következő oldal")
            print("[X] Kilépés")
        elif aktualis_oldal == oldalak_szama - 1:
            print("[B] Előző oldal")
            print("[X] Kilépés")
        else:
            print("[B] Előző oldal")
            print("[N] Következő oldal")
            print("[X] Kilépés")

        lapozas = input("Válasszon: ").strip().lower()

        if lapozas == "n":
            if aktualis_oldal < oldalak_szama - 1:
                aktualis_oldal += 1
            else:
                print("Már az utolsó oldalon van!")
        elif lapozas == "b":
            if aktualis_oldal > 0:
                aktualis_oldal -= 1
            else:
                print("Már az első oldalon van!")
        elif lapozas == "x":
            break
        else:
            print("Hibás választás!")


def main():
    while True:
        print()
        print("----- Népesség 2025 -----".center(40))
        print("[1] Megye adatai")
        print("[2] Település típusa")
        print("[X] Kilépés")

        menupont_bevitel = input("Írd be a választott menüpont sorszámát: ").strip().lower()

        if menupont_bevitel == "x":
            print("Program vége.")
            break

        menupont_valaszto(menupont_bevitel)


main()