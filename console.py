from colorama import *
import encrypt
import decrypt
init()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

hello = """
--|----------------------------------------------------------------------------------|--
  |   m    m    mmmmmm     mmmm      mmmm       mm      mmmmmm      mmm     mmmmmm   |  
  |   ##  ##    #         #"   "    #"   "      ##      #         m"   "    #        | 
  |   # ## #    #mmmmm    "#mmm     "#mmm      #  #     #mmmmm    #   mm    #mmmmm   |
  |   # "" #    #             "#        "#     #mm#     #         #    #    #        |
  |   #    #    #mmmmm    "mmm#"    "mmm#"    #    #    #          "mmm"    #mmmmm   |
--|----------------------------------------------------------------------------------|--
                                                                    by caxapok1python
"""
separator = "----------------------------------------------------------------------------------------"
symbols = "You can use all English and Russian litters and some symbols"
punctuation = '!#$%&()*+,-./:;<=>?@[]^_`{|}~'

modes = f"{Fore.YELLOW}[!]{Fore.RESET} 1(e): Encrypt\n" \
        f"{Fore.YELLOW}[!]{Fore.RESET} 2(d): Decrypt"

invalid_mode = f"{Fore.RED}[ø]{Fore.RESET} Invalid mode"


def get_text(type):
    if type == 'plain':
        text = input(f"{Fore.GREEN}[+] {Fore.RESET}Type some text\n"
                     f"{Fore.YELLOW}[!] {Fore.RESET}{symbols}{punctuation}\n"
                     f">>>{Fore.GREEN}")
        return text
    else:
        text = input(f"{Fore.GREEN}[+] {Fore.RESET}Paste Encrypted text\n"
                     f">>>{Fore.GREEN}")
        return text


def crypt(text):
    return encrypt.crypt(text)


def dcrypt(text):
    return decrypt.encrypt(text)


if __name__ == '__main__':
    print(Fore.MAGENTA, hello, Fore.RESET)
    while True:
        mode = input(f"{Fore.GREEN}[+]{Fore.RESET} Choose mode\n"
                     f"{modes}\n"
                     f">>>{Fore.GREEN}")

        if mode == '':
            print(invalid_mode)
        elif mode == '1' or mode == 'e':
            print(f"{Fore.GREEN}[+]{Fore.RESET} Encrypted text:\n"
                  f"{Fore.RED}{crypt(get_text('plain'))}{Fore.RESET}\n"
                  f"{Fore.MAGENTA}{separator}{Fore.RESET}")
        elif mode == '2' or mode == 'd':
            print(f"{Fore.GREEN}[+]{Fore.RESET} Decrypted text:\n"
                  f"{Fore.RED}{dcrypt(get_text('encrypted'))}{Fore.RESET}\n"
                  f"{Fore.MAGENTA}{separator}{Fore.RESET}")
        else:
            print(invalid_mode)
