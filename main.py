# Installing Dependencies
import os
import sys
import subprocess

def update():
    try:
        subprocess.run(['python3', 'update.py'], check=True)
    except:
        print('\033[31mUnable to run update.py\033[0m')
        sys.exit()

def generateConfig():
    try:
        subprocess.run(['python3', 'match_type.py'], check=True)
    except:
        print('\033[31mUnable to run match_type.py\033[0m')
        sys.exit()

def ensure_dependencies():
    # Looks for '.ensure_dependencies' in the root folder
    if not '.ensure_dependencies' in os.listdir():
        print('\033[35m.ensure_dependencies not found in the root directory. Installing dependencies... (Only for the first execution)\033[0m')
        with open('.ensure_dependencies','w+', encoding = 'utf-8') as file: file.write('True')
        ensure_pip()
        dependencies = ['requests', 'tabulate', 'bs4']
        for package in dependencies:
            try: subprocess.check_call(["pip","show",package])
            except subprocess.CalledProcessError:
                print(f"\033[33m{package} is not installed. Installing...\033[0m")
                try:
                    subprocess.check_call(["pip", "install", package])
                    print(f"\033[32m{package} installed successfully.\033[0m")
                except: print(f"\033[31mFailed to install {package}\033[0m")
            except FileNotFoundError:
                print('\033[31mERROR: pip not found or not reachable!\033[0m')
                print('\033[31mPlease make sure the following modules are installed using pip:\033[0m')
                print(*dependencies)
                sys.exit()
        print('--------------------------')
        print('\033[32mDependencies are installed\033[0m')
        print('--------------------------')
        os.system('cls') if os.name == 'nt' else os.system('clear')
                
def ensure_pip():
    try:
        import pip
        return True
    except ImportError:
        print("\033[31mpip not installed! Installing..\033[0m")
        pass

    py_version = sys.version_info[:2]
    if py_version == (2,7): install_command = "ez_setup.py"
    else: install_command = "get-pip.py"

    # Downloading the pip installation script
    url = f"https://bootstrap.pypa.io/{install_command}"
    try: subprocess.check_call([sys.executable, "-m", "ensurepip"])
    except subprocess.CalledProcessError: pass

    try: 
        import ensurepip
        return
    except subprocess.CalledProcessError:
        try:
            import urllib.request
            with urllib.request.urlopen(url) as response:
                script_content = response.read()
                exec(script_content)
        except Exception as e:
            print("\033[31mFailed to install pip:\033[0m", e)
            sys.exit()
    print("\033[32mpip is now installed\033[0m")
    return True
            
ensure_dependencies() # Ensure dependencies

def process_data(txt):
    dataset = []
    lecture = txt.split('\n')                                       # Converting each lecture into a single element
    lecture.pop(0)                                                  # Removing the headers 
    lecture.pop(-1)                                                 # and last empty dataset from the data
    for i in range(len(lecture)):
        lecture[i] = lecture[i].replace('"','')                     # Removing the existing "" characters
    details = []
    for i in lecture:
        details.append(i.split(','))                                # Splitting the list for only importing certain data
    for lecture in details:
        dataset.append([lecture[0], lecture[2], lecture[3][0:8], lecture[4][0:8], int(lecture[5][0])])
    return dataset                                                  # Return the processed data for displaying information

def display_results(dataset):
    if len(dataset)==0:                                             # If no lectures are there today
        print("\033[35mThere are no lectures today.\033[0m")
        sys.exit()
    noOfLectures = len(dataset)                                     # For displaying the total number of lectures
    noOfHours = 0                                                   # Storing the number of hours
    for i in dataset: noOfHours += i[-1]                            # Calculating the total numbers of hours
    print("Today is: \033[35m{}\033[0m".format(dt.today().strftime('%d-%m-%Y') if not datetime.now() > datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(temp[-1][-2].split(':')[0]),int(temp[-1][-2].split(':')[1]),int(temp[-1][-2].split(':')[2])) else getNextDate().strftime('%d-%m-%Y')))             # Displaying the date in DD-MM-YYYY format
    print("There are \033[35m{}\033[0m lectures today".format(noOfLectures))       # No. of Lectures
    print("You have to attend \033[35m{}\033[35m hours today\033[0m".format(noOfHours))    # No. of Hours
    print("Your college day starts from \033[35m{}\033[0m and ends at \033[35m{}\033[0m".format(dataset[0][2], dataset[-1][3]))
    print(table(dataset, headers = ["Lecture Name", "Room No.", "Start Time", "End Time", "Duration (in hrs)"], tablefmt='grid'))       # Printing the information in a table
    print('\n\033[33m(If the table is not properly visible, Kindly zoom out till the table fits the terminal window ( Ctrl + - ))\033[0m')

if not 'update.py' in os.listdir():
    print('\033[31mERROR: update.py missing in root directory. Kindly download the latest project files from:\033[0m')
    print('https://github.com/anirudh-meshram/College-Schedule')
else:
    update()

if not 'match_type.py' in os.listdir():
    print('\033[31mmatch_type.py missing in root directory. Kindly download the latest project files from:\033[0m')
    print('https://github.com/anirudh-meshram/College-Schedule')

if not '.config' in os.listdir():
    generateConfig()

# Using requests to make HTTP requests
import requests
from requests.exceptions import ConnectionError

# For displaying the information in a table
from tabulate import tabulate as table

# For import current data in order to get today's time-table from the website
from datetime import date as dt, timedelta
from datetime import datetime

def getNextDate():
    today = dt.today()
    delta = timedelta(days = 1)
    return today + delta

config = open('.config', 'r', encoding = 'utf-8').read()
types = ''

for i in config:
    types+='&typematch%5B%5D='+i

# Request URL gathered from Network data at time-table.sicsr.ac.in; Manipulating the string according to today's date
request_url = 'http://time-table.sicsr.ac.in/report.php?from_day={day}&from_month={month}&from_year={year}&to_day={day}&to_month={month}&to_year={year}&areamatch=&roommatch={types}&namematch=&descrmatch=&creatormatch=&match_confirmed=2&output=0&output_format=1&sortby=s&sumby=d&phase=2&datatable=1'.format(day = datetime.now().day, month = datetime.now().month, year = datetime.now().year, types = types)

try: results = requests.get(request_url,timeout=5)                                 # Making the HTTP request
except:
    print('\033[31mConnection Error!\033[0m')
    sys.exit()

temp = process_data(results.text)
if datetime.now() > datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(temp[-1][-2].split(':')[0]),int(temp[-1][-2].split(':')[1]),int(temp[-1][-2].split(':')[2])):
    print("\033[35mAs of now your lectures are over. Showing time-table for tomorrow\033[0m\n")
    tomorrow = getNextDate()
    request_url = 'http://time-table.sicsr.ac.in/report.php?from_day={day}&from_month={month}&from_year={year}&to_day={day}&to_month={month}&to_year={year}&areamatch=&roommatch={types}&namematch=&descrmatch=&creatormatch=&match_confirmed=2&output=0&output_format=1&sortby=s&sumby=d&phase=2&datatable=1'.format(day = tomorrow.day, month = tomorrow.month, year = tomorrow.year, types = types)
    try: results = requests.get(request_url,timeout=5)                                 # Making the HTTP request
    except:
        print('\033[31mConnection Error!\033[0m')
        sys.exit()
    display_results(process_data(results.text))
else:
    display_results(process_data(results.text))
