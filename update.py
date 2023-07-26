import requests
import os
import sys

def getGithubContent(url):
    headers = {'Accept': 'application/vnd.github.v3.raw'}
    try:
        response = requests.get(url, headers=headers)
    except:
        print('\033[33mUnable to access remote content, Skipping update...\033[0m')
        sys.exit()
    if response.ok: return response.json()
    else: return False

def update(response):
    if response:
        print('\033[32mChecking for updates...\033[0m')
        # Updating update.py
        for i in response:
            if i['name'] == 'update.py':
                try:
                    remote = requests.get(i['download_url']).text
                except:
                    print('\033[31mUnable to access remote content, Skipping update...\033[0m')
                    return
                with open(__file__, 'r', encoding='utf-8') as this:
                    local = this.read()
                if local != remote:
                    with open(__file__, 'w', encoding = 'utf-8') as this:
                        this.write(remote)
                        print('\033[32mSucessfully updated update.py\033[0m')
                        sys.exit()
        # Downloading missing files
        for i in response:
            if i['type'] == 'file' and i['name'][0] != '.' and i['name'] != 'update.py':
                if not i['name'] in os.listdir():
                    try:
                        remote = requests.get(i['download_url']).text
                    except:
                        print('\033[31mUnable to access remote content, Skipping update...\033[0m')
                        return
                    with open(i['name'], 'w', encoding = 'utf-8') as file:
                        file.write(remote)
                        print(f"\033[32mSuccesfully downloaded {i['name']}\033[0m")
        # Updating the existing content (except for other folders, update.py and dot-files)
        for i in response:
            if i['type'] == 'file' and i['name'][0] != '.' and i['name'] != 'update.py':
                try:
                    remote = requests.get(i['download_url']).text
                except:
                    print('\033[31mUnable to access remote content, Skipping update...\033[0m')
                    return
                with open(i['name'], 'r', encoding = 'utf-8') as this:
                    local = this.read()
                if remote != local:
                    with open(i['name'], 'w', encoding = 'utf-8') as file:
                        file.write(remote)
                        print(f"\033[32mSuccessfully updated {i['name']}\033[0m")
    else:
        print('\033[31mUnable to access remote content, Skipping update...\033[0m')
        return

update(getGithubContent('https://api.github.com/repos/anirudh-meshram/College-Schedule/contents/'))
