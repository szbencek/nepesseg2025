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
        case "3": pass
        case "x": main()
        


def megye_adatok():
    megyekod_bevitel = input("Kérem a megye kódját: ")

    telepulesek_szama = 0
    lakosok_szama = 0
    varosok_lakoinak_szama = 0

    for n in nepesseg_adatok:
        if n["megyekod"].lower() == megyekod_bevitel.lower():
            telepulesek_szama += 1
            lakosok_szama += n["ferfi"] + n["no"]

            if n["tipus"].lower() == "város":
                varosok_lakoinak_szama += n["ferfi"] + n["no"]

    print(f"Települések száma: {telepulesek_szama}")
    print(f"Összes lakos: {lakosok_szama}")
    print(f"Városok lakosai összesen: {varosok_lakoinak_szama}")

def telepules_tipus():
    pass


def main():
    print("----- Népesség 2026 -----".center(40))
    print("[1] Megye adatai")
    print("[2] Település típusa")
    print("[3]")
    print("[X] Kilépés")

    menupont_bevitel = input("Írd be a választott menüpont sorszámát: ")

    menupont_valaszto(menupont_bevitel)


main()