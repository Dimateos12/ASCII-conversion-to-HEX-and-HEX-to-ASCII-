def ASCII_to_HEX(tekst):
    #tekst = input("Podaj tekst by przekonwertować go na liczby HEX ")
    lista = []
    lista.extend(tekst)
    print(lista)
    convert = list(map(lambda convert: format(ord(convert), "x"), lista))
    return str(convert)


def HEX_to_ASCII(tekst):
    #tekst  = input("Podaj tekst w Hex ")
    bity  = bytes.fromhex(tekst)
    ascii_tekst = bity.decode("ASCII")
    return str(ascii_tekst)

