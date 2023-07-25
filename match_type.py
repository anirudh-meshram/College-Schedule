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
        print('Connection failed! Please try again!')
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
    print('\n(Scroll up to see the entire list)\n')
    while True:
        choice = input('\nEnter your choices separated by commas\nFor example: 0,2\tOR\t 1,3,5\n\n> ')
        choice = choice.split(',') 
        try:
            print('\nYou have chosen:\n')
            for i in choice:
                print(types[int(i)][-1])
        except (KeyError, ValueError):
            print('Invalid input!')
            print('Loading your choices again...')
            sleep(1.5)
            continue
        confirm = input('\nConfirm? (Enter "y" to confirm, any other key to choose again)\n\n> ')
        if confirm != 'y' and confirm != 'Y': continue
        break
    with open('.config', 'w+') as config:
        for i in choice:
            config.write(types[int(i)][0])
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print('Successfully generated .config file')
        print('\nIMPORTANT: If you want to reset your configuration, Remove the file ".config" from your project directory\n')
        input('Press Enter to continue')
        os.system('cls') if os.name == 'nt' else os.system('clear')
getChoice()