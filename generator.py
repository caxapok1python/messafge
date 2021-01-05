import random
import string

litters_en = string.ascii_letters
litters_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
digits = string.digits
punctuation = '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
SYMBOLS = litters_en + digits + punctuation
ALPHABET = litters_en + litters_ru + digits + punctuation


def generate_key():
    global SYMBOLS
    return ''.join(random.sample(SYMBOLS, 6))


def check_key(key):
    global punctuation
    for litter in key:
        if litter in punctuation:
            return True
    return False


def true_key():
    while True:
        key = generate_key()
        check = check_key(key)
        if check:
            return key


def generate_dict():
    keychain = {}
    for symbol in ALPHABET:
        keychain[symbol] = true_key()
    return keychain


def write_key_to_file(keys):
    with open(f"keychain.py", 'w') as file:
        file.write(f"PERSONAL_KEYS = {keys}")


if __name__ == '__main__':
    personal = generate_dict()
    write_key_to_file(personal)
else:
    pass
