import unicodedata

def normalice_text(texto:str)->str:
    """Quita las tildes a un texto

    Args:
        texto (str): Cadena de texto al que se le quitarán las tildes

    Returns:
        str: Cadena de texto sin tildes
    """
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto