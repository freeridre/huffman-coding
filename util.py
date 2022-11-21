from dataclasses import dataclass

"""Ez a fajlt dataclass-okat tartalmaz, amelyeket a foprogramban hasznalunk fel."""

@dataclass(slots = True)
class StoreHuffman:
    path: str
    heap: list
    codes: dict
    reverse_mapping: dict

@dataclass(frozen = True, slots = True)
class Symbol:
    """Symbols class, amely emoji unicode-jat tartalmazza. Azert dataclass, mert python 3.9-tol mar lehet ugy class tagokat inicializalni,
    hogy nem kell hozza explicit konstruktort (__init__()) hivni. frozen = True, azt jelenti, hogy a dataclass tagok ertekei nem tudnak megvaltozni,
    a slots = True pedig optimalizacio szempontjabol lett alkalmazva, python 3.10 mar lehet alkalamzni."""

    _crossed: str = "\U0000274E"
    _check_box: str = "\U00002705"
    _exclamation: str = "\U00002757"
    _info: str = "\U00002139"

@dataclass(frozen=True, slots=True, repr = False)
class Colors:
    """Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold"""

    _reset: str = '\033[0m'
    _bold: str = '\033[01m'
    _disable: str = '\033[02m'
    _underline: str = '\033[04m'
    _reverse: str = '\033[07m'
    _strikethrough: str = '\033[09m'
    _invisible: str = '\033[08m'

    @dataclass(frozen=True, slots=True)
    class ForeGround:
        """Fore ground colors of the debug messages."""
        _black: str = '\033[30m'
        _red: str = '\033[31m'
        _green: str = '\033[32m'
        _orange: str = '\033[33m'
        _blue: str = '\033[34m'
        _purple: str = '\033[35m'
        _cyan: str = '\033[36m'
        _lightgrey: str = '\033[37m'
        _darkgrey: str = '\033[90m'
        _lightred: str = '\033[91m'
        _lightgreen: str = '\033[92m'
        _yellow: str = '\033[93m'
        _lightblue: str = '\033[94m'
        _pink: str = '\033[95m'
        _lightcyan: str = '\033[96m'


    @dataclass(frozen=True, slots=True)
    class BackGround:
        """Back ground colors of the debug messages."""
        _black: str = '\033[40m'
        _red: str = '\033[41m'
        _green: str = '\033[42m'
        _orange: str = '\033[43m'
        _blue: str = '\033[44m'
        _purple: str = '\033[45m'
        _cyan: str = '\033[46m'
        _lightgrey: str = '\033[47m'