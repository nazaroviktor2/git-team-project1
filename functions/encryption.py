"""Encryption functions."""
import string

ASCII_LOWER = list(string.ascii_lowercase)
ASCII_UPPER = list(string.ascii_uppercase)
LEN_ALP = len(ASCII_UPPER)


def encrypt_by_tsezar_en(text: str, key: int = 0) -> str:
    """Encrypt only english text by caesar ciphers.

    Args:
        text: str - text fot encrypt.
        key: int - key for encrypt.

    Returns: str - encrypted text.
    """
    if key > LEN_ALP:
        key = key - (LEN_ALP * (key // LEN_ALP))

    elif key <= -LEN_ALP:
        key = abs(key)
        key = (key - (LEN_ALP * (key // LEN_ALP))) * -1
    encrypted_text = ""
    for symbol in text:
        if symbol in ASCII_UPPER:
            index = ASCII_UPPER.index(symbol) + key
            if index >= LEN_ALP:
                index -= LEN_ALP
            encrypted_text += ASCII_UPPER[index]
        elif symbol in ASCII_LOWER:
            index = ASCII_LOWER.index(symbol) + key
            if index >= LEN_ALP:
                index -= LEN_ALP
            encrypted_text += ASCII_LOWER[index]
        else:
            encrypted_text += symbol
    return encrypted_text
