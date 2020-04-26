from colorama import init #initiates the colorama module
init()

from colorama import Fore, Back, Style #Fore - text color, Back - back color, Style - font type
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

