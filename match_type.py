import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from tabulate import tabulate as table
from time import sleep
import sys
import os

def generateData():
    try:
        print('Loading...\n')
        page = requests.get('http://time-table.sicsr.ac.in/day.php?year={}&month={}&day={}&area=1&room=29'.format(dt.now().year, dt.now().month if str(dt.now().month).startswith('0') else str('0'+str(dt.now().month)), dt.now().day),timeout=5).text
    except:
        print('\033[31mERROR: Connection failed! Please try again!\033[0m')
        sys.exit(1)
    soup = bs(page, 'html.parser')
    options = soup.find(id='type').prettify().split('\n')
    for i in options:
        if i.strip() == '' or i.strip() == '</option>' or i.strip() == '<select id="type" name="type">':
            options.pop(options.index(i))
    for i in range(len(options)):
        options[i] = options[i].strip()
    options.pop()
    types = {}
    for i in range(len(options)):
        if options[i].startswith('<'):
            types[list(types.keys())[-1]+1 if len(types)>= 1 else 0] = [options[i][options[i].index('"')+1], options[i+1]]
    dataset = []
    for i in types:
        dataset.append([i, types[i][-1]])
    return (types, dataset)

def getChoice():
    types, dataset = generateData()
    print(table(dataset, headers = ["S. No", "Subject"], tablefmt='simple'))       # Printing the information in a table
    print('\n\033[36m( Scroll up to see the entire list )\n\033[0m')
    while True:
        choice = input('\nEnter your choices separated by commas\nFor example: 0,2\tOR\t 1,3,5\n\n> ')
        choice = choice.split(',') 
        try:
            print('\nYou have chosen:\n')
            for i in choice:
                print(types[int(i)][-1])
        except (KeyError, ValueError):
            print('\033[31mInvalid input!\033[0m')
            print('\033[33mLoading your choices again...\033[0m')
            sleep(1.5)
            continue
        confirm = input('\n\033[32mConfirm? (Enter "y" to confirm, any other key to choose again)\n\n> \033[0m')
        if confirm != 'y' and confirm != 'Y': continue
        break
    with open('.config', 'w+', encoding='utf-8') as config:
        for i in choice:
            config.write(types[int(i)][0])
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print('\033[32mSuccessfully generated .config file\033[0m')
        print('\n\033[33mIMPORTANT: If you want to reset your configuration, Remove the file ".config" from your project directory\n\033[0m')
        input('\033[32mPress Enter to continue\033[0m')
        os.system('cls') if os.name == 'nt' else os.system('clear')
getChoice()
