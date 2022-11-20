from huffman import HuffmanCoding
import os, importlib.util, sys, subprocess, emoji
from util import colors, fg, bg
 
PACKAGE = "emoji"
success = False

def install(package):
    print(fg.orange, "Telepitjuk a(z) ", fg.blue, package, " csomagot")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--upgrade"])
    global success
    success = True

def start():
    print(fg.cyan, "Kerem, hogy add meg az eleresi utjat annak a txt fajlnak, amit titkositani szeretnel!", colors.reset)
    file_path = input()

    if os.path.exists(file_path):
        if not (file_path.endswith(".txt")):
            print(fg.red ,"Nem txt fajlt adtal meg!", colors.reset)
            exit(0)
    elif not os.path.exists(file_path):
        print(fg.red, "Ures eleresi ut!", colors.reset)
        exit(0)
    else:
        print(fg.red, "Hibas eleresiut!", colors.reset)
        exit(0)

    h = HuffmanCoding(file_path)

    output_path = h.compress()
    print("Kodolt fajl eleresiutja: " + output_path)

    decom_path = h.decompress(output_path)
    print("Dekodolt fajl eleresiutja: " + decom_path)

def main():

    is_present = importlib.util.find_spec(PACKAGE)

    if is_present is None:
        print(fg.orange, PACKAGE, fg.red, emoji.emojize(":cross:) nincs feltelepitve!", colors.reset)
        install(PACKAGE)
    else:
        global success
        success = True

    if success:
        print (fg.blue, ":check: Minden csomag fel can rakva! Kezdhetjuk a titkositast!", colors.reset)
        start()

if __name__=='__main__':
    main()