import requests , os , time 
from colorama import Fore
import random
logo = f"""

███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░░██████╗███████╗░█████╗░░█████╗░████████╗
████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝╚█████╗░█████╗░░███████║██║░░╚═╝░░░██║░░░
██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░██╔══██║██║░░██╗░░░██║░░░
██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║██████╔╝██║░░░░░██║░░██║╚█████╔╝░░░██║░░░
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░

                              {Fore.WHITE + 'Made By Team Intraneno(ishan)'}
"""
print(Fore.BLUE + logo)
factype = input(Fore.RED + f' \n Choose The Type Of Fact You Want \n The Type Of Facts Are Given Below \n 1 - Math \n 2 - Trivia \n 3 - Date  \n 4 - Random  \n $ : ')
# formatt = 2/20
# /    CHECKS     \
if factype == '1':
    number = input(Fore.CYAN +  f'Enter Number: \n')
    mresult = requests.get(f'http://numbersapi.com/{number}/math')
    print( Fore.GREEN + f'The Math Number Fact: \n {Fore.WHITE + mresult.text} ')
    time.sleep(6)
    os.system('cls')
    os.system('python fact.py')
elif factype == "2":
    number = input(Fore.CYAN +  f'Enter Number: \n')
    tresult = requests.get(f'http://numbersapi.com/{number}/')
    print( Fore.GREEN + f'The Trivia Number Fact: \n {Fore.WHITE + tresult.text} ')
    time.sleep(6)
    os.system('cls')
    os.system('python fact.py')
elif factype == "3":
    month = input(Fore.BLUE + 'Enter Month : \n')
    day = input(Fore.BLUE + 'Enter Day : \n ')
    tresult = requests.get(f'http://numbersapi.com/{month}/{day}/date')
    print( Fore.GREEN + f'The Date Number Fact: \n {Fore.WHITE + tresult.text} ')
    time.sleep(6)
    os.system('cls')
    os.system('python fact.py')
elif factype == "4":
    types = ["math" , 'trivia' , "date"]
    ntype =  random.choice(types)
    if ntype == "math":
        number = input(Fore.CYAN +  f'Enter Number: \n')
        r1result = requests.get(f'http://numbersapi.com/{number}/math')
        print( Fore.GREEN + f'The Math Number Fact: \n {Fore.WHITE + r1result.text} ')
        time.sleep(6)
        os.system('cls')
        os.system('python fact.py')
    elif ntype == 'trivia':
        number = input(Fore.CYAN +  f'Enter Number: \n')
        r2result = requests.get(f'http://numbersapi.com/{number}/math')
        print( Fore.GREEN + f'The Trivia Number Fact: \n {Fore.WHITE + r2result.text} ')
        time.sleep(6)
        os.system('cls')
        os.system('python fact.py')
    elif ntype == 'date':
        month = input(Fore.BLUE + 'Enter Month : \n')
        day = input(Fore.BLUE + 'Enter Day : \n ')
        r3result = requests.get(f'http://numbersapi.com/{month}/{day}/date')
        print( Fore.GREEN + f'The Date Number Fact: \n {Fore.WHITE + r3result.text} ')
        time.sleep(6)
        os.system('cls')
        os.system('python fact.py')  
elif factype != '1' or '2' or '3' or '4':
    print('Pls Try Again Entering The Number According The Serial Above! ') 