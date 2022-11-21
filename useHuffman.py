from huffman import HuffmanCoding
from util import Colors, Symbol
import os, sys

# Peldanyositasok.
C = Colors()
Fg = C.ForeGround()
Sym = Symbol()

def main() -> None:
    """Ez a main fuggveny, amelynel bekerjuk a titkositando txt fajlt. Leellenorizzuk, hogy jo-e az eleresi ut, amennyiben nem, akkor kilepunk a programbol
        es ezt a felhasznalo tudtara is adjuk, amennyiben jo volt az eleresi ut, akkor leellenorzzuk, hogy txt fajlt adtunk-e meg, ha nem, ismet jelezzuk a
        hibat a felhasznalonak es kilepunk a programbol. Ha minden feltetel teljesult, interfeszen keresztul kodoljuk, illetve dekodoljuk a titkositando txt fajlt."""

    if (sys.version_info[0] < 3 and sys.version_info[1] < 10):
        print(Sym._crossed + Fg._red, " Python 3.10 alatt nem tamogatott a kod" + Sym._exclamation, C._reset)
        exit(0)
    

    print(Sym._info, Fg._cyan, "Kerem, hogy add meg az eleresi utjat annak a txt fajlnak, amit titkositani szeretnel " + Sym._exclamation, C._reset)
    # Bekerjuk a fajl-t.
    file_path = input()

    # Ha jo az eleresi ut.
    if os.path.exists(file_path):
        # Ha nem txt a fajlt kiterjesztese, akkor hibat dobunk.
        if not (file_path.endswith(".txt")):
            print(Sym._crossed + Fg._red, " Nem txt fajlt adtal meg" + Sym._exclamation, C._reset)
            exit(0)
    # Ha ures az eleresi ut, akkor is hibat dobunk.
    elif not os.path.exists(file_path):
        print(Sym._crossed, Fg._red, " Ures eleresi utat adtal meg" + Sym._exclamation, C._reset)
        exit(0)
    # Barmi mas eseten hibas az eleresi ut.
    else:
        print(Sym._crossed, Fg._red, " Hibas eleresi utat adtal meg" + Sym._exclamation, C._reset)
        exit(0)
    # Peldanyositjuk a titkosito class-t.
    h = HuffmanCoding(file_path)

    # Kodoljuk a szoveget.
    output_path = h._titkosit()
    print(Sym._info, Fg._orange, "Kodolt fajl:", Fg._blue + output_path, C._reset)

    # Dekodoljuk a szoveget.
    decom_path = h.decompress(output_path)
    print(Sym._info, Fg._orange, "Dekodolt fajl: ", Fg._blue + decom_path, C._reset)

# Innen kezdodik a programunk. Amennyiben a python interpreter megtalalja a main() fuggveny, akkor meghivja azt.
# C es C++-ban alapbol megtalalhato a main fuggveny. Pythonban, ez explicit nem letezik, ezert definialjuk, hogy
# ne az elso identalastol induljon a programunk.
if __name__ == "__main__":
    main()
