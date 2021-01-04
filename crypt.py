import personal
keys = personal.PERSONAL_KEYS


def get_string():
    return input("Type some text\n>>>")


def crypt(text):
    out = ''
    for litter in text:
        out += keys[litter]
    return out


if __name__ == '__main__':
    some_text = get_string()
    print(crypt(some_text))
