import personal
keys = personal.PERSONAL_KEYS


def get_str():
    return input("ENTER CRYPT TEXT\n>>>")


def get_key(dic, value):
    for k, v in dic.items():
        if v == value:
            return k


def prepare_text(text):
    to_encrypt = []
    for i in range(0, len(text), 6):
        to_encrypt.append(text[i:i+6])
    return to_encrypt


def encrypt(string):
    out = ''
    for litter in string:
        out += get_key(keys, litter)
    return out


if __name__ == '__main__':
    crypt = get_str()
    print(encrypt(prepare_text(crypt)))
