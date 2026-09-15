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

for n in nepesseg_adatok:
    print(n)

def menupont_valaszto(menupont):
    match menupont:
        case "1": megye_adatok()
        case "2": telepules_tipus()
        case "x": return

def telepules_tipus_menupontok():
    telepules_tipusok = []

    for n in nepesseg_adatok:
        if n["tipus"] in telepules_tipusok:
            continue
        else:
            telepules_tipusok.append(n["tipus"])

    for index, tipus in enumerate(telepules_tipusok):
        print(f"[{index + 1}] {tipus}")

    telepules = input("Kérem a település típusának sorszámát: ")

    return telepules_tipusok[int(telepules) - 1]
        


def megye_adatok():
    megyekod_bevitel = input("Kérem a megye kódját: ")

    telepulesek_szama = 0
    lakosok_szama = 0
    varosok_lakoinak_szama = 0

    for n in nepesseg_adatok:
        if n["megyekod"].lower() == megyekod_bevitel.lower():
            telepulesek_szama += 1
            lakosok_szama += n["ferfi"] + n["no"]

            if n["tipus"].lower() == "város" or n["tipus"].lower() == "vármegyei jogú város" or n["tipus"].lower() == "vármegye székhely":
                varosok_lakoinak_szama += n["ferfi"] + n["no"]

    print(f"Települések száma: {telepulesek_szama}")
    print(f"Összes lakos: {lakosok_szama} fő")
    print(f"Városok lakosai összesen: {varosok_lakoinak_szama} fő")


def telepules_tipus():
    print("Válasszon településtípust!")
    telepules_tipus = telepules_tipus_menupontok()

    terminal_height = os.get_terminal_size().lines

    telepules_adatok = []

    for n in nepesseg_adatok:
            if n["tipus"].lower() == telepules_tipus.lower():
                telepules_adatok.append(f"{n['telepules']} - {n['ferfi'] + n['no']} fő")

    for i in range(terminal_height - 1):
        if i < len(telepules_adatok):
            print(telepules_adatok[i])
        else:
            break



def main():
    print("----- Népesség 2026 -----".center(40))
    print("[1] Megye adatai")
    print("[2] Település típusa")
    print("[X] Kilépés")

    menupont_bevitel = input("Írd be a választott menüpont sorszámát: ")

    menupont_valaszto(menupont_bevitel)


main()