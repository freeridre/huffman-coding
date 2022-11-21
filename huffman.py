from util import Colors, Symbol
import heapq, os

C = Colors()
Fg = C.ForeGround()
Sym = Symbol()

class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        # defining comparators less_than and equals
        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if(other == None):
                return False
            if(not isinstance(other, HeapNode)):
                return False
            return self.freq == other.freq

    # Fuggvenyek a kodolashoz:

    def make_frequency_dict(self, text: str) -> dict():
        """Megszamoljuk, hogy az egyes karakterek hanyszor fordulnak elo.

        Args:
            text (str): Titkositando szoveg.

        Returns:
            dict(): Konyvtarat ad vissza, amelynek kulcsa az aktualis betu, es az erteke a betu gyakorisaganak szama.
        """
        
        # Konyvtar deklaralasa.
        frequency = dict()

        # Vegig iteralunk a karaktereken.
        for character in text:

            # Ha meg nincs benne a karakter a konytar kulcsaiban, akkor letrehozzuk a kulcsot es 0 ertekkel deklaraljuk.
            if not character in frequency:
                frequency[character] = 0
            # Ha mar korabban talaltunk pl. "a" betut, akkor egyel noveljuk a gyakorisaganak a szamat.
            frequency[character] += 1

        # Visszaadjuk a karakterek gyakorisaganak szamat egy konyvtarban. A konyvtar kulcsai a betuk,
        # az ertekek pedig az adott betu elofordulasanak a szama.
        return frequency

    def __make_heap(self, frequency: dict) -> None:
        # Vegig iteralunk a gyakorisagokon. Letre hozzuk a bianris fat a betuk gyakorisaga alapjan.
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def __merge_nodes(self) -> None:
        """Addig adjuk ossze a betuk gyakorisaganak szamat, amig az elemek szama nagyobb, mint egy a heap-ben.
        """
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            # Osszeadjuk a ket legkisebb gyakorisagu betu gyakorisagat.
            merged = self.HeapNode(None, node1.freq + node2.freq)

            # Mindig az aktualis ket legkisebb gyakorisagu betu szamat elmentjuk.
            merged.left = node1
            merged.right = node2

            # Frissitjuk a binaris fat.
            heapq.heappush(self.heap, merged)

    def __make_codes_helper(self, root, current_code):
        # Ha ures a fank, akkor uresen visszaterunk.
        if(root == None):
            return None

        # Amennyiben az adott betu kodolva van, akkor elmentjuk a binaris kodjat. A codes-nal a kulcs a betu,
        # a reverse_mapping eseteben a kulcs az adott betu binaris kodolasa.
        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return None

        # Rekurziv hivassal a baloldali gyakorisagokat 0-val, a jobboldali gyakorisagokat 1-gyel kodoljuk.
        self.__make_codes_helper(root.left, current_code + "0")
        self.__make_codes_helper(root.right, current_code + "1")


    def __make_codes(self) -> None:
        """_summary_
        """
        # Kiszedjuk a gyakorisagi fat a root-ba. A root tartalmazza a gyakorisagi fat, melyet le tudunk bontani.
        root = heapq.heappop(self.heap)
        current_code = str()
        self.__make_codes_helper(root, current_code)


    def __get_encoded_text(self, text: str) -> str:
        """Mindenegyes betunek a kodjat hozzarendeljuk az encoded_text string-hez.

        Args:
            text (str): kodolni kivant szoveg

        Returns:
            str: Kodolt binaris sorozat
        """
        encoded_text = str()
        for character in text:
            encoded_text += self.codes[character]

        if (len(encoded_text) < 10000):
            print(Sym._info, Fg._orange, "Szoveg kodoltan: ", Fg._blue + encoded_text, C._reset)

        return encoded_text


    def __pad_encoded_text(self, encoded_text: str):
        extra_padding = 8 - len(encoded_text) % 8
        # Paddingtol fuggoen plusz 0 bitet adunk a bit-stream vegehez.
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text


    def __get_byte_array(self, padded_encoded_text: str) -> bytearray():
        """_summary_

        Args:
            padded_encoded_text (str): kodolt szoveg.

        Returns:
            bytearray(): kodolt szoveg bytearray-ben.
        """
        if(len(padded_encoded_text) % 8 != 0):
            print(Sym._crossed, Fg._red, "Kodolt szoveg hibas" + Sym._exclamation, C._reset)
            exit(0)

        b = bytearray()

        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))

        return b


    def _titkosit(self) -> str:
        """Visszaadja a titkositott fajlt .bin kiterjesztesben.

        Returns:
            str: Titkositott fajl.
        """

        # Szetszedjuk fajl nevre es fajl kiterjesztesre a megadott fajlt.
        filename, file_extension = os.path.splitext(self.path)

        # A kimeneti fajlt kiterjesztese .bin tipusu lesz.
        output_path = filename + ".bin"

        # Azert nyitjuk meg with-el a fajlokat, mert a with automatikusan be is zarja a fajlokatt, mitutan mar nem hasznaljuk Oket.
        # Az r az sima olvasas, az r+ olvasas, es iras is, a wb az binaris fajl irasat jelenti.
        # https://docs.python.org/3/library/functions.html#open
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            # beolvassuk a fajlt.
            text = file.read()
            # Toroljuk a felesleges sorvegi karaktereket pl \n, " ".
            text = text.rstrip()

            # Gyakorisagi fa elokeszitese.
            frequency = self.make_frequency_dict(text)

            # Letre hozzuk a binaris fat a python heapq moduljaval. A Huffman-kod gyakorlatilag a betuk gyakorisaganak a binaris fajabol kodolt binaris stream.
            self.__make_heap(frequency)
            self.__merge_nodes()
            self.__make_codes()

            # Kodolt szoveget elmentjuk egy valtozoba.
            encoded_text = self.__get_encoded_text(text)

            padded_encoded_text = self.__pad_encoded_text(encoded_text)

            b = self.__get_byte_array(padded_encoded_text)
            output.write(bytes(b))

        print(Sym._check_box, Fg._green, "Kodolva" + Sym._exclamation, C._reset)
        return output_path


    """ Fuggvenyek a dekodolashoz: """


    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:] 
        encoded_text = padded_encoded_text[:-1*extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code, decoded_text = str()

        for bit in encoded_text:
            current_code += bit
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = str()

        return decoded_text


    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = str()

            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)
            
            output.write(decompressed_text)

        print(Sym._check_box, Fg._green, "Dekodolva" + Sym._exclamation, C._reset)
        return output_path

