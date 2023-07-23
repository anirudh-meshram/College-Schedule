import requests
import os
import sys

def getGithubContent(url):
    headers = {'Accept': 'application/vnd.github.v3.raw'}
    response = requests.get(url, headers=headers)
    if response.ok: return response.json()
    else: return False

def update(response):
    if response:
        print('Checking for updates...')
        # Updating update.py
        for i in response:
            if i['name'] == 'update.py':
                try:
                    remote = requests.get(i['download_url']).text
                except:
                    print('Unable to access remote content, Skipping update...')
                    return
                with open(__file__, 'r') as this:
                    local = this.read()
                if local != remote:
                    with open(__file__, 'w') as this:
                        this.write(remote)
                        print('Sucessfully updated update.py. Please run main.py again')
                        sys.exit(1)
        # Downloading missing files
        for i in response:
            if i['type'] == 'file' and i['name'][0] != '.' and i['name'] != 'update.py':
                if not i['name'] in os.listdir():
                    try:
                        remote = requests.get(i['download_url']).text
                    except:
                        print('Unable to access remote content, Skipping update...')
                        return
                    with open(i['name'], 'w') as file:
                        file.write(remote)
                        print(f"Succesfully downloaded {i['name']}")
        # Updating the existing content (except for other folders, update.py and dot-files)
        for i in response:
            if i['type'] == 'file' and i['name'][0] != '.' and i['name'] != 'update.py':
                try:
                    remote = requests.get(i['download_url']).text
                except:
                    print('Unable to access remote content, Skipping update...')
                    return
                with open(i['name'], 'r') as this:
                    local = this.read()
                if remote != local:
                    with open(i['name'], 'w') as file:
                        file.write(remote)
                        print(f"Successfully updated {i['name']}")
    else:
        print('Unable to access remote content, Skipping update...')
        return

update(getGithubContent('https://api.github.com/repos/anirudh-meshram/College-Schedule/contents/'))
