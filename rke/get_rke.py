#!/usr/bin/python3

# Source: https://docs.github.com/en/rest/repos/repos#list-repository-tags
#         https://github.com/rancher/rke/tags

import requests
import json
import subprocess
import os

###################################################################################

# Kubectl client should be the same or one version higher than Kubernetes
PINNED_VERSION = 'v1.4'

# Pages of github.com tags to search through (if you need to find older versions)
PAGES = 2

###################################################################################

def download_pages():
    output = []
    for n in range(PAGES):
        url = str("https://api.github.com/repos/rancher/rke/tags?per_page=100&page=" + str(n+1))
        response = requests.get(url)
        data = json.loads(response.text)
        output.append(data) 
    return output

def parse_tags():
    versions = []
    json_pages = download_pages()
    for data in json_pages:
        for x in range(len(data)):
            if '-' not in data[x]['name']:  # Excludes -alpha, -beta, -rc, -debug
                versions.append(data[x]['name'])
    return versions 

def latest_pinned_version():
    versions = parse_tags()
    return list(filter(lambda x: PINNED_VERSION in x, versions))[0]

# Locally installed version 
def check_installed_version():
    output = subprocess.check_output(['/usr/local/bin/rke','--version'])
    version = output.decode().split()[2]
    return version

def install_new_version(version):
    WGET = 'wget -q -O rke --show-progress https://github.com/rancher/rke/releases/download/' + version + '/rke_linux-amd64'
    os.system(WGET)    
    os.system('chmod 755 rke')
    os.system('sudo mv -v rke /usr/local/bin/')


if __name__ == '__main__':

    # What is the installed version?
    installed_version = check_installed_version()
    print("Installed: " + installed_version)

    # What is the latest "pinned" version available?
    latest_version = latest_pinned_version()
    #latest_version = 'v1.3.14'   # Uncomment for testing or downgrade
    print("Latest:    " + latest_version)

    # Download and install?
    if installed_version != latest_version:
        install = input("Install latest version? ")
        if install == 'y' or install == 'yes' or install == 'Y':
            install_new_version(latest_version)

