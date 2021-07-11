from colorama import Fore, Style

def log(msg: str):
    print(Fore.LIGHTBLUE_EX + '[#] ' + msg + Style.RESET_ALL)

def err(msg: str):
    print(Fore.YELLOW + '[!] ' + msg + Style.RESET_ALL)

def success(msg: str):
    if msg:
        print(Fore.LIGHTGREEN_EX + '[+] ' + msg + Style.RESET_ALL)
    else:
        print(Fore.LIGHTGREEN_EX + '[+] Success' + Style.RESET_ALL)

def fail(msg: str):
    if msg:
        print(Fore.LIGHTRED_EX + '[-] ' + msg + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + '[-] Fail' + Style.RESET_ALL)