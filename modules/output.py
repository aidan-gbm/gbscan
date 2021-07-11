from colorama import Fore, Style

def log(msg: str):
    print(Fore.LIGHTBLUE_EX + '[#]' + Style.RESET_ALL, msg)

def err(msg: str):
    print(Fore.YELLOW + '[!]' + Style.RESET_ALL, msg)

def success(msg: str):
    print(Fore.LIGHTGREEN_EX + '[+]' + Style.RESET_ALL, end=' ')
    print(msg + '\n') if msg else print('Success\n')

def fail(msg: str):
    print(Fore.LIGHTRED_EX + '[-]' + Style.RESET_ALL, end=' ')
    print(msg + '\n') if msg else print('Success\n')
