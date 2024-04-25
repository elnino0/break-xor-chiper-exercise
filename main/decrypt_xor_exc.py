import string
from itertools import cycle, product


def xor_strings(data: bytes, key: bytes) -> bytes:
    cycle_key = cycle(key)
    return bytes([a ^ b for a, b in zip(data, cycle_key)])


def xor_decrypt(encrypted_text: bytes, key: bytes) -> str:
    return xor_strings(encrypted_text, key).decode()


def guess_key(encrypted_text, key_size: int) -> set:

    if isinstance(encrypted_text, list):
        bytes_of_text = bytes(encrypted_text)
    elif isinstance(encrypted_text, str):
        bytes_of_text = encrypted_text.encode()
    else:
        raise ValueError("unexpected type")

    possible_match = set()
    for candidate_key in generate_key(key_size):
        resulte = xor_decrypt(bytes_of_text, candidate_key.encode())

        if verify_letters(string.printable, resulte):
            possible_match.add((resulte, candidate_key))

    return possible_match


def generate_key(length: int):
    chars = string.ascii_lowercase
    for item in product(chars, repeat=length):
        yield "".join(item)


def verify_letters(letters_index: str, text: str) -> bool:
    try:
        for c in text:
            if c not in letters_index:
                return False
    except Exception as e:
        print(e)
        return False

    return True
