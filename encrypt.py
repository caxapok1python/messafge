import keychain
keys = keychain.PERSONAL_KEYS


def get_string():
    return input("Type a Text\n>>>")


def crypt(text):
    out = ''
    for litter in text:
        out += keys[litter]
    return out


def main():
    some_text = get_string()
    print(crypt(some_text))


if __name__ == '__main__':
    main()
